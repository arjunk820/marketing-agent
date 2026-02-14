from pydantic import BaseModel
from typing import Optional


class EventBriefInput(BaseModel):
    venue_name: str
    venue_type: str
    city: str
    date: str
    genre: str
    vibe: str
    dj_name: Optional[str] = None
    additional_notes: Optional[str] = None


class ReviewInput(BaseModel):
    feedback: str  # "approve" or edit instructions
