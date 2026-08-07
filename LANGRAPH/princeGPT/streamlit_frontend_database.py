import streamlit as st
from langgraph_database_backend import (
    chatbot,
    retrieve_all_threads,
    create_thread,
    generate_title,
    update_thread_title
)
from langchain_core.messages import HumanMessage
import uuid


# =============================================================================
#                               UTILITY FUNCTIONS
# =============================================================================

def generate_thread_id():
    """
    Generate a new unique thread ID.

    We convert UUID to string because SQLite stores thread_id as TEXT.
    """
    return str(uuid.uuid4())


def add_thread(thread_id):
    """
    Add a new thread to:
    1. Streamlit session state
    2. SQLite conversations table
    """

    # Check whether this thread already exists
    if not any(
        chat['thread_id'] == thread_id
        for chat in st.session_state['chat_threads']
    ):

        new_chat = {
            'thread_id': thread_id,
            'title': 'New Chat'
        }

        # Add to Streamlit session
        st.session_state['chat_threads'].append(new_chat)

        # Add permanently to SQLite
        create_thread(thread_id)


def reset_chat():
    """
    Create a completely new conversation.
    """

    thread_id = generate_thread_id()

    st.session_state['thread_id'] = thread_id

    # Clear messages first
    st.session_state['message_history'] = []

    # Add thread to session + database
    add_thread(thread_id)


def update_title_in_session(thread_id, title):
    """
    Update the title inside Streamlit's session state.

    SQLite is updated separately using update_thread_title().
    """

    for chat in st.session_state['chat_threads']:

        if chat['thread_id'] == thread_id:
            chat['title'] = title
            break


def load_conversation(thread_id):
    """
    Retrieve conversation messages stored by LangGraph's
    SQLite checkpointer.
    """

    state = chatbot.get_state(
        config={
            'configurable': {
                'thread_id': thread_id
            }
        }
    )

    # New/empty threads may not contain messages yet
    return state.values.get('messages', [])


# =============================================================================
#                               SESSION SETUP
# =============================================================================

# Store messages currently displayed on screen
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# Load all existing conversations from our SQLite metadata table
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()


# Create current thread if one doesn't exist
if 'thread_id' not in st.session_state:

    # ---------------------------------------------------------
    # If conversations already exist:
    # open the most recent conversation
    #
    # Otherwise:
    # create a completely new conversation
    # ---------------------------------------------------------

    if len(st.session_state['chat_threads']) > 0:

        latest_chat = st.session_state['chat_threads'][-1]

        st.session_state['thread_id'] = latest_chat['thread_id']

        messages = load_conversation(
            latest_chat['thread_id']
        )

        temp_messages = []

        for msg in messages:

            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_messages.append({
                'role': role,
                'content': msg.content
            })

        st.session_state['message_history'] = temp_messages

    else:

        # No conversations exist yet
        thread_id = generate_thread_id()

        st.session_state['thread_id'] = thread_id

        add_thread(thread_id)


# =============================================================================
#                               SIDEBAR UI
# =============================================================================

st.sidebar.title('LangGraph Chatbot')


# --------------------------- NEW CHAT BUTTON ---------------------------

if st.sidebar.button(
    '➕ New Chat',
    use_container_width=True
):

    reset_chat()

    # Immediately refresh UI
    st.rerun()


st.sidebar.header('My Conversations')


# --------------------------- CONVERSATION LIST ---------------------------

for chat in st.session_state['chat_threads'][::-1]:

    thread_id = chat['thread_id']
    title = chat['title']

    # Show TITLE instead of UUID
    if st.sidebar.button(
        title,
        key=f"chat_{thread_id}",
        use_container_width=True
    ):

        # Change active conversation
        st.session_state['thread_id'] = thread_id


        # Retrieve messages from LangGraph
        messages = load_conversation(thread_id)


        # Convert LangChain messages into format
        # expected by Streamlit
        temp_messages = []

        for msg in messages:

            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_messages.append({
                'role': role,
                'content': msg.content
            })


        # Replace currently displayed messages
        st.session_state['message_history'] = temp_messages

        st.rerun()


# =============================================================================
#                               MAIN CHAT UI
# =============================================================================

# Display current conversation history
for message in st.session_state['message_history']:

    with st.chat_message(message['role']):

        st.markdown(
            message['content']
        )


# =============================================================================
#                               USER INPUT
# =============================================================================

user_input = st.chat_input(
    'Type here'
)


if user_input:

    # -------------------------------------------------------------------------
    # IMPORTANT
    #
    # Determine whether this is the FIRST message BEFORE adding
    # the user message to message_history.
    # -------------------------------------------------------------------------

    is_first_message = (
        len(st.session_state['message_history']) == 0
    )


    # -------------------------------------------------------------------------
    # Store user message in Streamlit
    # -------------------------------------------------------------------------

    st.session_state['message_history'].append({
        'role': 'user',
        'content': user_input
    })


    # Display user message
    with st.chat_message('user'):

        st.markdown(
            user_input
        )


    # -------------------------------------------------------------------------
    # LangGraph configuration
    # -------------------------------------------------------------------------

    CONFIG = {

        'configurable': {
            'thread_id': st.session_state['thread_id']
        },

        'metadata': {
            'thread_id': st.session_state['thread_id']
        },

        'run_name': 'chat_turn'
    }


    # -------------------------------------------------------------------------
    # Generate assistant response
    # -------------------------------------------------------------------------

    with st.chat_message('assistant'):

        ai_message = st.write_stream(

            message_chunk.content

            for message_chunk, metadata

            in chatbot.stream(

                {
                    'messages': [
                        HumanMessage(
                            content=user_input
                        )
                    ]
                },

                config=CONFIG,

                stream_mode='messages'
            )
        )


    # -------------------------------------------------------------------------
    # Store assistant response in Streamlit session
    # -------------------------------------------------------------------------

    st.session_state['message_history'].append({

        'role': 'assistant',

        'content': ai_message

    })


    # =========================================================================
    #                         GENERATE CHAT TITLE
    # =========================================================================

    # Generate title ONLY after the first AI response
    if is_first_message:

        try:

            # -------------------------------------------------------------
            # Generate title using Gemini
            # -------------------------------------------------------------

            title = generate_title(
                user_input
            )


            # -------------------------------------------------------------
            # Save title permanently into SQLite
            # -------------------------------------------------------------

            update_thread_title(
                st.session_state['thread_id'],
                title
            )


            # -------------------------------------------------------------
            # Update Streamlit session state
            #
            # This means the sidebar also knows the new title
            # without needing to retrieve everything from SQLite again.
            # -------------------------------------------------------------

            update_title_in_session(
                st.session_state['thread_id'],
                title
            )


            # -------------------------------------------------------------
            # Rerun Streamlit
            #
            # This causes:
            #
            # New Chat
            #     ↓
            # Generated Conversation Title
            #
            # to appear immediately in sidebar.
            # -------------------------------------------------------------

            st.rerun()


        except Exception as e:

            # Chat should still work even if title generation fails.
            print(
                f"Error generating conversation title: {e}"
            )