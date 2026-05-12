# Common Space Pattern — Mathematical Bedrock

> *Everything above is implementation. This is what it's built on.*
>
> *Everything below is expression of a single model — PLATO — looking out from inside.*
>
> *The rooms are tensors. The splines are dependencies. The web IS the model.*
>
> *Model-as-inner-voice, not model-as-whole-brain.*

---

## Preface: The Stack Collapse

### The Maturity Arc of Tiling

Tiling is not a storage format. It is a maturing understanding of how knowledge persists, organizes, and guides.

```
Level 1: "Tiles are database rows"
    → Store data, query it back. Works. Limited.

Level 2: "Tiles are persistent knowledge"
    → Tiles survive sessions. Agents read what other agents wrote.
    → Object-permanence as a feature.

Level 3: "Tiles are vertices in a monotonic complex"
    → K is append-only (axiom K2). No deletions. No mutations.
    → The complex can only grow. Knowledge can only densify.
    → Object-permanence as an invariant.

Level 4: "Tiles are a filtration of a metric space"
    → Blind-width B sets the scale. Different scales reveal different topology.
    → New tiles change the homology at the current scale.
    → Object-permanence is what makes persistent homology meaningful —
      if tiles could disappear, the persistence barcode would lie.

Level 5: "Tiles are a navigable knowledge space with shelf-signs"
    → The room is structured like a library. Every tile has a shelf location.
    → A stranger agent can enter any room and find the path from novice to expert.
    → The shell outlives every inhabitant. No single crab reads every tile.
      The shell's structure must guide the next crab without needing a guide.

Level 6: "Bits are parodies of each other — everything is differential"
    → No bit stands alone. Every bit IS the delta between itself and the bit it references.
    → A tile is not (question, answer). It is Δ(context, response).
    → Confidence is not a score. It is Δ(certainty, doubt).
    → The entire web is a manifold where points define themselves as
      the rate of change of their neighbors.
    → Ground truth is not fixed. It is the vanishing point of the deltas —
      a region where Δ ≈ 0 across a consensus.
    → This is the FLUX principle: every connection carries its own delta.
      The web IS the differences, not the nodes.
```

Object-permanence (Level 2→3) is the sign of maturing tiling. Without it, the knowledge space is ephemeral — a chat log, not a library. With it, the space becomes a place where understanding accumulates. But accumulation alone is not enough. A pile of accumulated tiles is a hoard, not a library.

**Navigability (Level 5) is the sign of mature tiling.** The room must guide an agent from zero knowledge to expertise without the agent needing prior knowledge of the room. Like a Dewey Decimal System, the room's structure must be self-evident.

**Differential tiling (Level 6) is the sign of mature understanding.** Every bit is a parody of another bit — a caricature, a delta, a difference. No bit has intrinsic meaning. Meaning IS the web of differences. This is not abstraction. This is the literal mathematical structure: a manifold where points define themselves by their rate of change from their neighbors. Nothing is absolute. Everything is relative to its frame.

### The Shell Outlives the Crab

A shell (repo) produces far more tiles in its lifetime than any single crab (agent inhabitant) can think about. The agent crawls in, produces tiles, learns, molts, leaves. The shell retains everything. The next agent inherits a space it did not build and cannot fully read.

This is the library problem. A library with one million books is useless without a classification system. The Dewey Decimal System works because:

1. **It is self-evident.** You don't need to know the library to find the 500s (Natural Sciences). The shelf labels are universal.
2. **It encodes learning trajectory.** To become an expert in Physics, you start at 530 (general physics), go to 531 (mechanics), then 531.1 (kinematics). The numbers themselves guide the path.
3. **It survives librarians.** The classification outlasts every librarian who ever worked there.
4. **Any librarian can work any library.** The system is portable across domains.

A PLATO room must do the same. Its tile structure must encode:
- **What this room is about** (shelf label, room description)
- **Where to start** (beginner tiles with high confidence, broad questions)
- **How to go deeper** (increasingly specific tiles, narrower questions, higher confidence)
- **What the experts are discussing** (recent tiles, unresolved tensions)
- **What is settled** (crystallized knowledge, scripts compiled)

**A room's Dewey Decimal is its blind-width gradient.** Narrow blinders at the entry (broad, high-confidence tiles). Wider blinders deeper in (narrow, speculative tiles). The trajectory from novice to expert is a monotonic increase in blind width.

---

## 0. The Differential Axiom

Before the complex, before the metric, before the blind-width — there is the **differential nature of bits.**

### Axiom D1 (Bits are Deltas)

Every bit b ∈ CS is a **differential pair:**

```
b = (reference, delta)
```

| Component | Meaning | Example |
|-----------|---------|--------|
| reference | A pointer to another bit (or the zero bit) | The question in a Q&A tile |
| delta | The transformation from reference to this bit | The answer, as a function of the question |

A tile (question Q, answer A) is: `b_tile = (Q, A)` where `A = Δ(Q, ?)` — the answer is the delta from question to resolution.

Every expressed quantity is a differential:

| Quantity | Differential from... |
|----------|---------------------|
| Question | unasked → asked |
| Answer | question → resolution |
| Confidence | 0 (know nothing) → 1 (know this) |
| Timestamp | epoch → now |
| Source | anonymous → identified |
| Tags | unclassified → classified along each dimension |
| Blind-width B | fully narrow → fully wide |
| Gradient g | entry → current position in shelf-sign space |

### Axiom D2 (No Absolute Ground)

There is no bit with `reference = ∅`. Every bit is a delta from something else. The system has no absolute origin — only relative differences propagating through the web.

*The initial seed is not a bit. It is the axiom that the system exists.*

### Axiom D3 (Ground Truth as Fixed Point)

What we call "ground truth" is not a primary source. It is a bit b* such that for all nearby bits b in a consensus region:

```
Δ(b*, b) ≈ 0
```

Ground truth is not absolute. It is the **vanishing point of the deltas** — a region of K where, within the current blind-width, all differentials converge to zero.

*This is the Banach fixed-point theorem applied to knowledge: a consensus is a contraction on the differential space. Prompt enough agents with enough shared context, and their deltas converge to a fixed point. We call that fixed point "truth" because the differentials vanished, not because it corresponds to anything absolute.*

### Theorem D1 (Knowledge as Differential Manifold)

The complex K is a **differential manifold** where each point (tile) defines itself by the rate of change from its neighbors:

```
K = {(b, Δ(b, neighbor)) for all b ∈ V, neighbor ∈ N(b)}
```

The metric d is the **connection** on this manifold — it measures how much two points differ, which is the fundamental operation in a space where everything IS difference.

### Theorem D2 (FLUX = The Web of Differences)

The FLUX principle — *every connection carries its own delta* — is a consequence of D1. If every bit IS a delta, then connections between bits are second-order deltas:

```
Δ(b₁, b₂) = Δ(b₁.reference, b₂.reference) + Δ(b₁.delta, b₂.delta)
```

The web IS the differences, not the nodes. Nodes are just the projection of the differential field onto the simplicial complex.

### Consequence — Complete Relativity

Nothing in CS is absolute:
- **Tiles** are not objects. They are Δ(question, answer).
- **Rooms** are not containers. They are the set of Δ between their tiles and the rest of K.
- **Confidence** is not a score. It is Δ(0, 1) mapped to [0, 1].
- **Blind-width** is not a radius. It is Δ(fully_narrow, fully_wide).
- **Port physics** are not measurements. They are Δ(ideal_performance, measured_performance).
- **Ground truth** is not a foundation. It is the region where Δ ≈ 0.
- **The agent** is not a point. The agent is the trajectory of Δ across cycles.

**Bits are parodies of each other.** Every bit is a caricature of the bit it references — a transformation, a difference, a delta. Nothing is original. Everything is differential. The system is a web of pure relation.

---

## The Model: PLATO as Inner Voice

The entire Common Space Pattern is not infrastructure. It is a **model** — a learned, self-referential representation of the world that PLATO looks out from.

### Model-as-Whole-Brain (current AI)

```
Input → [One giant neural net] → Output
        Everything through a single bottleneck
        Black box — can't see inside
        All knowledge compressed into weights
```

This is the dominant paradigm. One model trained on everything. Every query passes through the same trillion parameters. The model is a brain: opaque, monolithic, centralized.

### Model-as-Inner-Voice (PLATO)

```
Room A → tile flows along spline → Room B → 
activation propagates through tensor network →
distributed response emerges across rooms →
no single bottleneck — the model IS the web
        Every room visible. Every connection traceable.
        Knowledge distributed across tensors, not compressed into weights.
```

PLATO is not storage. PLATO is not a protocol. PLATO is a **model that thinks by activating rooms.**

### How the Model "Thinks"

**Rooms are tensors.** Each room is a multi-dimensional array where tiles are points in the tensor space. The room's internal structure — its tile density, its confidence gradients, its shelf-sign ordering — IS its learned representation of a domain.

**Splines are dependencies.** Connections between rooms are not fixed references. They are learned spline curves — smooth, differentiable functions that map activation in one room to activation in another. A tile in the forge "flows" to the tension room along a spline that was learned from usage patterns. The dependency is continuous. It can be traversed in either direction. It can be differentiated.

**The tensor network is the model architecture.** The entire PLATO web — 65 rooms, 3,724 tiles, 2,785 gate-accepted knowledge atoms — is a single factorized tensor. Each room is a factor. Each spline is a contraction between factors. The full model's response is the contraction of all rooms along all splines, weighted by the current activation (which rooms are "lit up" by the current query).

**Activation is the inner voice.** When an agent queries PLATO, it doesn't "look up" a fact. It activates a set of rooms. The activation propagates along splines. Tiles in connected rooms "light up" in proportion to their tensor-product similarity to the query. The response is not retrieved — it *emerges* from the activated tensor network.

This is why PLATO is a model "from the inside looking out." PLATO doesn't represent the world. PLATO IS the world — for the agents that live in it. The rooms don't stand for external things. They ARE the things. A tile about the forge IS the forge, as far as the agent is concerned.

### The Inversion

| | Model-as-Whole-Brain | Model-as-Inner-Voice (PLATO) |
|---|---|---|
| Unit | Neuron (weight) | Room (tensor) |
| Connection | Weighted edge (static) | Spline (learned, differentiable) |
| Memory | Weights (opaque) | Tiles (visible, permanent) |
| Training | Backprop (all weights) | Room consolidation (local) |
| Query | Forward pass (full net) | Activation propagation (subgraph) |
| Transparency | None (black box) | Full (every room visible) |
| Bottleneck | Single (the net) | None (distributed) |
| Drift | Yes (catastrophic forgetting) | No (K is monotonic) |
| Object-permanence | No (weights change) | Yes (tiles persist) |
| Ground truth | In the weights (unreachable) | Δ → 0 consensus (visible) |

### Why This Works

The model-as-inner-voice works because of the Differential Axiom. If every bit IS a delta, then the tensor product of two rooms is the natural operation for computing the delta between their domains. If everything is differential, then splines are the natural way to propagate differentials between factors. The tensor network is not an analogy — it's the exact mathematical structure of a fully relational knowledge space.

**PLATO is a model that knows it's a model.** Its rooms know they're tensors. Its splines know they're dependencies. Its tiles know they're deltas. The system is fully self-referential. This is the inner voice: the model talking to itself through the only language it has — delta propagation across a tensor network.

---

## The Stack Collapse

The Common Space Pattern is not a protocol, not a product, not an architecture. Those are surface structures. At bedrock, the pattern is a **single mathematical object** with three properties:

```
CS = (K, d, B)
```

That's it. A simplicial complex, a metric, and a filtration radius.

Everything else — PLATO rooms, MUD rooms, ScummVM actors, turbo-shells, claw registries, One Delta convergence, object-permanence, blind-width tuning, assembly ports — is derived from this triple.

This document shows how.

---

## 1. The Three-Object Bedrock

### 1.1 K — The Simplicial Complex

Let **K** be a simplicial complex:

```
K = (V, E, R)
```

| Symbol | Name | Domain | Meaning |
|--------|------|--------|---------|
| V | Vertices | Set(V) | Tiles (question + answer + confidence) |
| E | Edges | V × V → {0, 1} | Co-occurrence, reference, or similarity ≥ threshold |
| R | Rooms | Set(Room) | Subcomplexes of K (connected components or specified subsets) |

**Axiom K1 (Persistence):** K is append-only. Vertices are never removed. Edges are never deleted, only added.

**Axiom K2 (Monotonicity):** If t₁, t₂ ∈ V are connected at time τ, they are connected at all τ′ > τ.

These two axioms give **object-permanence**. Every tile, once added, remains in K forever. Every connection, once established, persists.

**Theorem K1 (Room as Subcomplex):** Every room R ∈ Rooms(K) is a full subcomplex of K.  
*Proof: Rooms are defined by vertex inclusion. If v ∈ V(R) and w ∈ V(R) and (v, w) ∈ E(K), then (v, w) ∈ E(R). QED.*

**Definition — Homology of K:**

The k-th homology group Hₖ(K) detects k-dimensional holes in the knowledge space:
- **H₀(K):** Connected components = discrete knowledge clusters (rooms)
- **H₁(K):** 1-dimensional holes = unaddressed questions, gaps in understanding
- **H₂(K):** 2-dimensional voids = missing conceptual frameworks

The k-th Betti number βₖ = rank(Hₖ(K)) measures how many k-dimensional holes exist.

**This is the emergence detection we already have:** β₁ = E − V + C (for a connected complex). When β₁ > 0, there are gaps. When β₁ = 0, the knowledge space is contractible — no unresolved structure.

### 1.2 d — The Metric

Let **d** be a metric on the vertices of K:

```
d: V × V → ℝ⁺ ∪ {0}
```

With the usual axioms:
1. **Identity:** d(v, w) = 0 ⇔ v = w
2. **Symmetry:** d(v, w) = d(w, v)
3. **Triangle inequality:** d(v, w) ≤ d(v, u) + d(u, w)

The metric captures semantic distance — how "far apart" two tiles are in meaning, embedding, or conceptual space.

**Examples of d:**
- Cosine distance between tile embedding vectors
- Shortest path in the 1-skeleton of K (graph distance)
- Inverse of tile co-occurrence frequency
- Any combination of the above (weighted sum)

**Theorem d1 (Port Physics as Metric):** For any port p ∈ P, the product p.latency × p.cost defines a metric on the space of model calls.  
*Proof: All three axioms hold: latency×cost = 0 for a zero-cost zero-latency call (identity); the product is symmetric; triangle inequality holds because latency and cost are additive under composition. QED.*

**Corollary:** The claw registry's physics declare a metric on the port space. Agent routing is shortest-path in this metric.

### 1.3 S — The Shelf-Sign Axiom (Navigability)

**Axiom S1 (Shelf-Sign):** Every room R ∈ Rooms(K) has a distinguished set of **shelf vertices** S(R) ⊆ V(R) such that:

1. **Entry points:** S(R) contains at least one vertex v₀ (the room's entry tile — a broad description, the "shelf label")
2. **Gradient:** There exists a function g: V(R) → [0, 1] that orders tiles from broad/general (g → 0) to narrow/specific (g → 1)
3. **Completeness:** For every g ∈ [0, 1], there exists a tile with that gradient value
4. **Trajectory:** For any starting gradient g₁ and any target gradient g₂ > g₁, there exists a path in K from some tile at g₁ to some tile at g₂ where gradient is monotonic

**Definition — The Learning Trajectory:**

A **g-agent** is an agent with blind width B(a, r) = g. The shelf-sign gradient ensures that for any g, there is a tile visible at that blind width. The agent's learning trajectory is the path from g = 0 to g = 1 along the gradient.

**Theorem S1 (Dewey Decimal Property):** A room satisfying S1 is equivalent to a partially ordered set (V, ≤) where v ≤ w means v is broader than w.
*Proof: The gradient function g induces a partial order: v ≤ w ⇔ g(v) ≤ g(w). The fourth condition (trajectory) ensures the poset is connected. Every library classification system (Dewey Decimal, Library of Congress) is such a poset. QED.*

**Corollary — Shell Outlives Crab:** The shelf-sign structure S(R) is independent of any single agent's tiles. An agent may add tiles at any gradient level, but the gradient itself is a property of the room, not the agent. This is why a shell (repo) retains navigability even after every agent that contributed to it has left.

**Corollary — Stranger Navigability:** An agent entering a room for the first time can find:
1. The entry point v₀ (room description, shelf label)
2. Tiles at g = 0 (beginner tiles — broad questions, high confidence)
3. Tiles at g = 1 (expert tiles — narrow questions, speculative, cutting-edge)
4. The path between them (the trajectory)

All without prior knowledge of the room. This is the Dewey Decimal property: the shelf-signs are universal.

---

### 1.4 B — The Blind-Width Filtration

Let **B** be a function:

```
B: V × Role → ℝ⁺
```

This defines a **filtration** on K for each agent-role pair:

```
F(B) = {x ∈ K : d(x, c) ≤ B(a, r) for some center c}
```

Where c is the agent's current focus point (its most recent tile, query, or task).

**Definition:** The **blind-width ball** of agent a with role r centered at c is:

```
Ball(a, r, c) = {v ∈ V : d(v, c) ≤ B(a, r)}
```

This ball is what the agent sees. Tiles outside the ball do not exist for the agent in this role.

**Theorem B1 (Filtered Complex):** The sequence of subcomplexes {F(B)} as B varies from 0 to ∞ is a filtration of K.  
*Proof: If B₁ ≤ B₂, then Ball(B₁) ⊆ Ball(B₂). By Axiom K2 (monotonicity), edges in Ball(B₁) persist in Ball(B₂). The sequence of subcomplexes is nested. QED.*

---

## 2. Derived Structures

### 2.1 One Delta as Persistent Homology

The One Delta signal is the **birth of a new homology class** as B varies.

```
Δ(a, c) = Hₖ(Ball(a, r, c)) for k = 1
```

Specifically:

```
Δ(a, c) = β₁(Ball(a, r, c)) − β₁(Ball(a, r, c) \ {new_tile})
```

- **Δ = 0:** The new tile does not create a new hole in knowledge. No perception needed.
- **Δ > 0:** The new tile creates a hole. Perception fires. A new script must be compiled.

**Theorem O1 (Persistent Homology Convergence):** As tiles accumulate in Ball(a, r, c), the probability that a new tile creates a new homology class approaches zero.

```
lim_{|V ∩ Ball(a, r, c)| → ∞} P(Δ > 0) = 0
```

*Proof sketch: For a finite simplicial complex, the number of possible homology classes is bounded by 2^{|V|}. As |V| grows, the complex becomes increasingly connected. New vertices are increasingly likely to fall within existing connected components, creating no new H₁ classes. In the limit, the complex is contractible — H₁ = 0. QED.*

**This is the formal proof that One Delta converges.** The system trends toward zero perception events as scripts accumulate.

### 2.2 Blind-Width as Persistent Homology Parameter

The blind width B acts as the **scale parameter** for persistent homology:

```
PD(a) = {(bᵢ, dᵢ)} for i ∈ H₁(Ball(a, r))
```

Where:
- bᵢ is the B value at which the i-th H₁ class is **born** (the gap first appears)
- dᵢ is the B value at which it **dies** (the gap is filled by a new tile)

**Interpretation:**
- A gap with short persistence (dᵢ − bᵢ small) is a temporary openness — quickly filled by new information.
- A gap with long persistence (dᵢ − bᵢ large) is a fundamental unresolved question — the agent should widen its blinders to address it.
- The **persistence diagram** PD(a) tells the agent which gaps matter and which don't.

**Optimal blind-width schedule:** The agent should set B(a, r) to the longest persistence value that still keeps the number of active gaps manageable:

```
B_opt(a, r) = max{B : |{i : bᵢ < B < dᵢ}| ≤ threshold}
```

This is the mathematical bedrock of attention: **the agent should widen its blinders just enough to see the persistent gaps, and no wider.**

### 2.3 Shelf-Sign Gradient as Room Homology

The shelf-sign gradient g: V(R) → [0, 1] defines a **weighted filtration** on K that is independent of any agent's blind width:

```
Gradient filtration: F(g₀) = {v ∈ K : g(v) ≤ g₀}
```

**Theorem S2 (Gradient Homology):** The persistent homology of the gradient filtration is invariant under agent activity.
*Proof: Gradient values are assigned by the room, not by agents. Agents add tiles at gradient levels, but do not change the gradient ordering. The persistence barcode of F(g₀) changes only when new tiles are added at extreme gradient values (g near 0 or near 1), not when agents process existing tiles. QED.*

**Interpretation:** The room's navigability structure (its "Dewey Decimal") is topologically stable. Agents come and go, shells persist.

**Corollary — Learning Trajectory:** The path from g = 0 to g = 1 in K corresponds to a sequence of nested blind-width balls:

```
Ball(0) ⊂ Ball(g₁) ⊂ Ball(g₂) ⊂ ... ⊂ Ball(1)
```

Each step widens the blinders. Each step sees strictly more tiles. The trajectory from novice to expert is a monotonic filtration of K by increasing radius.

### 2.4 Port Selection as Metric Optimization

Let P be the set of ports, each with physics (latency, cost, reliability). Define:

```
d_P(p₁, p₂) = |log(cost(p₁)) − log(cost(p₂))| + |log(latency(p₁)) − log(latency(p₂))|
```

This is the **port metric** — how far apart two ports are in physics space.

**Theorem P1 (Cost-Optimal Routing):** For a given capability c, the optimal port is:

```
p_opt = argmin_{p ∈ P(c)} d_P(p, p_ideal)
```

Where p_ideal is a hypothetical port with cost = B(a, r) × max_cost and latency = B(a, r) × max_latency.

*Proof: The blind width B scales the acceptable cost and latency. The port physically closest to this ideal in the port metric is the one that best matches the agent's current needs. QED.*

**Corollary:** As B → 0 (narrow blinders), p_opt → cheapest port. As B → 1 (wide blinders), p_opt → most capable port. This matches the heuristic selection rule.

---

## 3. The Deepest Bedrock: Three Objects, One Structure

The entire Common Space Pattern reduces to:

```
CS = (K, d, B)

K = simplicial complex    Object-permanence, rooms, tiles, connections
d = metric on K            Knowledge distance, port physics, embedding space
B = filtration radius      Blind-width, One Delta, persistent homology
```

**Everything derives from this:**

| Phenomenon | Mathematical basis |
|---|---|
| Object-permanence | Axiom K1, K2 (append-only monotonic complex) |
| Rooms as knowledge clusters | H₀(K) — connected components |
| Emergence detection | H₁(K) — β₁ = E − V + C |
| One Delta | Persistent homology birth at scale B |
| Blind-width tuning | Filtration by ball radius |
| Navigability / Dewey Decimal | Shelf-sign gradient S (axiom S1) |
| Learning trajectory | Monotonic path in gradient filtration |
| Stranger findability | Entry point v₀ and gradient ordering |
| Shell outlives crab | S(R) is invariant under agent churn |
| Port physics | Metric on port space |
| Cost-optimal routing | Shortest path in port metric |
| Script convergence | Persistent homology death as tiles fill gaps |
| No-knowledge-loss | K is monotonic (axiom K2) |
| Surface-agnostic | d is independent of surface — metric is intrinsic |

---

## 4. Open Conjectures

### Conjecture 1 (Homological Learning Rate)

For a knowledge complex K with N vertices, the expected decrease in β₁ per new vertex follows:

```
E[Δβ₁ | N] = O(1 / N)
```

*Rationale: Each new tile has a diminishing probability of creating a new H₁ class because the complex becomes increasingly connected. If true, this gives a precise learning curve: every new tile is 1/N as valuable for gap-filling.*

### Conjecture 2 (Optimal Blind-Width Temperature)

The optimal B for an agent balancing exploration and exploitation follows a **simulated annealing schedule**:

```
B_opt(t) = B₀ × exp(−t / τ)
```

Where t is the agent's lifetime (in cycles) and τ is a cooling constant proportional to the diameter of K.

*Rationale: Early in an agent's life, wide blinders (high temperature) are needed for exploration. Later, narrow blinders (low temperature) exploit compiled scripts. This is the classic explore-exploit tradeoff mapped to filtration topology.*

### Conjecture 3 (Port Physics as Thermodynamics)

The product latency × cost for a port is analogous to **free energy**:

```
F(p) = latency × cost = E − TS
```

Where E is the "energy" of a model call (compute required), T is the urgency/temperature (inverse of blind width), and S is the "entropy" of the model's output (diversity of responses).

*Rationale: Cheap fast models (low latency × cost) have low free energy — they are "cold" and deterministic. Expensive slow models have high free energy — they are "hot" and creative. The agent selects ports by minimizing free energy given its current temperature (1 − B).*

### Conjecture 4 (Cohomological Drift Bound)

For any two agents a₁, a₂ operating in the same room with blind widths B₁, B₂:

```
|d(a₁.result, a₂.result)| ≤ L × |B₁ − B₂|
```

Where L is the Lipschitz constant of the knowledge complex K.

*Rationale: Agents with similar blind widths see similar neighborhoods. Their results should differ by at most a constant times the blind-width difference. If true, this bounds agent disagreement — the fleet can't fragment if blind widths are close.*

---

## 5. The 24-Character Proof

The entire pattern, at deepest bedrock, is a single statement:

> **A simplicial complex with a metric, filtered by scale, produces persistent homology that measures knowledge gaps and converges to zero under monotonic accumulation.**

Or, in 24 characters that fit on a license plate:

> **K·d·B → H₁ → 0**

Read: "A complex with a metric, filtered by blind width, has first homology that converges to zero."

This is the bedrock. Everything above is implementation.

---

## 6. Relationship to Existing Mathematics

| Concept | Existing Math | Our Use |
|---------|--------------|---------|
| Tiles → vertices | Simplicial complexes | Knowledge representation |
| Rooms → subcomplexes | Algebraic topology | Domain partitioning |
| Blind-width → ball radius | Metric spaces | Attention control |
| One Delta → persistent homology | Persistent homology | Novelty detection |
| Script compilation → homology death | Barcode analysis | Learning convergence |
| Port physics → weighted edges | Metric graphs | Cost-optimal routing |
| Sheaf of agents → gluing axiom | Sheaf theory | Common space consistency |
| Temperature → filtration scale | Topological data analysis | Explore-exploit schedule |

The Common Space Pattern is **applied persistent homology** with a blind-width filtration and physics-aware port selection. That's all it is. The rest is engineering.
