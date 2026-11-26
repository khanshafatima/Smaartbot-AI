
import streamlit as st
from ollama import Client

# Page settings
st.set_page_config(
    page_title="SmartBot AI",
    page_icon="🤖",
    layout="centered"
)

# App title
st.title("🤖 SmartBot AI")
st.caption("Your Personal AI Assistant")

# Connect to Ollama Cloud
try:
    api_key = st.secrets["OLLAMA_API_KEY"]

    client = Client(
        host="https://ollama.com",
        headers={
            "Authorization": "Bearer " + api_key
        }
    )

except Exception as e:
    st.error("API key configuration problem.")
    st.stop()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# New Chat button
if st.button("➕ New Chat"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
question = st.chat_input("Ask me anything...")

if question:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("SmartBot is thinking..."):

            try:
                response = client.chat(
                    model="gemma4:31b",
                    messages=st.session_state.messages
                )

                answer = response.message.content

                st.write(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error("AI connection failed.")
                st.code(str(e))
