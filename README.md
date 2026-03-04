# 🛡️ SentinelLog: Cloud-Native Security Pipeline

An automated cloud-native log analysis and security alerting pipeline.

## 🏗️ System Architecture

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
