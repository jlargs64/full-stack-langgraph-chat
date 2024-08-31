from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.graph.state import CompiledStateGraph

load_dotenv()
llm = GoogleGenerativeAI(model="gemini-1.5-flash")


# State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


agent_graph = StateGraph(AgentState)
memory = MemorySaver()


# Nodes
async def agent_node(state: AgentState):
    messages = state["messages"]
    response = await llm.ainvoke(messages)
    return {"messages": [response]}


agent_graph.add_node("agent", agent_node)

# Edges
agent_graph.add_edge("agent", END)
agent_graph.set_entry_point("agent")

# Compile
compiled_agent: CompiledStateGraph = agent_graph.compile(checkpointer=memory)


def get_agent() -> CompiledStateGraph:
    return compiled_agent
