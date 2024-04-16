import streamlit as st

# Init session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        { "role": "system", "content": "You are a helpful assistant. Be short and precise." },
        { "role": "assistant", "content": "Hello, how can I help?" },
    ]

# Header
st.subheader("Smart Assistant")

# Message list
for msg in st.session_state.messages:
    if msg['role'] != "system":
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

# Chat input
if prompt := st.chat_input("Your question"):
    # Add user message:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({ "role": "user", "content": prompt })
    
    # Add reply
    reply = prompt[::-1]
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({ "role": "assistant", "content": reply })
