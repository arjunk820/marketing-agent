from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from .state import AgentState
from .nodes import research_node, audience_node, content_node, review_node, export_node


def should_regenerate(state: AgentState) -> str:
    if state["human_feedback"] == "approve":
        return "export"
    else:
        return "content"


def build_graph():

    graph = StateGraph(AgentState)

    # Add your nodes here
    graph.add_node("research", research_node)
    graph.add_node("audience", audience_node)
    graph.add_node("content", content_node)
    graph.add_node("review", review_node)
    graph.add_node("export", export_node)    

    # Add your edges here
    graph.add_edge(START, "research")
    graph.add_edge("research", "audience")
    graph.add_edge("audience", "content")
    graph.add_edge("content", "review")
    graph.add_conditional_edges("review", should_regenerate)
    graph.add_edge("export", END)

    # Compile with checkpointer and interrupt
    checkpointer = MemorySaver()
    return graph.compile(
        checkpointer=checkpointer,
        interrupt_before=["review"],
    )
