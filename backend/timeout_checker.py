import time
from datetime import datetime, timedelta
from database.db import load_requests, save_requests

def check_timeouts():
    requests = load_requests()
    now = datetime.utcnow()
    timeout_duration = timedelta(minutes=2)  # For demo, make it 2 minutes

    updated = False
    for req in requests:
        if req["status"] == "pending":
            created_at = datetime.fromisoformat(req["created_at"])
            if now - created_at > timeout_duration:
                req["status"] = "unresolved"
                updated = True
                print(f"⏱️ Request timed out: {req['question']}")

    if updated:
        save_requests(requests)

if __name__ == "__main__":
    while True:
        check_timeouts()
        time.sleep(60)  # check every 60 seconds
