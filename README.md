# Network Sentinel 🛰️
A Python tool I made to automatically check if my network and favorite servers are online. It pings multiple targets and logs the results so I can track any downtime.

I built this to practice network automation and logging in a Linux environment.

### Key Features:
* **Connectivity Check:** Uses ICMP pings to verify if Google, GitHub, and DNS servers are reachable.
* **Auto-Logging:** Every check is saved in `network_log.csv` with a timestamp for future debugging.
* **Simple Status:** Gives a quick "OPERATIONAL" or "DEGRADED" report after every run.

### How to use:
1. **Clone the repo:**
   `git clone https://github.com/eunicerobles638-cloud/network-uptime-automation.git`
2. **Go to the folder:**
   `cd network-uptime-automation`
3. **Run the script:**
   `python sentinel.py`

### Sample Output:
```text
--- Network Sentinel Check: 2026-03-24 02:45:10 ---
[UP] 8.8.8.8
[UP] github.com
[UP] google.com

System Status: OPERATIONAL ✅
---------------------------------------------

