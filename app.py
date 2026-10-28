from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

# Demonstration data only: these are simulated cloud servers, not live cloud metrics.
SERVERS = [
    {"name": "web-server-01", "cpu": 22, "memory": 38, "status": "Running"},
    {"name": "api-server-01", "cpu": 76, "memory": 71, "status": "Running"},
    {"name": "worker-server-01", "cpu": 12, "memory": 24, "status": "Running"},
    {"name": "database-01", "cpu": 64, "memory": 82, "status": "Running"},
    {"name": "test-server-01", "cpu": 8, "memory": 17, "status": "Running"},
]

def analyze_servers(servers):
    """Calculate illustrative energy estimates and optimization recommendations."""
    results = []
    total_estimated_kwh = 0.0

    for server in servers:
        # Simplified educational estimate: 0.08 kWh baseline + CPU-based component.
        estimated_kwh = round(0.08 + (server["cpu"] / 100) * 0.22, 3)
        total_estimated_kwh += estimated_kwh

        if server["cpu"] < 20 and server["memory"] < 35:
            recommendation = "Consider consolidating this lightly used workload."
            level = "high"
        elif server["cpu"] > 85 or server["memory"] > 90:
            recommendation = "Review capacity; this server may need more resources."
            level = "warning"
        else:
            recommendation = "Resource usage is within the demo's normal range."
            level = "normal"

        results.append({
            **server,
            "estimated_kwh": estimated_kwh,
            "recommendation": recommendation,
            "level": level,
        })

    avg_cpu = round(sum(s["cpu"] for s in servers) / len(servers)) if servers else 0
    avg_memory = round(sum(s["memory"] for s in servers) / len(servers)) if servers else 0

    # Illustrative estimate only, not a measured or guaranteed saving.
    underused = sum(1 for s in servers if s["cpu"] < 20 and s["memory"] < 35)
    potential_saving = round(underused * 0.04, 3)

    return results, avg_cpu, avg_memory, round(total_estimated_kwh, 3), potential_saving

@app.route("/")
def index():
    servers, avg_cpu, avg_memory, energy, potential_saving = analyze_servers(SERVERS)
    return render_template(
        "index.html",
        servers=servers,
        avg_cpu=avg_cpu,
        avg_memory=avg_memory,
        energy=energy,
        potential_saving=potential_saving,
        updated_at=datetime.now().strftime("%d %b %Y, %I:%M %p"),
    )

@app.route("/simulate", methods=["POST"])
def simulate():
    # Create a fresh, random demonstration snapshot for classroom presentation.
    for server in SERVERS:
        server["cpu"] = random.randint(5, 95)
        server["memory"] = random.randint(10, 95)
    return index()

if __name__ == "__main__":
    app.run(debug=True)
