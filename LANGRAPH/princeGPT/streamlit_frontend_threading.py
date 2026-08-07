import streamlit as st
from langgraph_backend import chatbot, generate_title
from langchain_core.messages import HumanMessage
import uuid


# ---------------- UTILITY FUNCTIONS ----------------

def generate_thread():
    return str(uuid.uuid4())


def reset_chat():
    thread_id = generate_thread()

    st.session_state['thread_id'] = thread_id

    add_thread(thread_id)

    st.session_state['message_history'] = []


def add_thread(thread_id):

    if not any(
        chat['thread_id'] == thread_id
        for chat in st.session_state['chat_threads']
    ):

        st.session_state['chat_threads'].append({
            'thread_id': thread_id,
            'title': 'New Chat'
        })


def update_thread_title(thread_id, title):

    for chat in st.session_state['chat_threads']:

        if chat['thread_id'] == thread_id:
            chat['title'] = title
            break


def load_conversation(thread_id):

    return chatbot.get_state(
        config={
            'configurable': {
                'thread_id': thread_id
            }
        }
    ).values['messages']


# ---------------- SESSION STATE ----------------

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread()


if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []


add_thread(st.session_state['thread_id'])


# ---------------- SIDEBAR ----------------

st.sidebar.title("Langgraph based chatbot")


if st.sidebar.button("New Chat"):
    reset_chat()


st.sidebar.title("My conversations")


for chat in st.session_state["chat_threads"][::-1]:

    if st.sidebar.button(
        chat['title'],
        key=chat['thread_id']
    ):

        st.session_state['thread_id'] = chat['thread_id']

        messages = load_conversation(
            chat['thread_id']
        )

        temp_message_dict = []

        for message in messages:

            if isinstance(message, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_message_dict.append({
                'role': role,
                'content': message.content
            })

        st.session_state['message_history'] = temp_message_dict


# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state['message_history']:

    with st.chat_message(message['role']):
        st.text(message['content'])


# ---------------- USER INPUT ----------------

user_input = st.chat_input('Type here')


if user_input:

    # Check BEFORE adding message
    is_first_message = (
        len(st.session_state['message_history']) == 0
    )

    # Generate conversation title
    if is_first_message:

        title = generate_title(user_input)

        update_thread_title(
            st.session_state['thread_id'],
            title
        )


    # Add user message
    st.session_state['message_history'].append({
        'role': 'user',
        'content': user_input
    })


    with st.chat_message('user'):
        st.text(user_input)


    # IMPORTANT:
    # Build config using CURRENT thread
    CONFIG = {
        'configurable': {
            'thread_id': st.session_state['thread_id']
        }
    }


    # Generate assistant response
    with st.chat_message('assistant'):

        ai_message = st.write_stream(

            message_chunk.content

            for message_chunk, metadata
            in chatbot.stream(

                {
                    'messages': [
                        HumanMessage(content=user_input)
                    ]
                },

                config=CONFIG,

                stream_mode='messages'
            )
        )


    # Store assistant response
    st.session_state['message_history'].append({
        'role': 'assistant',
        'content': ai_message
    })