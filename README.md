# 🤖 Financial Report Insight Agent

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
│   │   ├── mock_data.py
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
│   └── app.py
└── uv.lock
```

## 🧠 Key Development Decisions (The Trace)

The agent's success is proven by its ability to execute complex, conditional logic.

- **Tools Validation (✅ Passed):** Unit tests confirmed reliable data from mock tools.
- **ADK Logic Validation (✅ Passed):** The ADK Web UI Trace confirmed a successful 4-step chain: **Data Fetch (2x) → Calculate/Reason → Conditional Action (Skip or Call)**.

## 💻 Get Started Locally (Run the Full Stack)

**Prerequisites**

1. Python 3.10+
2. Your Gemini API Key (set as GEMINI_API_KEY in a file named .env in the project root).
3. The uv package manager.

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

### Running the End-to-End Application

You will need **two terminal** windows open:

#### Terminal 1: Start the FastAPI Backend (API Service)

The agent logic runs here and is exposed on port 8000.

```bash
uv run uvicorn main:app --reload
```

#### Terminal 2: Start the Streamlit Frontend (UI)

This starts the chat interface, which connects to the backend API.

```bash
uv run streamlit ui/app.py
```

#### Final Validation Test

1. Open your browser to the Streamlit URL (usually http://localhost:8501).

2. Enter the test prompts step by step:

```
Compare the Operating Margin for Q4-2024 versus Q4-2025. Which year performed better, and what cost-cut action should we take now?

How did our performance in the first half of 2025 (Q1-2025 and Q2-2025) compare to the disastrous second half of 2024 (Q3-2024 and Q4-2024)?

Compare Q2-2025 and Q3-2025 profitability for me.

Analyze the financial results for Q4-2024 in detail, including the Gross Margin and Operating Margin.

Do we have the final numbers for Q1-2026 yet?
```

The agent will execute its full chain of reasoning, use its tools, and return the final, detailed recommendation.
