from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from .state import AgentState
from .nodes import research_node, audience_node, content_node, review_node, export_node


def should_regenerate(state: AgentState) -> str:
    """
    Conditional edge after review_node.

    TODO:
    - If human_feedback == "approve" -> route to "export"
    - If human_feedback contains edit instructions -> route to "content"
    """
    pass


def build_graph():
    """
    TODO:
    1. Create StateGraph with AgentState
    2. Add nodes: research, audience, content, review, export
    3. Add edges:
       - START -> research
       - research -> audience
       - audience -> content
       - content -> review
       - review -> conditional edge (should_regenerate)
       - export -> END
    4. Set interrupt_before=["review"] for human-in-the-loop
    5. Compile with MemorySaver checkpointer
    6. Return compiled graph
    """

    graph = StateGraph(AgentState)

    # Add your nodes here

    # Add your edges here

    # Compile with checkpointer and interrupt
    checkpointer = MemorySaver()
    return graph.compile(
        checkpointer=checkpointer,
        interrupt_before=["review"],
    )
