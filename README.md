# Self-Healing Data Warehouse Agent using LangGraph & Snowflake

## Problem Statement

Modern data warehouses suffer from:
	•	corrupt data
	•	delayed manual audits
	•	silent quality failures

This project builds an autonomous AI agent that:
	•	audits warehouse data
	•	detects anomalies
	•	decides repair strategies
	•	heals the data
	•	re-validates automatically

  ## Architecture Overview
  <img width="1101" height="158" alt="Screenshot 2026-01-29 at 8 43 43 PM" src="https://github.com/user-attachments/assets/ff5b2e0e-de1b-4166-ba92-ee51b0f7ed7b" />
  
  ###### Agentic Warehouse Self-Healing Pipeline

## Tools
	•	LangGraph – Agent orchestration & state machine
	•	Snowflake (AWS) – Cloud Data Warehouse
	•	Snowpark Python – Data execution layer
	•	Python 3.13
	•	Faker – Synthetic data corruption

-> LangGraph is used to:

	•	define agents as nodes
	•	share state between agents
	•	control execution flow
	•	enable iterative reasoning loops


-> Execution Flow

	1.	Sentinel audits warehouse data
	2.	Strategist determines repair actions
	3.	Healer executes SQL fixes
	4.	Sentinel re-audits
	5.	Loop continues until clean  

	
## Execution & Results

<img width="1647" height="1000" alt="Screenshot 2026-01-29 at 9 58 23 PM" src="https://github.com/user-attachments/assets/a9ed3b3d-8dbb-48f8-a4d9-67a54f3b509b" />

###### The image below demonstrates a successful end-to-end execution of the Agentic Pipeline. The Sentinel Node queries Snowflake in real-time, identifies 10 records with data quality issues (negative quantities), and updates the global Graph State."


Future Improvements

	•	LLM-powered Strategist
	•	Dynamic anomaly detection
	•	Multi-table healing
	•	Cost-aware Snowflake queries
	•	Alerting & logging  
