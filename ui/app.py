import json
import requests
import streamlit as st

# --- Configuration ---
FAST_API_URL = "http://127.0.0.1:8000/query"

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="Financial Agent UI",
    page_icon="💰",
    layout="centered",
)
st.title("💰 Financial Agent UI")
st.caption("Powered by Gemini and the ADK via FastAPI")

# --- Initialize Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I am the Financial Analyst Agent. I can compare financial quarters and recommend cost-cutting actions. How can I help?",
        }
    ]


# --- Function to Call the Backend API ---
def get_agent_response(prompt: str):
    """Sends the user prompt to the FastAPI agent endpoint."""

    # Payload for the API request
    payload = {"prompt": prompt}

    try:
        reponse = requests.post(FAST_API_URL, json=payload)
        reponse.raise_for_status()
        data = reponse.json()

        return data.get("answer", "Error: No answer field found in API response.")

    except requests.exceptions.RequestException as e:
        return f"Error communicating with backend: {e}"
    except json.JSONDecodeError:
        return f"Error: Unable to parse JSON response from backend. Response content: {reponse.text}"


# --- Main Chat Loop ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input handling
if prompt := st.chat_input("Ask a question about profitability or cost-cutting..."):
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get the agent's response from the backend
    with st.spinner("Thinking..."):
        agent_response = get_agent_response(prompt)

    # Append agent response to chat history
    with st.chat_message("assistant"):
        st.markdown(agent_response)

    st.session_state.messages.append({"role": "assistant", "content": agent_response})
