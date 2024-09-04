import logging

from app.agent.agent import get_agent
from fastapi import HTTPException
from langchain_core.messages import HumanMessage
from langgraph.graph.state import CompiledStateGraph


class AgentService:
    def __init__(self, agent: CompiledStateGraph) -> None:
        self.agent = agent

    async def stream_agent_output(self, input: str, config: dict[str, dict[str, str]]):
        try:
            inputs = {"messages": [HumanMessage(content=input)]}
            async for output in self.agent.astream(
                inputs, config=config, stream_mode="updates"
            ):
                for value in output.values():
                    yield value["messages"][-1]
        except Exception as e:
            logging.exception(e)
            raise HTTPException(
                status_code=500, detail="Oops! An error occurred. Try again later."
            )


def get_agent_service() -> AgentService:
    return AgentService(get_agent())
