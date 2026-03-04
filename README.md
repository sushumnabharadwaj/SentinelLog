# SentinelLog

An automated cloud-native log analysis and security alerting pipeline.



\## 📖 Overview



\## 🏗️ System Architecture

```mermaid
flowchart LR
    subgraph Data Generation
        A[Mock Web Server] -->|Appends JSON| B(server.log)
        B -->|Reads & Parses| C[Ingestion Engine]
    end

    subgraph Docker Infrastructure
        C -->|Bulk Insert API| D[(Elasticsearch)]
        D --- E[Kibana Dashboard]
    end

    subgraph Threat Detection
        F[Security Analyzer] -->|Queries 401 Errors| D
        F -->|Analyzes Frequency| G{Threat Detected?}
        G -->|> 5 Failed Logins| H((🚨 Alert Admin))
    end


 subgraph Threat Detection
 F\[Security Analyzer] -->|Queries 401 Errors| D
 F -->|Analyzes Frequency| G{Threat Detected?}
 G -->|> 5 Failed Logins| H((🚨 Alert Admin))
 end

This project simulates a real-world cybersecurity pipeline. It generates mock web server traffic, ingests the logs into an Elasticsearch database in real-time, and uses a custom Python detection engine to identify and flag anomalous behavior (like Brute Force attacks).



\## 🛠️ Tech Stack

\* \*\*Language:\*\* Python (Pandas, Faker)

\* \*\*Infrastructure:\*\* Docker \& Docker Compose

\* \*\*Database \& Visualization:\*\* Elasticsearch \& Kibana



\## 🚀 How to Run Locally



1\. \*\*Clone the repository:\*\*

&nbsp;  `git clone https://github.com/sushumnabharadwaj/SentinelLog.git`

&nbsp;  `cd SentinelLog`



2\. \*\*Start the ELK Stack:\*\*

&nbsp;  `docker-compose up -d`



3\. \*\*Install Dependencies:\*\*

&nbsp;  `python -m venv venv`

&nbsp;  `venv\\Scripts\\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)

&nbsp;  `pip install -r requirements.txt`



4\. \*\*Run the Pipeline:\*\*

&nbsp;  \* Terminal 1: `python log\_generator/generate.py` (Starts the mock server)

&nbsp;  \* Terminal 2: `python log\_generator/ingest.py` (Pushes logs to database)

&nbsp;  \* Terminal 3: `python analyzer/detect.py` (Scans for hackers)

