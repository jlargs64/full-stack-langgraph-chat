import logging

from app.agent_service import get_agent_service
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI()
agent_service = get_agent_service()


class AgentRequest(BaseModel):
    user_input: str


@app.post("/stream")
async def stream(request: AgentRequest) -> StreamingResponse:
    logging.info(request)
    config = {"configurable": {"thread_id": "1"}}
    stream = agent_service.stream_agent_output(request.user_input, config)
    return StreamingResponse(stream, media_type="text/plain")
