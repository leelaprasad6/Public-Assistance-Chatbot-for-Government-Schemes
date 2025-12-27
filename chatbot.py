import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from model import vector_store, generate_response

st.set_page_config(page_title="Government Schemes Chatbot", page_icon="🤖")
st.title("Government Schemes Chatbot")
st.write("AI Assistant to answer Government Schemes related queries")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, Ask me anything about government schemes in India!"),
    ]

# User input
user_query = st.chat_input("Type your message here....")
if user_query is not None and user_query != "":
    # Retrieve relevant documents based on the query
    retrieved_docs = vector_store.similarity_search(user_query, k=5)
    # Generate a response using the retrieved documents
    response = generate_response(user_query, retrieved_docs)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))
    
#conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

