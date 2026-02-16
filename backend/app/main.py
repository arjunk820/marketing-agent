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
    """
    TODO:
    1. Generate a campaign_id (uuid)
    2. Create a thread_id for LangGraph (this is how it tracks state)
    3. Invoke the graph with the event brief as initial state
       - The graph will run until it hits the interrupt at review_node
    4. Store the campaign state in campaign_store
    5. Return {campaign_id, status: "awaiting_review"}

    Key LangGraph concept:
      result = graph.invoke(
          initial_state,
          config={"configurable": {"thread_id": thread_id}}
      )
    """

    campaign_id = str(uuid.uuid4())
    thread_id = str(uuid.uuid4())
    result = graph.invoke({"event_brief": brief.model_dump()}, 
                  config={"configurable": {"thread_id": thread_id}})
    campaign_store[campaign_id] = {"thread_id": thread_id, "status": "awaiting_review", "state": result}
    return {"campaign_id": campaign_id, "status": "awaiting_review"}


@app.get("/campaigns/{campaign_id}/stream")
async def stream_campaign(campaign_id: str):
    """
    TODO:
    1. Use graph.stream() instead of invoke() for real-time updates
    2. Yield SSE events as each node completes:
       data: {"node": "research", "status": "complete", "preview": "..."}
    3. Frontend connects via EventSource

    SSE format:
      yield f"data: {json.dumps(event)}\\n\\n"

    Key LangGraph concept:
      for event in graph.stream(state, config):
          yield format_sse(event)
    """
    pass


@app.post("/campaigns/{campaign_id}/review")
async def submit_review(campaign_id: str, review: ReviewInput):
    """
    TODO:
    1. Look up the campaign's thread_id from campaign_store
    2. Update the graph state with human_feedback
    3. Resume the graph from the interrupt:
       graph.invoke(None, config={"configurable": {"thread_id": thread_id}})
       (passing None resumes from last checkpoint)
    4. Return the updated campaign state
    """
    pass


@app.get("/campaigns/{campaign_id}")
async def get_campaign(campaign_id: str):
  if campaign_id not in campaign_store: # Raise exception if not found
      raise HTTPException(status_code=404, detail="Campaign not found")
  return campaign_store[campaign_id]
