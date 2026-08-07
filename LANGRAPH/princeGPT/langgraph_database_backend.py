from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import sqlite3

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# ======================== STATE ========================

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# ======================== CHAT NODE ========================

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)

    return {"messages": [response]}


# ======================== DATABASE ========================

conn = sqlite3.connect(
    database='chatbot.db',
    check_same_thread=False
)


# LangGraph checkpointer
checkpointer = SqliteSaver(conn=conn)


# Our own table for conversation metadata
conn.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    thread_id TEXT PRIMARY KEY,
    title TEXT NOT NULL DEFAULT 'New Chat',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


# ======================== GRAPH ========================

graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)


# ======================== TITLE GENERATION ========================

def generate_title(user_message):

    prompt = f"""
    Generate a short conversation title based on the user's message.

    Rules:
    - Maximum 5 words
    - No quotation marks
    - No punctuation at the end
    - Make it descriptive
    - Return ONLY the title

    User message:
    {user_message}
    """

    response = llm.invoke(prompt)

    return response.content.strip()


# ======================== THREAD DATABASE FUNCTIONS ========================

def create_thread(thread_id):

    thread_id = str(thread_id)

    conn.execute(
        """
        INSERT OR IGNORE INTO conversations (thread_id, title)
        VALUES (?, ?)
        """,
        (thread_id, "New Chat")
    )

    conn.commit()


def update_thread_title(thread_id, title):

    thread_id = str(thread_id)

    conn.execute(
        """
        UPDATE conversations
        SET title = ?
        WHERE thread_id = ?
        """,
        (title, thread_id)
    )

    conn.commit()


def retrieve_all_threads():

    cursor = conn.execute(
        """
        SELECT thread_id, title
        FROM conversations
        ORDER BY created_at ASC
        """
    )

    threads = []

    for row in cursor.fetchall():

        threads.append({
            'thread_id': row[0],
            'title': row[1]
        })

    return threads