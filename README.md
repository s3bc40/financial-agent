# 🤖 Financial Report Insight Agent (WIP)

## 📊 Project Overview

This is a Work-In-Progress (WIP) project showcasing my exploration into **AI Agent Implementation**. The goal is to build a robust, scalable microservice featuring a multi-step, autonomous AI Agent capable of complex reasoning and financial analysis.

**The Financial Agent** is designed to:

1.  **Retrieve Data:** Sequentially call internal tools to fetch financial metrics (Revenue, COGS, OpEx) for multiple quarters.
2.  **Analyze & Reason:** Calculate Gross Margin and Operating Margin internally.
3.  **Act Conditionally:** Based on the calculated data, it conditionally decides whether to execute a cost-cutting action (only if a margin drop is detected).

### Status: Backend Integration (Day 1 Complete)

The core agent logic has been developed and successfully validated. We are currently in the process of exposing this logic via a production-ready API.

- ✅ **Agent Logic (ADK):** Complete and validated (Validation 3 Passed).
- ✅ **Tools (Mock Data):** Complete and unit-tested (Validation 2 Passed).
- 🟡 **API Wrapper (FastAPI):** Currently implementing **Step 4** (Integration).
- ⚪ **Frontend (Streamlit):** Pending.
- ⚪ **Deployment (Cloud Run):** Pending.

## 🏗️ Technical Stack & Architecture

This project deliberately uses a decoupled, Python-centric microservice architecture to demonstrate scalability and professional development practices.

| Layer                   | Technology                             | Purpose                                                                                                                                           |
| :---------------------- | :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Agent Logic (Brain)** | **Google Agent Development Kit (ADK)** | Handles the LLM interaction, tool orchestration, Reasoning and Action (ReAct) logic, and session management.                                      |
| **API / Service Layer** | **FastAPI**                            | Provides a high-performance, asynchronous REST API (`/query`) to serve the agent's functionality. Essential for decoupling the agent from the UI. |
| **Tooling & Data**      | **Pure Python Mocks**                  | Mocked internal API calls (`tools.py`) to simulate interactions with financial databases.                                                         |
| **Project Management**  | **uv**                                 | Used for ultra-fast dependency resolution and environment management.                                                                             |
| **Testing**             | **Pytest**                             | Ensures the reliability and integrity of the core tool logic.                                                                                     |
| **UI (Planned)**        | **Streamlit**                          | A fast, Python-only framework to build a user-friendly chat interface that consumes the FastAPI service.                                          |

## 📁 Project Structure

```bash
.
├── agents
│   ├── financial_agent
│   │   ├── agent.py
│   │   ├── __init__.py
│   │   └── tools.py
│   ├── __init__.py
├── api
│   └── __init__.py
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── tests
│   ├── __init__.py
│   └── test_financial_agent_tools.py
├── ui
└── uv.lock
```

## 🧠 Key Development Decisions (The Trace)

The agent's success is proven by its ability to execute complex, conditional logic.

- **Tools Validation (✅ Passed):** Unit tests confirmed reliable data from mock tools.
- **ADK Logic Validation (✅ Passed):** The ADK Web UI Trace confirmed a successful 4-step chain: **Data Fetch (2x) → Calculate/Reason → Conditional Action (Skip or Call)**.

## 💻 Get Started Locally

### Prerequisites

1.  Python 3.10+
2.  Your Gemini API Key (set as `GOOGLE_API_KEY` in your `agents/financial_agent/.env` file).

### Setup

```bash
# Clone the repository
git clone https://github.com/s3bc40/financial-agent.git
cd financial-agent

# Install dependencies using uv
uv sync
```

### Running the Agent (Validation)

To see the agent's logic in action (requires a running Gemini API key):

```bash

# Navigate to the agents package root
cd agents
# Run the ADK web UI to interact and see the trace
uv run adk web
```
