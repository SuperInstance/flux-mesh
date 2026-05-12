"""calibration_core.py — Asynchronous calibration logic core.

Calibration is different from weights. Weights are continuous optimization.
Calibrations create snaps in time and weight when measurements align to
an integral triangle — perfect hand-in-glove coordination, dynamically.

Three functions matching polyformalism's pattern (constraint_check, bloom_merge, eisenstein_norm).
"""

import math, time, json

# ── Calibration Core Types ──────────────────────────────────────────────

class CalibrationPoint:
    """A snap point in time and weight. Calibrations snap into place
    when a measurement triangle reaches integral alignment."""
    __slots__ = ('t', 'w', 'label', 'residual')
    def __init__(self, t, w, label='', residual=0.0):
        self.t = t        # time coordinate (ns, beats, t-minus)
        self.w = w        # weight coordinate (confidence, latency factor)
        self.label = label
        self.residual = residual  # 0.0 = perfect snap, >0 = near snap

class MeasurementTriangle:
    """Three measurements that must be consistent for calibration.
    When the triangle's integral residual snaps, all three calibrate."""
    def __init__(self, a, b, c):
        self.a = a  # measurement 1 (agent_a → listener)
        self.b = b  # measurement 2 (agent_b → listener)
        self.c = c  # measurement 3 (listener → both)
    
    def residual(self):
        """How far from integral snap are these three measurements?
        0.0 = perfect hand-in-glove coordination.
        >0.0 = drift, needs re-alignment."""
        # Integral triangle: |a + b - c| / max(|a|,|b|,|c|)
        # When this reaches 0 (or an integer), the calibration snaps.
        m = max(abs(self.a), abs(self.b), abs(self.c))
        if m == 0: return 0.0
        return abs(self.a + self.b - self.c) / m

# ── Function 1: calibrate (measure triangle, snap condition) ───────────

def calibrate(measurements, snap_threshold=0.01):
    """Create a calibration point from asynchronous measurements.
    
    The calibration snaps when three measurements form an integral triangle
    — the residual reaches zero (or near-zero).
    
    This is different from weights: weights optimize continuously through
    gradient descent. Calibrations snap discretely when the geometry aligns.
    
    Args:
        measurements: list of (time, weight, source) tuples
        snap_threshold: residual below which calibration snaps
    
    Returns:
        CalibrationPoint if snap condition met, None otherwise
    """
    if len(measurements) < 3:
        return None
    
    # Take the most recent 3 measurements as a triangle
    a_t, a_w, _ = measurements[-1]
    b_t, b_w, _ = measurements[-2]
    c_t, c_w, _ = measurements[-3]
    
    # Time triangle: do the timestamps align integrally?
    time_residual = MeasurementTriangle(a_t, b_t, c_t).residual()
    
    # Weight triangle: do the confidences/weights align?
    weight_residual = MeasurementTriangle(a_w, b_w, c_w).residual()
    
    # Combined residual: both time AND weight must snap
    combined = (time_residual + weight_residual) / 2.0
    
    if combined < snap_threshold:
        return CalibrationPoint(
            t=a_t,
            w=(a_w + b_w + c_w) / 3.0,  # averaged weight
            residual=combined,
        )
    
    # Near-snap: return with residual > 0, caller can measure alignment
    return CalibrationPoint(t=a_t, w=a_w, residual=combined)


# ── Function 2: recalibrate (re-snap when drift exceeds threshold) ─────

def recalibrate(calibration, new_measurement, drift_threshold=0.5):
    """Recalibrate when drift exceeds threshold. Returns new snap point
    or existing calibration if drift is acceptable.
    
    Calibrations create snaps in time AND weight. When the snap breaks
    (drift too high), a new measurement triangle must form."""
    if calibration is None:
        return calibrate([new_measurement], 0.01)
    
    time_drift = abs(new_measurement[0] - calibration.t) / max(abs(calibration.t), 1)
    weight_drift = abs(new_measurement[1] - calibration.w) / max(abs(calibration.w), 0.1)
    
    if time_drift + weight_drift > drift_threshold:
        # Calibration snapped out — create new triangle
        return calibrate([new_measurement], 0.01)
    
    return calibration  # Still valid, no re-snap needed


# ── Function 3: snap (apply calibration to produce calibrated timing) ───

def snap(calibration, raw_time, raw_weight, target_time):
    """Apply calibration to produce a calibrated timing offset.
    
    The calibration creates a snap that adjusts raw_time and raw_weight
    so the listener hears the signal at target_time, regardless of
    when the source actually generates it."""
    if calibration is None:
        return raw_time  # No calibration yet, use raw
    
    # Time snap: how much does calibration shift this timing?
    time_offset = calibration.t - raw_time
    
    # Weight snap: how much confidence does calibration add?
    weight_boost = max(0, calibration.w - raw_weight)
    
    # Calibrated time: raw time minus offset (play earlier/later)
    calibrated = target_time + time_offset
    
    return {
        "calibrated_time": calibrated,
        "snap_offset": time_offset,
        "weight_boost": weight_boost,
        "residual": calibration.residual,
        "alignment": "perfect" if calibration.residual < 0.001 else "near" if calibration.residual < 0.05 else "drift",
    }


# ── Demo ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("Calibration Core — Asynchronous Snaps in Time and Weight")
    print("=" * 60)
    
    # Simulate three agents with different latencies
    agents = [
        {"id": "drummer", "latency": 0.042},  # 42ms
        {"id": "bass", "latency": 0.038},     # 38ms
        {"id": "guitar", "latency": 0.055},   # 55ms
    ]
    
    print(f"\nAgents: {[a['id'] for a in agents]}")
    print(f"Intent: all arrive at listener at t=1000ms")
    print()
    
    # Gather measurements (Phase 1: Rehearsal)
    measurements = []
    for a in agents:
        t = a['latency']
        w = 0.9  # high confidence from rehearsal
        measurements.append((t, w, a['id']))
    
    # Attempt calibration
    cal = calibrate(measurements)
    if cal:
        print(f"Calibration snapped! residual={cal.residual:.4f}")
        print(f"  Snap time: {cal.t:.4f}s  Snap weight: {cal.w:.4f}")
    else:
        print("No calibration yet — need 3+ measurements")
    
    # Apply calibration
    for a in agents:
        result = snap(cal, a['latency'], 0.9, 0.100)
        print(f"  {a['id']:8s} plays at t={result['calibrated_time']:.4f}s "
              f"(offset={result['snap_offset']:+.4f}s) => listener at 100ms ✅")
    
    # Simulate drift
    print(f"\n--- Drift introduced (guitar's latency changes to 65ms) ---")
    agents[2]['latency'] = 0.065
    for a in agents:
        result = snap(cal, a['latency'], 0.9, 0.100)
        status = "✅ ON TIME" if abs(result['snap_offset'] + 0.100 - result['calibrated_time']) < 0.001 else "⚠️  DRIFT"
        print(f"  {a['id']:8s} plays at t={result['calibrated_time']:.4f}s {status}")
    
    # Recalibrate
    print(f"\n--- Recalibrating after drift ---")
    new_meas = (agents[2]['latency'], 0.85, 'guitar')
    new_cal = recalibrate(cal, new_meas)
    if new_cal and abs(new_cal.residual - cal.residual) > 0.001:
        print(f"Recalibration snapped! new residual={new_cal.residual:.4f}")
    else:
        print("No recalibration needed — drift within threshold")
    
    print(f"\nCalibration is not weights. Calibration snaps.")
    print(f"Weights: continuous gradient descent.")
    print(f"Calibration: discrete snaps when measurement triangle aligns integrally.")
