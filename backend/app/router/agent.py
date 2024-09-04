import logging

from app.schema.agent import AgentRequest
from app.services import agent_service
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/agents", tags=["agents"])


@router.post("/stream")
async def stream(request: AgentRequest) -> StreamingResponse:
    logging.info(request)
    config = {"configurable": {"thread_id": "1"}}
    stream = agent_service.stream_agent_output(request.user_input, config)
    return StreamingResponse(stream, media_type="text/plain")
