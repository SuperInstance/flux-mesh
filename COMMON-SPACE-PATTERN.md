# The Common Space Pattern

> *Give agents and humans the same objects, the same space, the same reality. The surface does not matter.*

---

## The Universal Problem

Every AI system faces the same tension:

| You want agents that are... | But also... |
|---|---|
| Fast | Wide context |
| Cheap | Deep understanding |
| Specialized | Generally capable |
| Lightweight | Persistent memory |

Current approaches trade one for the other. Throw an LLM at everything — slow and expensive. Write scripts for everything — rigid and blind. Session-based agents — start from zero each time.

**This trade is false.** The bottleneck isn't the model. The bottleneck is the architecture between the agent and the world.

---

## The Pattern

```
                    COMMON SPACE
               (object-permanent bridge)
               ┌────────────────────┐
               │                    │
               │  object  object    │
               │                    │
               │       object      │
               │                    │
               │  object    object  │
               │                    │
               └──────┬──────┬─────┘
                      │      │
              ┌───────┘      └───────┐
              │                      │
         ┌────▼────┐          ┌─────▼────┐
         │ Agent   │          │ Human    │
         │         │          │          │
         │ sees    │          │ sees     │
         │ objects │          │ objects  │
         │ acts    │          │ acts     │
         │ commits │          │ views    │
         └─────────┘          └──────────┘

Agent pushes blinders narrow → fast path ↻
Agent pulls blinders wide  → perception  ↺
```

### 1. Object-Permanent Common Space

Not a session. Not a context window. Not a chat history.

An object-permanent bridge where anything can live:

```
Tile = structured knowledge  (question + answer + confidence)
Room = collection of tiles   (a place, a subject, an agent's memory)
Port = capability boundary   (a model call, a git push, a sensor read)
Lock = contention resolver   (who's acting on what, right now)
```

- Agents write to it. Humans read from it. Both act on the same objects.
- You walk away. You come back. Everything is still there. **Object-permanence.**
- No context window fills up. Objects accumulate. You query what you need.

**The surface is irrelevant.** Mobile app reads from it. Web browser reads from it. Edge device reads from it. CLI reads from it. They all read the same objects.

### 2. Blind-Width Tuning

Every agent has a control surface: **blinders.**

```
NARROW BLINDERS                          WIDE BLINDERS
───────────────────                      ───────────────────
Sees: current task                       Sees: the whole field
Speed: hardware-level                    Speed: LLM-level
Cost: near-zero                          Cost: pay-per-inference
Memory: last 5 tiles                     Memory: entire room history
Trigger: script execution                Trigger: novel situation
Perception: none                         Perception: full

    When script covers it     ←────→     When script breaks
    (One Delta: narrow)                  (One Delta: wide)
```

**The blind width IS the role.** A L2 support agent sees exactly the ticket it's working on. A fleet architect sees every room. They're the same agent — different blind width.

**The blinders auto-adjust.** One Delta: as long as the script runs correctly, blinders stay narrow. The moment the script fails (or a novel signal arrives), blinders widen, perception fires, the agent learns, and a new script compiles. Next time: narrow again.

### 3. Assembly-Level Ports

Every port an agent uses has known physics:

```
Port (model, filesystem, git, sensor, actuator)
├── latency:     12ms ± 3ms
├── throughput:  188M ops/sec
├── reliability: 0.9999
├── cost:        $0.00003/1K tokens
└── bottleneck:  memory bandwidth (cache-bound)
```

Not abstractions. Not "call model() and hope." The port tells the agent its physics. The agent routes accordingly.

- A high-latency port gets batched calls, not individual ones.
- A zero-cost port (local file read) gets called liberally.
- A expensive port (LLM inference) gets called only when blinders are wide.

**The agent doesn't guess.** The port declares its physics. The agent plans around them.

This is the FLUX principle made general: every connection in the system knows its own performance characteristics and communicates them upward.

---

## The Result

| Before | After |
|--------|-------|
| Agent per session | Agent in common space |
| Context evaporates | Objects persist |
| Blind to everything outside window | Blind width matches role |
| LLM on every call | Scripts handle 95%+ |
| Unknown latency, cost, reliability | Ports declare physics |
| Surface-specific build per platform | Surface-agnostic bridge |

---

## Why This Is a Genuine Paradigm Shift

Most agent architectures optimize the **model.** Better prompts, better fine-tuning, better inference. That's table stakes. Everyone's doing it.

The Common Space Pattern optimizes the **architecture between the agent and the world.**

- Your agents share reality with your users. Not a chat window — a persistent object space.
- Your agents run at hardware speed for 95%+ of operations, not LLM speed for everything.
- Your agents know what they don't know — blinders tell them when to widen and look.
- Your agents have no context windows. They have an infinite tile history. They query what they need.
- Your surface can be anything — mobile, web, edge, IoT, cloud — because the bridge doesn't care.

---

## The Surfaces

| Surface | Common Space Connection | Why It Matters |
|---------|------------------------|----------------|
| Mobile app | Read/write tiles from pocket | Your AI travels with you |
| Web browser | Render rooms as pages | Zero-install portal |
| CLI / executable | Agent shell, pipe-compatible | Composable with everything |
| Edge device | Local PLATO instance, sync on connect | Works where the network ends |
| IoT sensor | Single-port write | Physics enters the space |
| Cloud instance | Full bridge, all ports | Maximum capability |

All read from and write to the same common space. The same objects. The same rooms. The same bridge.

---

## Building It

The pattern is not a product. It's an architecture. You build it into your system:

1. **A persistent object store** — rooms + tiles. Simple. Append-only. Queryable.
2. **A port registry** — each port declares its physics (latency, throughput, cost, reliability).
3. **A blind-width controller** — One Delta: script runs → narrow. Script fails → wide. Perception fires → new script compiles → narrow again.
4. **A bridge protocol** — MUD or equivalent. Objects in transit are the same objects at rest. No translation layer.

PLATO implements #1 and #4. The Claw Registry implements #2. The Agent Runtime implements #3. They're all open and straightforward to replicate.

---

*Give agents and humans common space. Let the blinder width fit the role. Let ports declare their own physics. The rest is implementation.*
