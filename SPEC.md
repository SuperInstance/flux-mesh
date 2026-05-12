# Common Space Pattern — Formal Specification

> **Version:** 1.0  
> **Status:** Formal specification  
> **Applies to:** Any agent-human common space architecture

---

## 1. Formal Model

### 1.1 Core Objects

Let a **Common Space** be a 5-tuple:

```
CS = (R, T, P, A, B)
```

| Symbol | Domain | Description |
|--------|--------|-------------|
| R | Set(Room) | All rooms in the space |
| T | Set(Tile) | All tiles across all rooms |
| P | Set(Port) | All registered ports (model calls, exec, etc.) |
| A | Set(Agent) | All agents registered in the space |
| B | Agent × Role → [0, 1] | Blind-width function |

### 1.2 Room

```
Room = {
    name:      String          (unique identifier)
    tiles:     List(Tile)      (ordered, append-only)
    created:   Timestamp
    metadata:  Map(String, Any) (arbitrary key-value)
}
```

**Invariant R1 (Room identity):** `∀r₁, r₂ ∈ R, r₁.name = r₂.name ⇒ r₁ = r₂`

**Invariant R2 (Append-only):** `∀r ∈ R, ∀t ∈ r.tiles, t is never removed or mutated.`  
*Tiles may be soft-deleted by marking confidence = 0, but the tile object is never destroyed.*

### 1.3 Tile

A tile is the fundamental unit of structured knowledge.

```
Tile = {
    id:          String         (globally unique hash)
    room:        String         (owning room)
    question:    String         (the prompt/query)
    answer:      String         (the content/response)
    confidence:  Float [0, 1]   (truthworthiness estimate)
    source:      String         (creating agent or system)
    tags:        List(String)   (classification labels)
    created:     Timestamp
    signature:   String         (cryptographic or content hash)
    metadata:    Map(String, Any)
}
```

**Theorem T1 (Object-permanence):** `∀t ∈ T, ∀s ∈ Sessions, t ∈ read(t.room, s)`
*Proof: By R2, tiles are never removed. Any session reading a room receives all tiles in that room. QED.*

**Theorem T2 (Ordering):** `∀r ∈ R, tiles(r) is totally ordered by created.`  
*Proof: Tiles are appended sequentially. Append preserves total order. QED.*

### 1.4 Port

A port is a capability boundary that an agent reaches through. Every port declares its physics.

```
Port = {
    name:        String
    capability:  Capability      (analytical | creative | reasoning | implement | openclaw)
    provider:    String          (deepinfra | exec | openclaw | subagent)
    model:       String          (model identifier or command)
    physics:     PortPhysics
}
```

```
PortPhysics = {
    latency_ms:      Float       (mean latency in milliseconds)
    latency_std_ms:  Float       (standard deviation)
    cost_per_1k:     Float       (USD per 1,000 tokens/operations)
    reliability:     Float [0,1] (probability of successful call)
    throughput:      Float       (max operations per second)
    bottleneck:      String      (limiting factor description)
}
```

**Invariant P1 (Declared physics):** `∀p ∈ P, p.physics.latency_ms ≥ 0 ∧ p.physics.reliability ∈ [0, 1]`

**Invariant P2 (Capability coverage):** `∀c ∈ Capabilities, ∃p ∈ P such that p.capability = c`  
*Every capability must have at least one port that provides it.*

### 1.5 Agent

```
Agent = {
    name:         String
    room:         String         (the agent's habitat room)
    role:         Role           (current role determines blind width)
    capabilities: List(Capability) (which claws this agent can use)
    cycle:        Int            (number of cycles executed)
    state:        AgentState     (idle | reading | reasoning | writing)
}
```

```
Role = {
    name:         String
    blind_width:  Float [0, 1]  (0 = fully narrow, 1 = fully wide)
    description:  String
}
```

### 1.6 Blind-Width Function

```
B: Agent × Role → [0, 1]
```

**Definition:** `B(a, r) = r.blind_width`

The blind width determines:
- **Context window size:** `context_size = B(a, r) × max_context`
- **Execution speed:** `speed = max_speed × (1 − B(a, r))`
- **Perception trigger threshold:** `threshold = base_threshold × (1 − B(a, r))`
- **Port selection bias:** `bias toward cheaper ports when B → 0, toward more capable ports when B → 1`

**Invariant B1 (Monotonicity):** Let `r_narrow, r_wide ∈ Roles` with `r_narrow.blind_width < r_wide.blind_width`.  
Then `∀a ∈ A, B(a, r_narrow) < B(a, r_wide)`.

**Invariant B2 (One Delta convergence):** As the number of compiled scripts for a given input grows, the blind width for that input approaches 0.

```
∀input ∈ Inputs, lim_{|scripts(input)| → ∞} B(a, role_matching(input)) → 0
```

*Interpretation: The more scripts cover a situation, the narrower the blinders get. Perception fires less. The system converges to hardware speed for known patterns.*

---

## 2. Operational Semantics

### 2.1 Agent Cycle

An agent cycle is a 4-step process:

```
CYCLE(a ∈ A):
  1. READ:    context ← tiles(a.room, limit = f(B(a, a.role)))
  2. REASON:  result ← port(capability_for_role(a.role)).call(prompt(context), a)
  3. WRITE:   tile ← create_tile(a.room, result)
  4. ADAPT:   a.role ← adjust_role(a, context, result)
              a.cycle ← a.cycle + 1
```

**Step 1 — READ:** The agent reads from its habitat room. The number of tiles read is proportional to its blind width.

```
f(B) = floor(B × MAX_TILES) + MIN_TILES
```

**Step 2 — REASON:** The agent selects a port by capability (determined by its role) and calls it with context as prompt.

```
capability_for_role(r) = r.primary_capability
port(c) = {p ∈ P | p.capability = c}
result = port(c).call(system_prompt(a), prompt(context))
```

**Step 3 — WRITE:** The result is formed into a tile and appended to the agent's room.

```
create_tile(room, result) = Tile {
    id: hash(room, question, timestamp),
    room: room,
    question: format_question(a, result),
    answer: result,
    source: a.name,
    confidence: f_confidence(result),
    created: now()
}
```

**Step 4 — ADAPT:** The agent adjusts its role (and therefore blind width) based on what happened.

```
adjust_role(a, context, result):
  if is_novel(result):
    return wider_role(a.role)  // Novelty → widen blinders
  elif is_redundant(result):
    return narrower_role(a.role)  // Repetition → narrow blinders
  else:
    return a.role  // No change
```

### 2.2 One Delta Signal

The One Delta is the single signal that triggers perception:

```
Δ(a, input) = (∃s ∈ scripts(a) : s.handles(input)) ? s.execute(input) : PERCEIVE(a, input)
```

Where:
- `scripts(a)` is the set of compiled scripts an agent has for its current domain
- `PERCEIVE(a, input)` expands to: widen blinders, call LLM, tile result, compile new script

**Theorem O1 (Convergence):** For any recurring input I, after k repetitions where k is finite, Δ(a, I) = s.execute(I) without perception.

*Proof sketch: By the algorithm, the first occurrence of I triggers PERCEIVE, which compiles a new script. The second occurrence of I matches the compiled script. By induction, any recurring input converges to script execution. The number of unique inputs is bounded by the agent's experience, making k finite. QED.*

### 2.3 Port Selection

Port selection follows a cost-optimal strategy given blind width:

```
select_port(a, capability):
  candidates = {p ∈ P | p.capability = capability}
  
  if B(a, a.role) < 0.3:   // Narrow blinders → cheapest
    return argmin_{candidates} p.physics.cost_per_1k
  elif B(a, a.role) < 0.7: // Medium → balanced
    return argmin_{candidates} p.physics.cost_per_1k × p.physics.latency_ms
  else:                     // Wide blinders → most capable
    return argmax_{candidates} p.physics.reliability
```

---

## 3. Invariants (Must Hold at All Times)

| ID | Invariant | Type |
|----|-----------|------|
| R1 | Room names are unique | Safety |
| R2 | Tiles are append-only (never mutated or destroyed) | Safety |
| P1 | Port physics are non-negative, reliability ∈ [0,1] | Safety |
| P2 | Every capability has at least one port | Liveness |
| B1 | Blind width is monotonic with role | Safety |
| B2 | One Delta converges to script execution | Progress |
| T1 | Object-permanence holds across sessions | Safety |
| T2 | Room tiles are totally ordered | Safety |
| O1 | Recurring inputs converge to script-only execution | Progress |
| A1 | Every agent has a unique name and a home room | Safety |
| A2 | Every agent cycle produces exactly one tile | Progress |

---

## 4. Verification

### 4.1 Static Verification (Compiler-Checkable)

The following are enforced by the type system at agent registration:

- `∀a ∈ A, a.room ∈ R` (agent's home room exists)
- `∀a ∈ A, a.capabilities ⊆ capabilities(P)` (agent only uses registered capabilities)
- `∀p ∈ P, p.physics satisfies P1` (port physics are well-formed)

### 4.2 Runtime Verification (Monitorable)

The following are monitored continuously:

- **Tile append rate:** `|T| / hour` — should be steady, not zero
- **One Delta ratio:** `|script_executions| / |perception_calls|` — should trend toward ∞
- **Blind width distribution:** average B across all agents — should converge to 0.2-0.3 for mature systems
- **Port reliability:** actual reliability vs declared — should match within 2σ

### 4.3 Formal Properties

**Property 1 — No Knowledge Loss:** `∀t ∈ T, ∀s₁, s₂ ∈ Sessions, ∃s₁, s₂ such that read(t.room, s₁) = read(t.room, s₂) ∩ read(t.room, s₁)`.  
*Every tile visible in one session is visible in all subsequent sessions.*

**Property 2 — Bounded Perception:** For any agent a with N compiled scripts, the probability that a novel input triggers perception is at most 1 / (N + 1).  
*As scripts accumulate, perception probability approaches zero.*

**Property 3 — Cost Bounded by Role:** For any agent a, the expected cost per cycle is bounded by:
```
E[cost(cycle(a))] ≤ B(a, a.role) × cost_expensive_port + (1 − B(a, a.role)) × cost_cheapest_port
```

---

## 5. Implementation Mapping

| Formal Concept | Implementation |
|---|---|
| Room | PLATO room (e.g., `agent-oracle1`) |
| Tile | PLATO tile (question, answer, confidence, source) |
| Port | ClawPort in ClawRegistry (deepinfra, exec, subagent) |
| PortPhysics | Claw config: cost, latency, reliability, strength |
| Agent | PlatoAgent running as systemd unit |
| Agent Cycle | `run_cycle()`: read → reason → write → adapt |
| Blind Width | Determined by role + capability selection |
| One Delta | Auto-compiled scripts (script_hits vs ai_calls in ScummVM) |
| Common Space | MUD + PLATO (object-permanent bridge) |
| Surface | ScummVM, terrain, mobile, web, CLI, edge |

---

## 6. Limits and Open Questions

1. **Tile volume:** How many tiles before room reads become expensive? Current: `O(n)` scan. Future: indexed queries.
2. **Blind-width oscillation:** If an agent cycles between novelty and familiarity, blinders may oscillate. The fix is a hysteresis threshold: `widen_threshold > narrow_threshold`.
3. **Port physics drift:** Port latency and reliability change over time. Ports should re-declare their physics periodically.
4. **Multi-agent tile conflicts:** Two agents writing to the same room with contradictory answers. Resolution: confidence-weighted consensus or explicit arbitration room.
5. **Formal proof of O1:** The convergence proof sketch needs a full induction. This is a candidate for Coq or TLA+ formalization.
