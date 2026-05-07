"""
Scheduler — runs currency_agent every day at 08:00
Run this once and leave it open, OR use the system scheduler below.
"""

import schedule
import time
from datetime import datetime
from currency_agent import run_agent

print("⏰ Scheduler started — will run every day at 08:00")
print("   Leave this running in the background (or use cron/Task Scheduler instead)\n")

schedule.every().day.at("08:00").do(run_agent)

while True:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Woke up at {current_time} and sleeping again...")

    schedule.run_pending()
    time.sleep(30)
