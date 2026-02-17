from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from .models import EventBriefInput, ReviewInput
from .graph.graph import build_graph
from .store import campaign_store
import uuid
import json
import asyncio

app = FastAPI(title="Fantasia Marketing Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = build_graph()


@app.post("/campaigns")
async def create_campaign(brief: EventBriefInput):
    campaign_id = str(uuid.uuid4())
    thread_id = str(uuid.uuid4())
    result = await asyncio.to_thread(
                  graph.invoke, {"event_brief": brief.model_dump()}, 
                  config={"configurable": {"thread_id": thread_id}})
    campaign_store[campaign_id] = {"thread_id": thread_id, "status": "awaiting_review", "state": result}
    return {"campaign_id": campaign_id, "status": "awaiting_review"}


@app.get("/campaigns/{campaign_id}/stream")
async def stream_campaign(campaign_id: str):
    if campaign_id not in campaign_store:
        raise HTTPException(status_code=404, detail="Campaign not found")

    thread_id = campaign_store[campaign_id]["thread_id"]
    config = {"configurable": {"thread_id": thread_id}}

    async def event_generator():
        loop = asyncio.get_event_loop()
        # Use a queue to yield events as they arrive
        chunks = await loop.run_in_executor(None, lambda: list(graph.stream(None, config=config)))
        for chunk in chunks:
            for node_name, node_output in chunk.items():
                event = {"node": node_name, "status": "complete", "output": node_output}
                yield f"data: {json.dumps(event)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.post("/campaigns/{campaign_id}/review")
async def submit_review(campaign_id: str, review: ReviewInput):
    if campaign_id not in campaign_store:
        raise HTTPException(status_code=404, detail="Campaign not found")
    thread_id = campaign_store[campaign_id]["thread_id"]
    result = await asyncio.to_thread(
                graph.invoke, {"human_feedback": review.feedback}, 
                config={"configurable": {"thread_id": thread_id}})
    status = "exported" if review.feedback == "approve" else "awaiting_review"
    campaign_store[campaign_id] = {"thread_id": thread_id, "status": status, "state": result}
    return result


@app.get("/campaigns/{campaign_id}")
async def get_campaign(campaign_id: str):
    if campaign_id not in campaign_store: # Raise exception if not found
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign_store[campaign_id]
