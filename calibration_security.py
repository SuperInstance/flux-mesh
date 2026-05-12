"""calibration_security.py — Security through calibration.
Normal timing = no alarm. Drift = investigation. Missing event = glitch.
Correlated anomalies = higher abstraction needed."""

import math, time, json

class CalibrationSecurity:
    """Reads security signals from calibration residuals.
    No separate monitoring needed — the calibration IS the sensor."""
    
    def __init__(self, drift_threshold=0.5):
        self.agents = {}     # agent_id -> calibration history
        self.alerts = []
        self.alarms = []
        self.glitch_count = 0
    
    def observe(self, agent_id, timestamp, residual):
        """Observe an agent's calibration residual.
        Normal range: 0.0-0.3 (tight calibration)
        Investigation: 0.3-0.7 (possible drift or interference)
        Alarm: >0.7 (likely compromised or malfunctioning)
        Missing: no observation for >2x expected interval"""
        
        now = time.time()
        if agent_id not in self.agents:
            self.agents[agent_id] = {
                "history": [],
                "last_seen": now,
                "status": "normal",
            }
        
        agent = self.agents[agent_id]
        agent["history"].append((now, residual))
        agent["last_seen"] = now
        
        # Diagnostic chain: residual tells the story
        if residual < 0.3:
            agent["status"] = "normal"
        elif residual < 0.7:
            agent["status"] = "investigate"
            self.alerts.append({
                "type": "drift",
                "agent": agent_id,
                "residual": residual,
                "time": now,
                "action": "security agent dispatched to investigate",
            })
        else:
            agent["status"] = "alarm"
            self.alarms.append({
                "type": "anomaly",
                "agent": agent_id,
                "residual": residual,
                "time": now,
                "action": "alarm agent notified — possible compromise",
            })
        
        return agent["status"]
    
    def check_missing(self, agent_id, expected_interval):
        """Check if an agent has gone silent.
        Missing event IS a signal — it means an object is not being perceived."""
        agent = self.agents.get(agent_id)
        if not agent:
            return "unknown"
        
        elapsed = time.time() - agent["last_seen"]
        if elapsed > expected_interval * 2:
            self.alarms.append({
                "type": "missing",
                "agent": agent_id,
                "elapsed": elapsed,
                "expected_interval": expected_interval,
                "time": time.time(),
                "action": "object not being perceived — higher abstraction investigation needed",
            })
            return "glitch"
        
        return "present"
    
    def detect_glitch(self):
        """Correlated anomalies across multiple agents = 'glitch in the matrix'.
        Not a calibration issue. A higher-level phenomenon."""
        recent_alarms = [a for a in self.alarms 
                        if time.time() - a.get("time", 0) < 30]
        
        if len(recent_alarms) >= 2:
            # Two or more agents showing anomalies simultaneously
            # This is not a calibration issue — something systemic
            self.glitch_count += 1
            return {
                "glitch": True,
                "agents": [a["agent"] for a in recent_alarms],
                "count": self.glitch_count,
                "action": "higher abstraction investigation triggered — complete object may not be perceived",
            }
        
        return {"glitch": False}


if __name__ == "__main__":
    print("=" * 65)
    print("Calibration Security — Timing IS the Signal")
    print("=" * 65)
    
    sec = CalibrationSecurity()
    
    # Normal operation: four agents firing within calibration
    print("\nNormal operation — all agents tight:")
    for agent in ["drone_A", "drone_B", "sensor_C", "watchdog_D"]:
        for i in range(5):
            status = sec.observe(agent, time.time(), 0.02 + i * 0.01)
        print(f"  {agent:12s} status={status}")
    
    # Drift: one agent starts deviating
    print("\nDrift detected — security investigation:")
    for i in range(3):
        status = sec.observe("drone_A", time.time(), 0.3 + i * 0.15)
    print(f"  drone_A     status={status} → alert #{len(sec.alerts)}")
    
    # Anomaly: residual spikes
    print("\nAnomaly — alarm triggered:")
    status = sec.observe("drone_A", time.time(), 0.85)
    print(f"  drone_A     status={status} → alarm #{len(sec.alarms)}")
    
    # Missing agent
    print("\nMissing agent — 'glitch in the matrix':")
    # Simulate drone_B going silent (last_seen was set above, so elapsed > 2*interval)
    # Actually set last_seen far back
    if "sensor_C" in sec.agents:
        sec.agents["sensor_C"]["last_seen"] = time.time() - 60
    status = sec.check_missing("sensor_C", 10)
    print(f"  sensor_C    status={status} → alarm #{len(sec.alarms)}")
    
    # Correlated anomalies = glitch
    print("\nCorrelated anomalies — higher abstraction investigation:")
    glitch = sec.detect_glitch()
    if glitch["glitch"]:
        print(f"  GLITCH #{sec.glitch_count}: {glitch['action']}")
        print(f"  Agents involved: {glitch['agents']}")
    
    print(f"\n{'='*65}")
    print(f"Alerts (investigations): {len(sec.alerts)}")
    print(f"Alarms (compromise):     {len(sec.alarms)}")
    print(f"Glitches (systemic):     {sec.glitch_count}")
    print(f"{'='*65}")
    print("Security is a byproduct of calibration. No separate monitoring needed.")
