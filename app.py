## Conversational Q&A Chatbot
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

import os


# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's chat")

from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(temperature=0.5)

if "FlowMessages" not in st.session_state:
    st.session_state["FlowMessages"] = [
        SystemMessage(content="You are an AI assistant")
    ]


## Function to load OpenAI model and get respones
def get_chatmodel_responses(question):
    """Get a prompt from user and return a response/answer."""

    st.session_state["FlowMessages"].append(HumanMessage(content=question))

    # Pass the question to our openai model
    answer = chat(st.session_state["FlowMessages"])

    st.session_state["FlowMessages"].append(AIMessage(content=answer.content))

    return answer.content


input = st.text_input("Input: ", key="input")
response = get_chatmodel_responses(input)

submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
