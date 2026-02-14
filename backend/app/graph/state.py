from typing import TypedDict, Optional


class EventBrief(TypedDict):
    venue_name: str
    venue_type: str  # "nightclub", "rooftop", "lounge", etc.
    city: str
    date: str
    genre: str  # "RnB", "house", "hip-hop", etc.
    vibe: str  # free-form: "intimate late-night", "high-energy festival"
    dj_name: Optional[str]
    additional_notes: Optional[str]


class AgentState(TypedDict):
    event_brief: EventBrief
    research: dict  # venue + scene analysis from research node
    audience_profile: dict  # target demographic from audience node
    content: dict  # generated marketing content from content node
    human_feedback: Optional[str]  # "approve", "regenerate", or edit instructions
    final_campaign: Optional[dict]  # packaged output from export node
    current_node: str  # for streaming status updates
    messages: list  # LangGraph message history
