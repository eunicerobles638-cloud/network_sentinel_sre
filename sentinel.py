#!/usr/bin/env python
import os
import platform
import subprocess
import time
from datetime import datetime

# List of servers to monitor (Standard for DevOps)
TARGETS = ["8.8.8.8", "github.com", "google.com"]
LOG_FILE = "network_log.csv"

def check_ping(hostname):
    # Standard ping command for Linux/macOS
    param = '-c' if platform.system().lower() != 'windows' else '-n'
    command = ['ping', param, '1', hostname]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def run_sentinel():
    print(f"--- Network Sentinel Check: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    
    with open(LOG_FILE, "a") as f:
        all_up = True
        for target in TARGETS:
            status = "UP" if check_ping(target) else "DOWN"
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp}, {target}, {status}\n"
            
            f.write(log_entry)
            print(f"[{status}] {target}")
            
            if status == "DOWN":
                all_up = False
                
        if all_up:
            print("\nSystem Status: OPERATIONAL ✅")
        else:
            print("\nSystem Status: DEGRADED ⚠️")
    print("-" * 45)

if __name__ == "__main__":
    run_sentinel()

