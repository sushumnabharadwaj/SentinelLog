from elasticsearch import Elasticsearch
import pandas as pd

# Connect to your local database
es = Elasticsearch("http://127.0.0.1:9200")
INDEX_NAME = "sentinel-traffic-logs*"

def fetch_failed_logins():
    """Queries Elasticsearch for all 401 Unauthorized attempts."""
    print("🔍 Scanning database for failed login attempts...")
    
    # Elasticsearch query to find 401 status codes
    query = {
        "query": {
            "match": {
                "status": 401
            }
        },
        "size": 1000  # Grab up to 1000 recent failed attempts
    }

    try:
        # Search the database
        response = es.search(index=INDEX_NAME, body=query)
        hits = response['hits']['hits']
        
        # Extract just the useful data into a list
        logs = [hit['_source'] for hit in hits]
        return logs
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return []

def analyze_threats(logs):
    """Uses Pandas to find IP addresses with too many failed logins."""
    if not logs:
        print("✅ No failed logins found. System is secure.")
        return

    # Load the data into a Pandas DataFrame (like a virtual Excel sheet)
    df = pd.DataFrame(logs)
    
    # Count how many times each IP appears in the failed logins list
    ip_counts = df['ip'].value_counts()
    
    # Set our security threshold (e.g., more than 5 failed attempts is suspicious)
    THRESHOLD = 5
    
    # Filter for IPs that crossed the threshold
    malicious_ips = ip_counts[ip_counts > THRESHOLD]
    
    if malicious_ips.empty:
        print("✅ Normal traffic detected. No brute-force attacks found.")
    else:
        print("\n🚨 THREAT DETECTED: BRUTE FORCE ATTACK 🚨")
        print("===========================================")
        for ip, count in malicious_ips.items():
            print(f"⚠️  BLOCK IP: {ip} -> Attempted {count} failed logins!")
        print("===========================================")

if __name__ == "__main__":
    # Run the pipeline
    if es.ping():
        failed_logs = fetch_failed_logins()
        analyze_threats(failed_logs)
    else:
        print("❌ Could not connect to Elasticsearch. Is Docker running?")