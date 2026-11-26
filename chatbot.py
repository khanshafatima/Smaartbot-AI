
import streamlit as st
import ollama

st.set_page_config(
    page_title="SmartBot AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 SmartBot AI")
st.caption("Your Personal AI Assistant")

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

    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("SmartBot is thinking..."):

            response = ollama.chat(
                model="llama3.2:1b",
                messages=st.session_state.messages
            )

            answer = response["message"]["content"]
            st.write(answer)

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
