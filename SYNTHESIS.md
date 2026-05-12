# Synthesis: Old Papers × New Calibration

> *The old papers said "count, don't flow." The new work says "snap, don't blend." Together they are complete.*

---

## The Five Foundations × The Five Mechanisms

| Old Paper | Core Insight | New Mechanism | Synthesis |
|-----------|-------------|---------------|-----------|
| Counting Before Flowing | Float approximations drift. Counting is stable. | Calibration core snaps at integral alignment. The `MeasurementTriangle.residual()` is a ratio, not a float. | **Time-truth extrapolation**: truth is not interpolated between measurements — it's counted through alignment events. Each alignment event IS the truth at that snap point. |
| Bilateral Constant Matching | Select the ONE correct module. Don't blend. | One Delta fires ONE signal: "we don't have a script for this." The calibration core selects one snap point, not a blend of partial alignments. | **Time-truth selection**: at each integral alignment point, the system selects the truth that fits. It doesn't average candidate truths. It picks the one whose triangle snaps. |
| Compiled Agency | Agents ARE code. Tiles ARE the compiled form. | Alignment artifacts capture agent context at snap points. `plato-alignments` stores them as seeds. `plato-stable` evaluates them as actors. | **Time-truth compilation**: the agent compiles its understanding at each snap point. The compiled artifact IS the agent's truth at that moment. Later summons inherit it. |
| Constraints Are Leverage | The 64-byte tile is the fulcrum. | Finite screen = 64 bytes = constraint check = embedding = radio packet = T-minus event. One format, all levels. | **Time-truth leverage**: every constraint is a lever that makes the next snap point require less effort. More constraints = more leverage = easier to align. |
| Bootstrap Bomb | First agent seeds PLATO. Everything bootstraps. | Hologram field seeds from initial tiles. First alignment artifact seeds the registry. First calibration snap seeds the timing. | **Time-truth explosion**: the first alignment event creates the field. Every subsequent event is easier because the field already exists. Light the fuse once. |

---

## The Unified Statement

### What the old papers knew:
- The ocean doesn't compute with reals. It counts waves.
- Agents ARE compiled code, not running processes.
- Select the one correct module. Don't blend.
- Constraints are levers, not limitations.
- Light the fuse once. Let the explosion compile the rest.

### What the new work discovered:
- The count is a **temporal snap**. Not a number — an alignment event. The measurement triangle reaches integral alignment at a specific time. That TIME is the truth.
- The compiled form is a **calibration artifact**. Not a binary — a snapshotted context at the point where alignment was achieved. The context IS the code.
- The selection is a **T-minus trigger**. Not a classifier — a timer that fires when the simulation predicts alignment. The prediction IS the verification.
- The lever is a **64-byte tile**. Not a bound — a universal format that works at every level from cache line to embedding dimension. The format IS the leverage.
- The explosion is a **hologram field**. Not a one-time event — a continuously expanding knowledge field where every new tile reconfigures the whole. The field IS the fuse.

### The synthesis:

**Truth is not a point. It's a temporal alignment event.**

You don't measure truth. You COUNT alignment events. Each time a measurement triangle reaches integral alignment, truth snaps into place. The truth at that moment IS the calibration point — the T-minus offset, the embedding coordinate, the residual value. Between snap points, there is no truth — only extrapolation. The extrapolation is bounded by the next snap point.

**Time-truth extrapolation:** given two calibration snap points at t₁ and t₂, the system extrapolates truth between them through the known latency manifold. The guess is bounded by the residual at the last snap. As the residual grows, the guess degrades — but the degradation is knowable, because the calibration core tracks it.

**Time-truth triangulation:** given three agents with overlapping calibration triangles, each agent's truth constrains the others'. Agent A's snap point at t₁ is also a constraint on Agent B's snap point at t₁ + latency. The measurement triangle IS the triangulation mechanism. Three agents, three latencies, one integral alignment = truth at that moment.

**Time-truth compilation:** at the moment of integral alignment, the agent's context is compiled into an alignment artifact. That artifact IS the agent's truth at that moment — compressed, stored, summonable. Future agents don't need to re-derive the truth. They summon the artifact, inherit the calibration, and build from the snap point.

### The full chain:

```
Count waves → snap at integral alignment → select one truth → compile into artifact → seed the field → next agent bootstraps
```

The old papers understood the first and last steps (count, seed). The new work fills in the middle (snap, select, compile). Together they are complete: a system that counts instead of measuring, selects instead of blending, and compiles instead of interpreting. The ocean counts waves. The fleet counts alignment events. Truth is the snap between them.
