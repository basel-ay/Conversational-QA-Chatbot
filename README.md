# Conversational-QA-Chatbot

## Overview
This project implements a conversational question and answer (Q&A) chatbot using LangChain and Streamlit. The chatbot interacts with users by responding to various casual inquiries and engages in conversation. It utilizes LangChain technology for natural language processing and communication, and the user interface is built with Streamlit for a seamless and interactive experience.

## Requirements
- Python 3.x
- Streamlit
- LangChain
- OpenAI API (requires API key)

## Install dependencies:
`pip install -r requirements.txt
`

## Usage
* Set up the required environment variables, including your **OpenAI API key**.
* Run the Streamlit app by executing the following command in the terminal:
  
`streamlit run app.py`

Interact with the chatbot by typing questions or messages in the input field and clicking the "Ask the question" button. The chatbot will respond with relevant answers.

## Implementation Details
* The chatbot user interface is created using Streamlit, which provides a user-friendly and interactive environment.
* LangChain's schema is used to define message types such as HumanMessage, SystemMessage, and AIMessage.
* A ChatOpenAI model is utilized for processing user inputs and generating responses.
* The conversation flow is managed and stored in the session state to maintain context between interactions.

## Future Improvements
* Integration with more advanced natural language processing models.
* Adding support for multi-turn conversations and context tracking.
* Enhancing the user interface with additional features such as voice input/output.

## Samples

![image](https://github.com/basel-ay/Conversational-QA-Chatbot/assets/64821137/37129fe3-8377-4747-b01f-560192d4114c)

![image](https://github.com/basel-ay/Conversational-QA-Chatbot/assets/64821137/ae27d877-8138-44aa-b36e-8428a762985f)
