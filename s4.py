import streamlit as st
from generateNextQuestion_s4 import GlobalQuestionManager
from llm_s4 import return_llm_feedback

st.title("Reflective Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

#make a global object 
question_manager = GlobalQuestionManager()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Correct f-string with proper newlines and function calls
    # old - response = f"{question_manager.get_next_question()} \n{return_llm_feedback(f'response:{prompt} history:{st.session_state.messages}')}"
    response_ask_new_question=question_manager.get_next_question()
    response_feedback=return_llm_feedback(f'response:{prompt} history:{st.session_state.messages}')
    response=f"{response_feedback} \n {response_ask_new_question}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
