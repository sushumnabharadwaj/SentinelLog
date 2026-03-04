# SentinelLog

An automated cloud-native log analysis and security alerting pipeline.



\## 📖 Overview



\## 🏗️ System Architecture



```mermaid

flowchart LR

&nbsp;   subgraph Data Generation

&nbsp;       A\[Mock Web Server] -->|Appends JSON| B(server.log)

&nbsp;       B -->|Reads \& Parses| C\[Ingestion Engine]

&nbsp;   end



&nbsp;   subgraph Docker Infrastructure

&nbsp;       C -->|Bulk Insert API| D\[(Elasticsearch)]

&nbsp;       D --- E\[Kibana Dashboard]

&nbsp;   end



&nbsp;   subgraph Threat Detection

&nbsp;       F\[Security Analyzer] -->|Queries 401 Errors| D

&nbsp;       F -->|Analyzes Frequency| G{Threat Detected?}

&nbsp;       G -->|> 5 Failed Logins| H((🚨 Alert Admin))

&nbsp;   end



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

