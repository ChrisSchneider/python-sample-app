import streamlit as st
from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    HumanMessage,
    SystemMessage,
    AIMessage,
    TextGenerationParameters,
)

# Init session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant. Be short and precise."),
    ]
if "client" not in st.session_state:
    st.session_state.client = Client(credentials=Credentials.from_env())

# Header
st.subheader("Smart Assistant")

# Message list
for msg in st.session_state.messages:
    if msg.role != "system":
        with st.chat_message(msg.role):
            st.markdown(msg.content)

# Chat input
if prompt := st.chat_input("Your question"):
    # Add user message:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))
    
    # Add reply
    response = st.session_state.client.text.chat.create(
        model_id="ibm/granite-13b-chat-v2",
        messages=st.session_state.messages
    )
    reply = response.results[0].generated_text
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append(AIMessage(content=reply))
