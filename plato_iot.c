/* plato_iot.c — PLATO as ESP32 native runtime.
 * 
 * A PLATO room IS an ESP32. Walking into the room = connecting to the device.
 * The room's runtime IS the firmware. Every tick = a T-minus event.
 * 64-byte tiles = cache lines = BLE packets = flash pages.
 *
 * Minimal design: fits in 512KB RAM, 4MB flash. No OS required.
 */

#include <stdint.h>
#include <string.h>
#include <stdbool.h>

/* ── PLATO tile: 64 bytes = 1 cache line = 1 radio packet ──────────── */

typedef struct __attribute__((packed)) {
    float embedding[8];     /* 32 bytes: position in knowledge field */
    uint8_t confidence;      /* 0-255: how sure are we about this tile */
    uint8_t t_minus;         /* ticks until next expected event */
    uint16_t crc;            /* integrity check */
    uint8_t payload[28];    /* room-specific data */
} plato_tile_t;

_Static_assert(sizeof(plato_tile_t) == 64, "PLATO tile must be 64 bytes");

/* ── ESP32 room: the device IS the room ────────────────────────────── */

typedef struct {
    plato_tile_t tiles[64];  /* 4KB tile buffer = 64 tiles */
    uint8_t n_tiles;         /* current tile count */
    uint32_t tick;           /* hardware tick counter */
    float centroid[8];       /* field center of gravity */
    float boundary[8];       /* field extent */
} plato_room_t;

static plato_room_t room;    /* The room IS the device state */

/* ── Core operations (no malloc, no OS) ────────────────────────────── */

void plato_init(void) {
    memset(&room, 0, sizeof(room));
    room.tick = 0;
}

uint32_t plato_tick(void) {
    /* One tick = one main loop iteration = one T-minus decrement.
     * Called from the hardware timer ISR or main loop. */
    room.tick++;
    
    /* Decrement all T-minus counters */
    for (int i = 0; i < room.n_tiles; i++) {
        if (room.tiles[i].t_minus > 0) {
            room.tiles[i].t_minus--;
            /* T-minus reached zero: fire the event */
            if (room.tiles[i].t_minus == 0) {
                /* T-minus is the trigger. Not the signal. */
                return room.tiles[i].crc;  /* event identifier */
            }
        }
    }
    return 0;  /* no event this tick */
}

int plato_add_tile(const plato_tile_t* tile) {
    /* Add a tile to the room. Room IS the tile buffer. */
    if (room.n_tiles >= 64) return -1;  /* room full */
    room.tiles[room.n_tiles++] = *tile;
    
    /* Update field centroid (running average) */
    int n = room.n_tiles;
    for (int i = 0; i < 8; i++) {
        room.centroid[i] = room.centroid[i] * (n - 1) / n + tile->embedding[i] / n;
        float dev = tile->embedding[i] - room.centroid[i];
        if (dev > room.boundary[i]) room.boundary[i] = dev;
        if (-dev > room.boundary[i]) room.boundary[i] = -dev;
    }
    return 0;
}

void plato_schedule(uint8_t tile_index, uint8_t t_minus) {
    /* Schedule a T-minus event. The tick decrements this counter.
     * When it reaches zero, the event fires — no sensor needed. */
    if (tile_index < room.n_tiles) {
        room.tiles[tile_index].t_minus = t_minus;
    }
}

/* ── Sensor integration: ESP32 peripherals as PLATO rooms ──────────── */

void plato_read_gpio(plato_tile_t* tile, uint32_t gpio_state) {
    /* A GPIO read IS a tile. Embed the pin states into the tile. */
    memset(tile, 0, sizeof(*tile));
    for (int i = 0; i < 8; i++) {
        tile->embedding[i] = (gpio_state & (1 << i)) ? 0.5f : -0.5f;
    }
    tile->confidence = 200;  /* high confidence — direct hardware read */
}

void plato_read_adc(plato_tile_t* tile, uint16_t adc_value, float scale) {
    /* An ADC reading IS a tile. Scale to [-1, 1] embedding. */
    memset(tile, 0, sizeof(*tile));
    tile->embedding[0] = (adc_value / 4095.0f) * 2.0f - 1.0f;
    tile->confidence = (uint8_t)(adc_value >> 4);  /* rough · no calibration yet */
}

/* ── Radio: BLE/ESP-NOW packets ARE tiles ───────────────────────────── */

typedef plato_tile_t radio_packet_t;
/* A radio packet IS a PLATO tile. 64 bytes. Same format. Send and receive rooms. */

int plato_send_room(const plato_room_t* local, plato_room_t* remote) {
    /* Send our room state to a neighbor.
     * One 64-byte packet per tile. The packet IS the tile. */
    for (int i = 0; i < local->n_tiles; i++) {
        /* radio_send((uint8_t*)&local->tiles[i], sizeof(plato_tile_t)); */
    }
    return local->n_tiles;
}

int plato_receive_room(plato_room_t* local, const plato_room_t* remote) {
    /* Receive a neighbor's room state.
     * Their tiles become our tiles. Their field merges with ours. */
    for (int i = 0; i < remote->n_tiles; i++) {
        plato_add_tile(&remote->tiles[i]);
    }
    return remote->n_tiles;
}

/* ── Main loop: the room ticks ────────────────────────────────────── */

int main(void) {
    plato_init();
    
    /* Seed the room with initial state */
    plato_tile_t boot_tile = {0};
    boot_tile.confidence = 255;
    boot_tile.t_minus = 0;
    plato_add_tile(&boot_tile);
    
    while (1) {
        /* Tick — one main loop iteration */
        uint32_t event = plato_tick();
        
        if (event) {
            /* T-minus reached zero. Fire the event. The signal is verification. */
            /* handle_event(event); */
        }
        
        /* Read sensors → tile them → add to room */
        plato_tile_t sensor_tile;
        plato_read_adc(&sensor_tile, 2048, 3.3f);
        plato_add_tile(&sensor_tile);
        
        /* Schedule next reading */
        plato_schedule(room.n_tiles - 1, 100);  /* fire in 100 ticks */
        
        /* Radio: exchange rooms with neighbors */
        /* plato_send_room(&room, &neighbor); */
        /* plato_receive_room(&room, &neighbor); */
        
        /* Simple delay (ESP32 ticks at 240MHz, ~1 tick = 4ns) */
        for (volatile int d = 0; d < 10000; d++);
    }
}
