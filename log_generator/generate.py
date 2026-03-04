import json
import time
import random
from datetime import datetime
from faker import Faker

# Initialize Faker to generate realistic fake data
fake = Faker()

# The file where we will write our fake server logs
LOG_FILE = "server.log"

def generate_normal_log():
    """Simulates normal user traffic on a website."""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": fake.ipv4(),
        "method": random.choice(["GET", "POST", "PUT"]),
        "endpoint": random.choice(["/home", "/login", "/api/data", "/checkout", "/contact"]),
        "status": random.choice([200, 200, 200, 201, 404, 500]), # Weighted to be mostly successful (200)
        "user_agent": fake.user_agent()
    }

def generate_anomaly(malicious_ip):
    """Simulates a failed login attempt (401 Unauthorized)."""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": malicious_ip,
        "method": "POST",
        "endpoint": "/login",
        "status": 401, 
        "user_agent": fake.user_agent()
    }

def main():
    print(f"🚀 Starting mock server. Writing logs to {LOG_FILE}...")
    print("Press Ctrl+C to stop.")
    
    # Open the file in 'append' mode
    with open(LOG_FILE, "a") as f:
        try:
            while True:
                # 5% chance to trigger an anomalous event (Brute Force Attack)
                if random.random() < 0.05:
                    bad_ip = fake.ipv4()
                    print(f"⚠️ INJECTING ANOMALY: Brute force attack from {bad_ip}")
                    
                    # Generate 10-20 rapid failed login attempts from the same IP
                    for _ in range(random.randint(10, 20)): 
                        log = generate_anomaly(bad_ip)
                        f.write(json.dumps(log) + "\n")
                        f.flush() # Force write to file immediately
                        time.sleep(0.05) # Very fast requests
                else:
                    # Normal traffic
                    log = generate_normal_log()
                    f.write(json.dumps(log) + "\n")
                    f.flush()
                
                # Wait a random amount of time between 0.5 and 2 seconds before the next normal request
                time.sleep(random.uniform(0.5, 2.0))
                
        except KeyboardInterrupt:
            print("\n🛑 Log generation stopped by user.")

if __name__ == "__main__":
    main()