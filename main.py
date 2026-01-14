import streamlit as st
import ollama 

st.title("Simple Ollama Application")

if "messages" not in st.session_state:
	st.session_state.messages = []


for message in  st.session_state.messages:
	with st.chat_message(message['role']):
		st.markd0own(message['content'])




