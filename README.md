# Network Sentinel 🛰️

A Python-based network telemetry tool designed for automated service availability monitoring and incident logging.

## 🛠️ Features
- **Service Monitoring:** Tracks the reachability of critical network targets using ICMP protocols.
- **Automated Logging:** Built-in logic to record real-time status updates into a structured CSV format.
- **Incident Alerting:** Identifies service downtime and triggers system-level notifications for immediate diagnostics.
- **Linux Integration:** Seamlessly executes network-level commands and verifies connectivity across Linux environments.

## 📂 Project Structure
- `sentinel.py`: The primary automation script for network health checks and status probing.
- `network_log.csv`: Structured telemetry file containing historical status records.

## 🚀 Getting Started
1. **Clone the repository:**
   `git clone https://github.com/YOUR_USERNAME/network-sentinel-sre.git`
2. **Navigate to the directory:**
   `cd network-sentinel-sre`
3. **Run the monitor:**
   `python sentinel.py`

## 📊 Sample Output
```text
[2026-03-16 01:05:12] 8.8.8.8: UP
[2026-03-16 01:05:13] github.com: UP
[2026-03-16 01:05:15] aws.amazon.com: UP
System Status: OPERATIONAL ✅

