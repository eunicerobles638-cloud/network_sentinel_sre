import os
import time
import csv
from datetime import datetime

# --- CONFIGURATION ---
TARGETS = ["8.8.8.8", "github.com", "google.com"]
LOG_FILE = "network_log.csv"
CHECK_INTERVAL = 60  # seconds

def check_ping(hostname):
    # -c 1 (1 packet), -W 2 (2 seconds timeout)
    response = os.system(f"ping -c 1 -W 2 {hostname} > /dev/null 2>&1")
    return "UP" if response == 0 else "DOWN"

def init_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Target", "Status"])

def notify_alert(target):
    # Termux-specific notification
    os.system(f'termux-notification --title "NETWORK ALERT" --content "{target} is DOWN!" --priority high')

def start_sentinel():
    init_log()
    print(f"🛰️ Sentinel Active. Monitoring: {', '.join(TARGETS)}")
    
    try:
        while True:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for target in TARGETS:
                status = check_ping(target)
                print(f"[{now}] {target}: {status}")
                
                with open(LOG_FILE, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([now, target, status])
                
                if status == "DOWN":
                    notify_alert(target)
            
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 Sentinel stopped by user.")

if __name__ == "__main__":
    start_sentinel()
