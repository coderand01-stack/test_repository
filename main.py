import streamlit as st
import ollama 

st.title("Simple Ollama Application")

if "messages" not in st.session_state:
	st.session_state.messages = []


for message in  st.session_state.messages:
	with st.chat_message(message['role']):
		st.markd0own(message['content'])


if input := st.chat_input("Ask me anything!"):
	with st.chat_message("user"):
		st.markdown(input)

	st.session_state.messages.append({'role':'user','content':input})

	with st.chat_message("assistant"):
		response = ollama.chat(
			model="qwen2.5-coder:1.5b",
			messages=st.session_state.messages
		)
		st.markdown(response.content)
		st.session_state.messages.append({'role':'assistant','content':response.content})


