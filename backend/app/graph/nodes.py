from langchain_anthropic import ChatAnthropic
from .state import AgentState
from .mock_data import get_mock_venue_data, get_mock_scene_data

llm = ChatAnthropic(model="claude-sonnet-4-20250514")


def research_node(state: AgentState) -> dict:
    """
    Analyze venue and local scene.

    TODO:
    1. Pull mock data based on state["event_brief"]["venue_name"] and city
    2. Return {"research": {...venue_info, scene_context, competing_events}}

    In production, this would call Tavily/SerpAPI tools.
    For now, use mock_data.py to return realistic venue data.
    """
    pass


def audience_node(state: AgentState) -> dict:
    """
    Profile the target audience based on genre + venue + scene data.

    TODO:
    1. Build a prompt using state["event_brief"] + state["research"]
    2. Ask the LLM to output a structured audience profile:
       - age_range, interests, platforms, content_preferences, price_sensitivity
    3. Parse the response (use structured output or JSON mode)
    4. Return {"audience_profile": {...}}

    Tip: Use a system prompt that positions the LLM as a nightlife marketing strategist.
    """
    pass


def content_node(state: AgentState) -> dict:
    """
    Generate marketing content for all channels.

    TODO:
    1. Build a prompt using event_brief + research + audience_profile
    2. Generate:
       - instagram_caption (with emojis, hashtags, CTA)
       - event_description (2-3 paragraphs for listing sites)
       - email_blast (subject line + body for mailing list)
       - sms_teaser (under 160 chars)
    3. Return {"content": {instagram_caption, event_description, email_blast, sms_teaser}}

    Tip: You can make separate LLM calls per content type, or one big structured call.
    Separate calls = more control, one call = faster.
    """
    pass


def review_node(state: AgentState) -> dict:
    """
    Human-in-the-loop checkpoint.

    This node is interrupted BEFORE execution via LangGraph's interrupt_before.
    The frontend shows the generated content, user provides feedback.
    When resumed, state["human_feedback"] will be populated.

    TODO:
    1. Check state["human_feedback"]
    2. If "approve" -> return state as-is (graph continues to export)
    3. If feedback contains edit instructions -> route back to content_node
       (you'll handle this via conditional edges in graph.py)
    """
    pass


def export_node(state: AgentState) -> dict:
    """
    Package everything into a final campaign brief.

    TODO:
    1. Combine event_brief + audience_profile + approved content
    2. Structure as a clean campaign object with metadata (generated_at, version, etc.)
    3. Return {"final_campaign": {...}}
    """
    pass
