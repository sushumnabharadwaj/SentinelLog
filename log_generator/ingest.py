from elasticsearch import Elasticsearch, helpers
import json

# Connect to your local Elasticsearch container
es = Elasticsearch("http://127.0.0.1:9200")

def read_logs():
    """Reads the local log file and prepares it for Elasticsearch."""
    try:
        with open("server.log", "r") as f:
            for line in f:
                yield {
                    "_index": "sentinel-traffic-logs", # The name of our database table
                    "_source": json.loads(line.strip())
                }
    except FileNotFoundError:
        print("Error: server.log not found. Did you run generate.py first?")
        exit(1)

if __name__ == "__main__":
    print("🔌 Connecting to Elasticsearch...")
    
    # Check if connected
    if es.ping():
        print("✅ Connected successfully! Uploading logs...")
        # Bulk insert the data
        helpers.bulk(es, read_logs())
        print("🚀 All logs successfully ingested into Elasticsearch!")
    else:
        print("❌ Could not connect to Elasticsearch. Is Docker running?")