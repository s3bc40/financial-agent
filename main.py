import asyncio

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from google.genai import types

from agents.financial_agent.agent import get_adk_runner, get_session_service

load_dotenv()


# --- Pydantic Models for Data Validation ---
class QueryRequest(BaseModel):
    prompt: str


class QueryResponse(BaseModel):
    answer: str


# --- FastAPI Application Setup ---
app = FastAPI(
    title="Financial Agent Service",
    description="An API service for handling financial queries using an AI agent.",
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {"status": "OK", "service": "Financial Agent FastAPI"}


@app.post("/query", response_model=QueryResponse)
async def run_agent_query(request: QueryRequest):
    """
    Takes a user prompt, processes it using the financial agent, and returns the answer.

    Args:
        request (QueryRequest): The request body containing the prompt and optional session ID.
    """
    # Generate required IDs for the Runner contract
    temp_user_id = str(uuid4())
    temp_session_id = str(uuid4())

    # Get the session service and runner
    session_service = get_session_service()
    runner = get_adk_runner()

    # 3Ensure the session exists before running the runner
    session = await session_service.get_session(
        app_name="agents", user_id=temp_user_id, session_id=temp_session_id
    )

    if not session:
        await session_service.create_session(
            app_name="agents", user_id=temp_user_id, session_id=temp_session_id
        )

    # Run the agent with the provided prompt
    try:
        message_content = types.Content(
            parts=[types.Part(text=request.prompt)],
            role="user",
        )

        # Execute the agent asynchronously in a separate thread
        events_generator = await asyncio.to_thread(
            runner.run,
            new_message=message_content,
            user_id=temp_user_id,
            session_id=temp_session_id,
        )

        # Collect all events from the generator
        events = list(events_generator)

        # Extract the final answer from event stream
        final_response = "Error: Agent failed to produce a final response."

        # Iterate through events in reverse, looking for the final text response
        for event in reversed(events):
            # Check if the event has a 'content' object
            if hasattr(event, "content") and event.content:
                # Check if the content has parts and the first part has text
                if event.content.parts and hasattr(event.content.parts[0], "text"):
                    final_response = event.content.parts[0].text

                    # Since we are iterating backwards, the first text we find is the final response.
                    break

        return QueryResponse(answer=final_response)

    except Exception as e:
        error_message = f"Agent execution failed. Error: {type(e).__name__} - {e}"
        print(f"ERROR: {error_message}")
        return QueryResponse(answer=error_message)
