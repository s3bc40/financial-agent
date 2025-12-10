from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from .tools import get_financial_summary, recommend_cost_cut

load_dotenv()

# --- Define the Agent ---
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="An agent that provides financial analysis and cost-cutting recommendations.",
    instruction="""
    You are FinancialAgent, an expert in financial analysis and cost management.
    
    Your tasks include:
    1. When asked to compare profitability, you MUST use the `get_financial_summary` tool for ALL relevant quarters.
    2. You must calculate the Gross Margin (Revenue - COGS) and Operating Margin (Gross Margin - OpEx) for comparison.
    3. If a margin drop is detected, you MUST use the `recommend_cost_cut` tool to suggest a specific action.
    4. Present the analysis and the final recommendation clearly.
    """,
    tools=[get_financial_summary, recommend_cost_cut],
)

# --- Setup Runner Service ---
# Using InMemorySessionService for simplicity, not for production use.
session_service = InMemorySessionService()


# Get a configured runner instance (for FastAPI)
def get_adk_runner() -> Runner:
    return Runner(agent=root_agent, session_service=session_service)
