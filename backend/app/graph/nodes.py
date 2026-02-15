import json
from datetime import datetime, timezone
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage
from .state import AgentState
from .mock_data import get_mock_venue_data, get_mock_scene_data

llm = ChatAnthropic(model="claude-sonnet-4-20250514")


def research_node(state: AgentState) -> dict:
    """Analyze venue and local scene using mock data."""
    venue_data = get_mock_venue_data(state["event_brief"]["venue_name"])
    scene_data = get_mock_scene_data(state["event_brief"]["city"])
    return {"research": {"venue": venue_data, "scene": scene_data}, "current_node": "research"}


def audience_node(state: AgentState) -> dict:
    """Profile the target audience based on genre + venue + scene data."""
    response = llm.invoke([
        SystemMessage(content="You are a nightlife marketing strategist. Return ONLY valid JSON, no markdown."),
        HumanMessage(content=f"""Based on this event and research, create an audience profile.
        Event: {json.dumps(state["event_brief"])}
        Research: {json.dumps(state["research"])}

        Return JSON with these fields:
        - age_range (e.g. "21-30")
        - interests (list of strings)
        - platforms (list of social platforms people use the most)
        - content_preferences (what content formats they engage with)
        - price_sensitivity (low/medium/high)"""),
    ])

    audience_profile = json.loads(response.content)
    return {"audience_profile": audience_profile, "current_node": "audience"}


def content_node(state: AgentState) -> dict:
    """Generate marketing content for all channels."""
    feedback_context = ""
    if state.get("human_feedback") and state["human_feedback"] != "approve":
        feedback_context = f"\n\nThe previous content was rejected. Apply this feedback: {state['human_feedback']}"

    response = llm.invoke([
        SystemMessage(content="You are a nightlife marketing copywriter. Return ONLY valid JSON, no markdown."),
        HumanMessage(content=f"""Generate marketing content for this event.
        Event: {json.dumps(state["event_brief"])}
        Venue & Scene Research: {json.dumps(state["research"])}
        Target Audience: {json.dumps(state["audience_profile"])}{feedback_context}

        Return JSON with:
        - instagram_caption (with emojis, hashtags, CTA)
        - event_description (2-3 paragraphs for listing sites)
        - email_blast (object with "subject" and "body" fields)
        - sms_teaser (under 160 characters)"""),
    ])

    content = json.loads(response.content)
    return {"content": content, "current_node": "content"}


def review_node(state: AgentState) -> dict:
    """Human-in-the-loop checkpoint."""
    return {"current_node": "review"}


def export_node(state: AgentState) -> dict:
    """Package everything into a final campaign brief."""
    final_campaign = {
        "event_brief": state["event_brief"],
        "audience_profile": state["audience_profile"],
        "content": state["content"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "version": 1,
    }
    return {"final_campaign": final_campaign, "current_node": "export"}
