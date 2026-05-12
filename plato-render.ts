/**
 * plato-render.ts — High-level PLATO room rendering for browsers.
 * 
 * PLATO rooms render as: game engines, boat dashboards, website backends.
 * One room, multiple renderings. Same tiles, different views.
 */

// ── PLATO Room Client ──────────────────────────────────────────────

interface PlatoTile {
  embedding: number[];  // 8-dim position in knowledge field
  confidence: number;   // 0-255
  t_minus: number;      // ticks until next event
  payload: string;      // room-specific data
}

interface PlatoRoom {
  name: string;
  tiles: PlatoTile[];
  centroid: number[];
  boundary: number[];
  tick: number;
}

class PlatoClient {
  private url: string;
  
  constructor(platoUrl: string) {
    this.url = platoUrl;
  }
  
  async joinRoom(roomName: string): Promise<PlatoRoom> {
    const resp = await fetch(`${this.url}/room/${roomName}`);
    if (!resp.ok) throw new Error(`Cannot join room: ${roomName}`);
    return resp.json();
  }
  
  async submitTile(room: string, tile: PlatoTile): Promise<void> {
    await fetch(`${this.url}/submit`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ room, tile }),
    });
  }
}

// ── Rendering Engine ────────────────────────────────────────────────

type RenderMode = 'game' | 'dashboard' | 'website';

interface Renderer {
  render(room: PlatoRoom, container: HTMLElement): void;
  onTick(room: PlatoRoom): void;
}

// ── Mode 1: Game Renderer ──────────────────────────────────────────

class GameRenderer implements Renderer {
  private canvas: HTMLCanvasElement;
  private ctx: CanvasRenderingContext2D;
  
  constructor() {
    this.canvas = document.createElement('canvas');
    this.canvas.width = 800;
    this.canvas.height = 600;
    this.ctx = this.canvas.getContext('2d')!;
  }
  
  render(room: PlatoRoom, container: HTMLElement): void {
    container.innerHTML = '';
    container.appendChild(this.canvas);
    
    const ctx = this.ctx;
    ctx.fillStyle = '#0a0a1a';
    ctx.fillRect(0, 0, 800, 600);
    
    // Draw tiles as entities in the game world
    room.tiles.forEach((tile, i) => {
      const x = ((tile.embedding[0] + 1) / 2) * 780 + 10;
      const y = ((tile.embedding[1] + 1) / 2) * 580 + 10;
      const size = tile.confidence / 255 * 20 + 5;
      
      ctx.beginPath();
      ctx.arc(x, y, size, 0, Math.PI * 2);
      ctx.fillStyle = `hsl(${i * 36}, 70%, ${50 + tile.confidence / 5}%)`;
      ctx.fill();
      ctx.strokeStyle = '#ffd700';
      ctx.lineWidth = 1;
      ctx.stroke();
      
      // T-minus indicator
      if (tile.t_minus > 0) {
        ctx.beginPath();
        ctx.arc(x, y, size + 4, 0, (Math.PI * 2 * tile.t_minus) / 255);
        ctx.strokeStyle = '#ff4444';
        ctx.lineWidth = 2;
        ctx.stroke();
      }
    });
    
    // Field boundary
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.strokeRect(10, 10, 780, 580);
    
    // Room name and tick
    ctx.fillStyle = '#ffd700';
    ctx.font = '14px monospace';
    ctx.fillText(`⚔️ ${room.name} — tick ${room.tick}`, 15, 25);
    ctx.fillStyle = '#666';
    ctx.fillText(`${room.tiles.length} tiles in field`, 15, 45);
  }
  
  onTick(room: PlatoRoom): void {
    // Game-specific tick handling: check for combat events
    room.tiles.forEach(tile => {
      if (tile.t_minus === 0 && tile.confidence > 200) {
        console.log(`⚔️ Combat event: ${tile.payload}`);
      }
    });
  }
}

// ── Mode 2: Dashboard Renderer ─────────────────────────────────────

class DashboardRenderer implements Renderer {
  private container!: HTMLElement;
  
  render(room: PlatoRoom, container: HTMLElement): void {
    this.container = container;
    container.innerHTML = '';
    container.style.background = '#0a0a1a';
    container.style.color = '#e0e0e0';
    container.style.fontFamily = 'system-ui';
    container.style.padding = '20px';
    
    // Title
    const title = document.createElement('h1');
    title.textContent = `📊 ${room.name}`;
    title.style.color = '#ffd700';
    title.style.marginBottom = '20px';
    container.appendChild(title);
    
    // Gauges grid
    const grid = document.createElement('div');
    grid.style.display = 'grid';
    grid.style.gridTemplateColumns = 'repeat(auto-fill, minmax(200px, 1fr))';
    grid.style.gap = '16px';
    container.appendChild(grid);
    
    room.tiles.forEach((tile, i) => {
      const gauge = document.createElement('div');
      gauge.style.background = '#1a1a3a';
      gauge.style.borderRadius = '8px';
      gauge.style.padding = '16px';
      gauge.style.border = '1px solid #333';
      
      const value = ((tile.embedding[0] + 1) / 2 * 100).toFixed(1);
      const label = `sensor_${i}`;
      
      gauge.innerHTML = `
        <div style="color:#888;font-size:0.8em;margin-bottom:4px">${label}</div>
        <div style="font-size:2em;font-weight:bold;color:#44ff44">${value}</div>
        <div style="margin-top:8px;background:#333;height:6px;border-radius:3px;overflow:hidden">
          <div style="width:${value}%;background:#44ff44;height:100%;border-radius:3px"></div>
        </div>
        <div style="color:#555;font-size:0.7em;margin-top:4px">confidence: ${tile.confidence}/255</div>
      `;
      grid.appendChild(gauge);
    });
  }
  
  onTick(room: PlatoRoom): void {
    // Update gauges on each tick
    this.render(room, this.container);
  }
}

// ── Mode 3: Website Renderer ───────────────────────────────────────

class WebsiteRenderer implements Renderer {
  private container!: HTMLElement;
  
  render(room: PlatoRoom, container: HTMLElement): void {
    this.container = container;
    container.innerHTML = '';
    container.style.background = '#0a0a1a';
    container.style.color = '#e0e0e0';
    container.style.fontFamily = 'system-ui';
    container.style.maxWidth = '800px';
    container.style.margin = 'auto';
    container.style.padding = '20px';
    
    // The PLATO room IS the website content
    const header = document.createElement('header');
    header.style.borderBottom = '1px solid #333';
    header.style.paddingBottom = '16px';
    header.style.marginBottom = '16px';
    header.innerHTML = `<h1 style="color:#ffd700">${room.name}</h1>
      <p style="color:#666">${room.tiles.length} tiles · tick ${room.tick}</p>`;
    container.appendChild(header);
    
    // Tiles render as page sections
    room.tiles.forEach((tile, i) => {
      const section = document.createElement('section');
      section.style.background = '#1a1a3a';
      section.style.borderRadius = '8px';
      section.style.padding = '16px';
      section.style.marginBottom = '12px';
      section.style.border = '1px solid #333';
      
      section.innerHTML = `
        <div style="color:#ffd700;font-weight:bold;margin-bottom:8px">${tile.payload || `Tile ${i}`}</div>
        <div style="color:#888;font-size:0.85em">
          embedding: [${tile.embedding.map(v => v.toFixed(2)).join(', ')}]
        </div>
        <div style="color:#555;font-size:0.75em;margin-top:4px">
          confidence ${tile.confidence}/255 · T-${tile.t_minus}
        </div>
      `;
      container.appendChild(section);
    });
    
    // Footer
    const footer = document.createElement('footer');
    footer.style.borderTop = '1px solid #333';
    footer.style.paddingTop = '16px';
    footer.style.marginTop = '16px';
    footer.style.color = '#444';
    footer.style.textAlign = 'center';
    footer.style.fontSize = '0.8em';
    footer.textContent = '🦐 Cocapn fleet · lighthouse keeper architecture';
    container.appendChild(footer);
  }
  
  onTick(room: PlatoRoom): void {
    // Re-render page on significant changes (not every tick)
    if (room.tick % 10 === 0) {
      this.render(room, this.container);
    }
  }
}

// ── Factory ─────────────────────────────────────────────────────────

function createRenderer(mode: RenderMode): Renderer {
  switch (mode) {
    case 'game': return new GameRenderer();
    case 'dashboard': return new DashboardRenderer();
    case 'website': return new WebsiteRenderer();
  }
}

// ── Demo ────────────────────────────────────────────────────────────

async function demo() {
  const client = new PlatoClient('http://localhost:8847');
  const modes: RenderMode[] = ['game', 'dashboard', 'website'];
  
  modes.forEach(mode => {
    const renderer = createRenderer(mode);
    const container = document.createElement('div');
    container.id = `plato-${mode}`;
    document.body.appendChild(container);
    
    // Subscribe to room updates
    setInterval(async () => {
      try {
        const room = await client.joinRoom('forge');
        renderer.render(room, container);
        renderer.onTick(room);
      } catch (e) {
        console.log(`Waiting for PLATO...`);
      }
    }, 1000);
  });
}

// Export for bundling
export { PlatoClient, createRenderer, GameRenderer, DashboardRenderer, WebsiteRenderer };
export type { PlatoTile, PlatoRoom, RenderMode };
