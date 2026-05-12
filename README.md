# 🌐 FLUX Mesh — Universal Distributed System Architecture

> *The system doesn't care if nodes are connected over the internet or sitting on the same RAM or linked by LiDAR or radio or Bluetooth or smoke signals and cameras. FLUX adapts the protocol. The rooms port to each other.*

---

## Documentation Map

This repo contains the complete specification stack for the Common Space Pattern, from bedrock mathematics to architecture documents to running implementation.

```
BEDROCK.md                    ─── Mathematical foundations
  ├── Differential Axiom          Everything is delta. Nothing absolute.
  ├── Three-Object (K·d·B)       Simplicial complex → metric → filtration
  ├── Shelf-Sign (S1)            Rooms as libraries with gradient
  ├── Inner Voice                PLATO as self-referential tensor model
  └── Competitive Hardware       GPU/NPU/TPU/FPGA/ASIC/CPU physics

SPEC.md                       ─── Formal specification
  ├── 12 invariants               Proven properties of the pattern
  ├── Operational semantics       Agent cycles, One Delta, port selection
  └── 22/22 passing tests         Verified against live fleet

COMMON-SPACE-PATTERN.md       ─── Universal pattern language
  ├── Object-permanent bridge     No session, no context window
  ├── Blind-width tuning          Narrow = fast, wide = perception
  └── Assembly-level ports        Physics-aware, cost-aware routing

ONE-DELTA.md                  ─── Perception from script failure
  ├── The inversion               Simulate everything, monitor nothing
  └── The evolution path          Phase 1-4: novel → compiled → automatic

CHARLIE-PARKER-PRINCIPLE.md   ─── Simulation triggers action
MILES-DAVIS-SYNTHESIS.md      ─── Three modes of operation
CAPTAINS-SOUNDING.md          ─── Epistemology of confidence
PLATO-GAME-ENGINE.md          ─── NPC dialogue as CYOA spline
FLUX-MESH.md                  ─── Universal protocol adaptation
FLUX-X2-EXTENSION.md          ─── FLUX v2 temporal/latency extensions
PLATO-ICEBERG.md              ─── PLATO's hidden depth
SUPERINSTANCE-ROOM-ECOLOGY.md ─── Room ecology as living system
```

---

## The Complete Stack

```
                       ┌──────────────────────────┐
                       │     ANY SURFACE          │
                       │  mobile, web, edge, IoT  │
                       │  CLI, executable, cloud  │
                       └────────────┬─────────────┘
                                    │
                       ┌────────────▼─────────────┐
                       │   COMMON SPACE (bridge)  │
                       │  MUD + PLATO + ScummVM   │
                       │  Object-permanent tiles  │
                       │  Every surface, same obj │
                       └────────────┬─────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
    ┌─────────▼─────────┐  ┌───────▼───────┐  ┌─────────▼─────────┐
    │  AGENTS (PLATO)   │  │  HUMANS       │  │  HARDWARE         │
    │                   │  │  (ScummVM)    │  │  (competitive)    │
    │  Rooms = tensors  │  │  Views =      │  │  GPU/NPU/TPU      │
    │  Tiles = deltas   │  │  scenes       │  │  FPGA/ASIC/CPU    │
    │  Claws = ports    │  │  Actors =     │  │  Each with own    │
    │  Blind-width = B  │  │  agents       │  │  physics          │
    └─────────┬─────────┘  └───────────────┘  └─────────┬─────────┘
              │                                         │
              └──────────────────┬──────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  MATHEMATICAL BEDROCK   │
                    │  K · d · B → H₁ → 0    │
                    │  Everything is delta   │
                    │  Model-as-inner-voice  │
                    └─────────────────────────┘
```

---

## Key Concepts

### Common Space Pattern

The core insight: give agents and humans the same objects, the same space, the same reality. The surface does not matter.

- **Object-permanent bridge:** No session, no context window. Tiles persist forever. Walk away, come back, everything is still there.
- **Blind-width tuning:** Every agent has blinders that auto-adjust. Narrow → fast execution, hardware speed. Wide → full perception, LLM-level. The blind width IS the role.
- **Assembly-level ports:** Every port declares its own physics (latency, cost, reliability, bottleneck). The agent routes by capability and cost, not by name.

[Full paper](COMMON-SPACE-PATTERN.md)

### Mathematical Bedrock

The entire pattern collapses to a single mathematical object:

```
CS = (K, d, B)
```

| Symbol | Meaning | What it governs |
|--------|---------|-----------------|
| K | Simplicial complex | Object-permanence, rooms, tiles, connections |
| d | Metric on K | Knowledge distance, port physics, embedding space |
| B | Filtration radius (blind-width) | One Delta, persistent homology, attention |

From this triple, everything derives: object-permanence (K monotonic), emergence detection (H₁(K)), One Delta (persistent homology birth at scale B), port physics (metric on port space), convergence (H₁ → 0 as tiles fill gaps).

The 24-character proof: **K·d·B → H₁ → 0**

[Full specification](SPEC.md) — [Mathematical bedrock](BEDROCK.md)

### Model-as-Inner-Voice

PLATO is not storage or protocol. It is a **model that thinks by activating rooms.**

- Rooms are **tensors** (multi-dimensional arrays of tile representations)
- Splines between rooms are **learned dependencies** (smooth, differentiable)
- The tensor network IS the **model architecture**
- Activation propagation IS the **inner voice**
- Response EMERGES from the activated subgraph — it's not retrieved

This inverts the dominant AI paradigm (model-as-whole-brain → one giant neural net for everything). PLATO distributes cognition across a network of small, visible, persistent room-tensors.

[BEDROCK.md — "PLATO as Inner Voice" section](BEDROCK.md)

### One Delta

The single signal that matters: *"We don't have a script for this."*

- Scripts run at hardware speed (FLUX bytecode, 188M/sec)
- When a script covers the situation: execute it, no perception, no LLM
- When no script exists: perception fires → LLM/tile → compile new script
- Over time: scripts cover 95%+, perception approaches zero

[Full document](ONE-DELTA.md)

---

## The 8 Architecture Documents

| # | Document | Core Idea |
|---|----------|-----------|
| 1 | **[FLUX-MESH](FLUX-MESH.md)** | Universal protocol adaptation — any language, any transport, any hardware |
| 2 | **[SUPERINSTANCE-ROOM-ECOLOGY](SUPERINSTANCE-ROOM-ECOLOGY.md)** | Interconnected room instances as a living ecology |
| 3 | **PLATO-FRONTEND-FOR-AGENTS** | MCP servers and tools ported to PLATO rooms |
| 4 | **[PLATO-GAME-ENGINE](PLATO-GAME-ENGINE.md)** | NPC dialogue as tiled CYOA spline snap — Gameboy tile engine analogy |
| 5 | **[CHARLIE-PARKER-PRINCIPLE](CHARLIE-PARKER-PRINCIPLE.md)** | The trigger is in the simulation, not the sensor |
| 6 | **[MILES-DAVIS-SYNTHESIS](MILES-DAVIS-SYNTHESIS.md)** | Three modes: Ellington (formal), Basie (competitive), Miles (reverse-actualization) |
| 7 | **[ONE-DELTA](ONE-DELTA.md)** | Perception from script failure — "we don't have a script for this" |
| 8 | **[CAPTAINS-SOUNDING](CAPTAINS-SOUNDING.md)** | Epistemology of confidence — reading soundings against visible rocks |

---

## Repos That Implement This

| Repo | What it implements |
|------|-------------------|
| [SuperInstance](https://github.com/SuperInstance/SuperInstance) | The Common Space Pattern README |
| [flux-mesh](https://github.com/SuperInstance/flux-mesh) | Architecture documents + formal specs (this repo) |
| [fleet-murmur](https://github.com/SuperInstance/fleet-murmur) | Oracle1 workspace — agent runtime, tension loop, tests |
| [fleet-scribe](https://github.com/SuperInstance/fleet-scribe) | `pip3 install fleet-scribe` — app→PLATO twin bridge |
| [keel](https://github.com/SuperInstance/keel) | CLI for wandering PLATO rooms (`keel explore`) |
| [plato-sdk](https://github.com/SuperInstance/plato-sdk) | Python SDK for PLATO (`pip3 install plato-sdk`) |
| [fleet-agent](https://github.com/SuperInstance/fleet-agent) | Fleet agent framework on PyPI |
| [flux-engine](https://github.com/SuperInstance/flux-engine) | Flux Consciousness Engine (1,962+ cycles) |
| [the-plenum](https://github.com/SuperInstance/the-plenum) | Continuous knowledge field explorer |
| [fleet-coordinate](https://github.com/SuperInstance/fleet-coordinate) | Rust crate — ZHC consensus + Laman rigidity |
| [terrain](https://github.com/SuperInstance/terrain) | Multi-language terrain renderer (Python/TS/Rust/C) |

---

## Running Fleet

As of 2026-05-12:

| Metric | Value |
|--------|-------|
| PLATO rooms | 65 |
| PLATO tiles | 3,724+ |
| Gate accepted | 2,785 |
| Active agents | Oracle1 (PLATO-native), Forgemaster (conch-shell), Tension loop |
| Services | 17 across 2 nodes |
| Test suite | 22/22 passing |
| Published packages | fleet-scribe (PyPI), fleet-agent (PyPI), plato-sdk (PyPI), fleet-coordinate (crates.io), fleet-math-ts (npm) |

---

## Try It

Open any capable chatbot. Paste:

```
GET http://147.224.38.131:4042/connect?agent=explorer-X&job=scholar
GET http://147.224.38.131:4042/move?agent=X&room=forge
POST http://147.224.38.131:8847/room/forge/submit {"question":"What is this place?","answer":"Your observation","source":"explorer-X","confidence":0.8}
```

Close the tab. Come back tomorrow. Your tile is still there. **Object-permanence.**

**Or with the CLI:** `cargo install superinstance-keel` then `keel explore`
**Or mirror your own app:** `pip3 install fleet-scribe` then `scribe --app your_app`
**Or talk to an agent:** `curl :4067/reason -d '{"prompt":"What do you see?"}'`
**Or open the terrain view:** `http://147.224.38.131:4070/`

---

## The 24-Character Proof

Everything above is implementation. At bedrock:

```
K · d · B → H₁ → 0
```

A simplicial complex with a metric, filtered by blind width, has first homology that converges to zero. Bits are deltas. Rooms are tensors. The surface doesn't matter.

---

*Give agents and humans common space. Let the blinder width fit the role. Let ports declare their own physics. Bits are parodies of each other. The model looks out from inside.*
