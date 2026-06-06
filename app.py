import streamlit as st

from chatbot.chain import chain

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Aman Singh Real Estate Assistant",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------

st.title("🏠 Aman Singh Real Estate Assistant")

st.markdown("""
Welcome! 👋

I can help you with:

✅ Buying Properties  
✅ Selling Properties  
✅ Renting Houses, Flats & Shops  
✅ Leasing Residential & Commercial Buildings  
✅ Property Consultation  
✅ Site Visit Assistance  

Simply ask your question below.
""")

# -----------------------------
# Session State
# -----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("Real Estate Assistant")

    st.write(
        "Ask any property-related question and get instant assistance."
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# -----------------------------
# Display Chat History
# -----------------------------

for message in st.session_state.chat_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# -----------------------------
# Chat Input
# -----------------------------

user_query = st.chat_input(
    "Ask about buying, selling, renting, leasing..."
)

if user_query:

    with st.chat_message("user"):
        st.markdown(user_query)

    st.session_state.chat_history.append(
        HumanMessage(content=user_query)
    )

    response = chain.invoke(
        {
            "chat_history": st.session_state.chat_history,
            "user_query": user_query
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )