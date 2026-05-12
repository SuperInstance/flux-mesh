"""plato_render_pipeline.py — Generic PLATO→Any rendering pipeline.
Port → render → evaluate → compile → reuse. Swap the renderer to change output.
Game, dashboard, website, MIDI, IoT signal — same pipeline, different target."""

import json, time, hashlib, math

class Pipeline:
    """Generic rendering pipeline: port PLATO room to any output."""
    
    def __init__(self):
        self.scripts = {}    # step_key -> compiled script
        self.script_hits = 0
        self.ai_calls = 0
        self.steps = {"port": 0, "render": 0, "evaluate": 0}
    
    def _check_script(self, key):
        """Returns compiled script if exists, None if AI needed."""
        if key in self.scripts:
            self.script_hits += 1
            return self.scripts[key]
        self.ai_calls += 1
        return None
    
    def _compile(self, key, script):
        """Store a compiled script for future use. AI not needed next time."""
        self.scripts[key] = script
    
    def port(self, room_data):
        """Step 1: Port PLATO room to abstract game state.
        Universal — same output regardless of render target."""
        script_key = f"port_{room_data.get('room', 'unknown')}"
        cached = self._check_script(script_key)
        if cached: return cached
        
        tiles = room_data.get("tiles", [])
        state = []
        for i, t in enumerate(tiles):
            emb = t.get("embedding", [0]*8)
            state.append({
                "id": t.get("source", f"entity_{i}"),
                "x": (emb[0] + 1) / 2 if len(emb) > 0 else 0.5,
                "y": (emb[1] + 1) / 2 if len(emb) > 1 else 0.5,
                "anim_type": "idle",
                "move_type": "walk",
                "confidence": t.get("confidence", 0.5),
                "energy": abs(emb[6]) / 2 + 0.5 if len(emb) > 6 else 0.5,
                "dialogue": t.get("question", "") or t.get("answer", "")[:100],
                "t_minus": t.get("t_minus", 0),
            })
        
        self._compile(script_key, state)
        return state


# ── Render Targets ───────────────────────────────────────────────────

class GameRenderer:
    """Render game state as HTML5 canvas game."""
    def render(self, state):
        # Already implemented in plato-scummvm.html
        pass

class DashboardRenderer:
    """Render game state as live IoT dashboard."""
    def render(self, state):
        gauges = []
        for entity in state:
            gauges.append({
                "label": entity["id"],
                "value": round(entity["energy"] * 100, 1),
                "confidence": round(entity["confidence"] * 100, 1),
                "status": "nominal" if entity["energy"] > 0.5 else "warning",
            })
        return {"type": "dashboard", "gauges": gauges}

class MidiRenderer:
    """Render game state as FLUX-tensor-MIDI events."""
    def render(self, state):
        notes = []
        for i, entity in enumerate(state):
            anim_val = {"idle":0, "walk":0.25, "talk":0.5, "gesture":0.75, "special":1.0}
            notes.append({
                "channel": i % 16,
                "note": 36 + int(anim_val.get(entity.get("anim_type","idle"),0) * 24),
                "velocity": int(entity["energy"] * 127),
                "t_minus": entity["t_minus"],
            })
        return {"type": "midi", "notes": notes, "tempo": 120}

class WebRenderer:
    """Render game state as PLATO-first website."""
    def render(self, state):
        sections = []
        for entity in state:
            sections.append({
                "title": entity["id"],
                "content": entity["dialogue"][:200],
                "status": "active" if entity["energy"] > 0.5 else "idle",
                "progress": entity["energy"],
            })
        return {"type": "website", "sections": sections}

class IoTControlRenderer:
    """Render game state as IoT device signals."""
    def render(self, state):
        signals = []
        for entity in state:
            signals.append({
                "device": entity["id"],
                "setpoint": entity["x"],
                "current": entity["energy"],
                "action": "actuate" if entity["t_minus"] == 0 else "monitor",
            })
        return {"type": "iot", "signals": signals}


# ── Pipeline runner ──────────────────────────────────────────────────

class PlatoRenderer:
    """Unified PLATO→Any renderer. Works with any PLATO room, any output."""
    
    def __init__(self):
        self.pipeline = Pipeline()
        self.renderers = {
            "game": GameRenderer(),
            "dashboard": DashboardRenderer(),
            "midi": MidiRenderer(),
            "website": WebRenderer(),
            "iot": IoTControlRenderer(),
        }
    
    def render(self, room_data, target="game"):
        state = self.pipeline.port(room_data)
        renderer = self.renderers.get(target)
        if not renderer:
            return {"error": f"Unknown render target: {target}. Use: {list(self.renderers.keys())}"}
        return renderer.render(state)


if __name__ == "__main__":
    print("=" * 65)
    print("Generic PLATO Rendering Pipeline")
    print("=" * 65)
    
    # Simulate a PLATO room
    room = {"room": "forge", "tiles": [
        {"source": "smith", "embedding": [0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.8, 0.0], "confidence": 0.9, "question": "The forge glows with creative energy."},
        {"source": "anvil", "embedding": [0.6, 0.5, 0.5, 0.0, 0.0, 0.0, 0.4, 0.0], "confidence": 0.7, "question": "Strike while the iron is hot."},
        {"source": "bellows", "embedding": [0.8, 0.7, 0.75, 0.33, 0.0, 0.0, 0.9, 0.0], "confidence": 0.5, "t_minus": 30},
    ]}
    
    renderer = PlatoRenderer()
    
    print(f"\n--- All 5 render targets ---")
    for target in ["game", "dashboard", "midi", "website", "iot"]:
        result = renderer.render(room, target)
        print(f"\n  [{target.upper()}]")
        if isinstance(result, dict) and "type" in result:
            print(f"    Type: {result['type']}")
            items = [k for k in result.keys() if k != 'type'][:3]
            for item in items:
                val = result[item]
                if isinstance(val, list):
                    print(f"    {item}: {len(val)} items")
                    for v in val[:2]:
                        print(f"      → {v}")
        else:
            print(f"    {json.dumps(result)[:100]}")
    
    print(f"\n{'='*65}")
    print(f"Pipeline: AI calls={renderer.pipeline.ai_calls} Script hits={renderer.pipeline.script_hits}")
    print(f"One PLATO room. 5 render targets. Same pipeline. Different outputs.")
