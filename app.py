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

