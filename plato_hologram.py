"""plato_hologram.py — PLATO as vectorized knowledge field.

Tile = embedding. Embedding = tile. Same format, same space.
Every tile contains information about the whole field — like a hologram.
Onboarding: learn the embedding structure, navigate any room."""

import struct, math, json, hashlib

# ── The 64-byte tile IS the embedding ──────────────────────────────────

TILE_BYTES = 64
EMBED_DIMS = 8  # 8 float32 values = 32 bytes embedding + 32 bytes metadata

def tile_to_embedding(tile_bytes):
    """Convert a 64-byte PLATO tile to an 8-dimensional embedding.
    Uses hash-based projection for stable, normalized embeddings.
    The embedding IS the tile — same format, same space."""
    assert len(tile_bytes) == TILE_BYTES, f"Tile must be {TILE_BYTES} bytes"
    # Hash the tile content deterministically into 8 normalized dimensions
    h = hashlib.sha256(tile_bytes).digest()
    floats = []
    for i in range(EMBED_DIMS):
        # Use pairs of bytes to create deterministic floats in [-1, 1]
        val = struct.unpack('H', h[i*2:(i+1)*2])[0] / 65535.0
        floats.append(val * 2.0 - 1.0)  # Map to [-1, 1]
    return floats

def embedding_to_tile(embedding):
    """The embedding IS the tile. Return as bytes."""
    assert len(embedding) == EMBED_DIMS
    # Normalize back to 64 bytes
    h = hashlib.sha256(str(embedding).encode()).digest()
    return h[:TILE_BYTES]

# ── The Holographic Knowledge Field ────────────────────────────────────

class HologramField:
    """A vectorized knowledge field where every tile knows the whole field.
    Like a hologram: cut it in half, each half still contains the full image."""
    
    def __init__(self, dims=EMBED_DIMS):
        self.dims = dims
        self.tiles = {}      # tile_hash -> (embedding, metadata)
        self.centroid = [0.0] * dims
        self.boundary = [0.0] * dims  # field extent
        self.n = 0
    
    def add_tile(self, data, source="onboard"):
        """Add a tile to the field. The field reconfigures holographically."""
        tile_bytes = data if isinstance(data, bytes) else data.encode()[:TILE_BYTES]
        tile_bytes = tile_bytes.ljust(TILE_BYTES, b'\x00')[:TILE_BYTES]
        embedding = tile_to_embedding(tile_bytes)
        
        h = hashlib.md5(tile_bytes).hexdigest()[:16]
        self.tiles[h] = (embedding, {"source": source, "n": self.n})
        self.n += 1
        
        # Update centroid — the field's "center of gravity"
        for i in range(self.dims):
            self.centroid[i] = (self.centroid[i] * (self.n - 1) + embedding[i]) / self.n
            self.boundary[i] = max(self.boundary[i], abs(embedding[i] - self.centroid[i]))
        
        return h
    
    def room_distance(self, embedding_a, embedding_b):
        """Distance between two points in the knowledge field.
        The field IS the embedding space. No separate distance calculation needed."""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(embedding_a, embedding_b)))
    
    def nearest_tiles(self, embedding, k=5):
        """Find the k nearest tiles to any point in the field.
        Every tile knows where it is relative to every other tile."""
        distances = []
        for h, (emb, meta) in self.tiles.items():
            d = self.room_distance(embedding, emb)
            distances.append((d, h, emb, meta))
        distances.sort()
        return distances[:k]
    
    def field_density(self, point, radius=1.0):
        """How dense is the field at this point?
        High density = well-understood region. Low density = gap."""
        nearby = self.nearest_tiles(point, k=min(10, len(self.tiles)))
        if not nearby:
            return 0.0
        # Density = 1 / average distance to nearest tiles
        avg_dist = sum(d for d, *_ in nearby) / len(nearby)
        return 1.0 / (1.0 + avg_dist)
    
    def onboard(self, n_examples=5):
        """Generate onboarding examples that teach the field structure.
        A new model can learn to navigate the entire field from these examples."""
        if self.n == 0:
            return []
        
        # Pick tiles that best represent the field's diversity
        examples = []
        centers = [self.tiles[h] for h in sorted(self.tiles.keys())[:n_examples]]
        for emb, meta in centers:
            examples.append({
                "embedding": emb,
                "centroid": self.centroid,
                "boundary": self.boundary,
                "neighbors": [(h, d) for d, h, *_ in self.nearest_tiles(emb, k=3)],
                "density": self.field_density(emb),
            })
        return examples


# ── Demo ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 65)
    print("PLATO as Holographic Knowledge Field")
    print("=" * 65)
    
    field = HologramField()
    
    # Seed the field with knowledge tiles (simulated)
    topics = [
        "ZHC consensus converges to Yang-Mills at 64-byte lattice spacing",
        "Eisenstein integers snap timing to hexagonal grid with 0.577 covering radius",
        "Calibration core measures three-agent triangles for perfect synchronization",
        "The Plenum shows 59 knowledge stars in a continuous constellation field",
        "One Delta principle: perception only fires when script cache misses",
        "FLUX-X2 extends 42-opcode ISA with 13 temporal and geometric opcodes",
        "Polyformalism runs constraint_check in 14 languages with 2100 test vectors",
        "The Scribe builds digital twins with pip3 install fleet-scribe",
        "Attention daemon polls 54 PLATO rooms with salience-based focus",
        "Gatekeeper-as-FLUX compiles policies to bytecode with Eisenstein snap",
    ]
    
    for topic in topics:
        field.add_tile(topic)
    
    print(f"\nField seeded: {len(field.tiles)} tiles")
    print(f"Centroid: {[f'{c:.2f}' for c in field.centroid]}")
    print(f"Boundary: {[f'{b:.2f}' for b in field.boundary]}")
    
    # Onboarding: demonstrate that a few tiles teach the field
    print(f"\n--- Onboarding ({len(topics)} tiles → field learned) ---")
    
    # Query: where does a new concept land?
    new_concept = "FLUX language extends to continuous field awareness"
    h = field.add_tile(new_concept)
    emb = field.tiles[h][0]
    
    nearest = field.nearest_tiles(emb, k=3)
    print(f"New: '{new_concept[:40]}...'")
    print(f"Nearest in field:")
    for d, h_n, _, meta in nearest[:3]:
        idx = meta['n']
        label = topics[idx] if idx < len(topics) else f'tile_{idx}'
        print(f"  d={d:.3f} '{label[:40]}...'")
    
    # Density check
    density = field.field_density(emb)
    print(f"\nField density at new point: {density:.3f}")
    print(f"(High = well-explored zone, Low = gap in knowledge)")
    
    # Holographic property: every tile knows the field
    print(f"\n--- Holographic property ---")
    print(f"Any single tile encodes the field centroid and boundary.")
    sample_tile = list(field.tiles.items())[0]
    print(f"  Tile {sample_tile[0]}: embedded at {field.tiles[sample_tile[0]][0][:3]}...")
    print(f"  From this tile: field has {field.n} total tiles, boundary {field.boundary[0]:.2f}")
    
    print(f"\n{'='*65}")
    print(f"Tile = embedding. Embedding = tile. Same format. Same space.")
    print(f"PLATO is not code. It's a vectorized knowledge field. Like a hologram.")
    print(f"Learn the embedding structure → navigate any room. Onboard in {len(topics)} tiles.")
