from agents.planner import Planner
from agents.graph_agent import GraphAgent


def test_planner_routes_metadata_questions_to_graph():
    planner = Planner()
    route = planner.route("How is Opportunity related to Account and Case?")
    assert route == "graph"


def test_graph_agent_returns_relationship_summary():
    agent = GraphAgent()
    result = agent.answer("How is Opportunity related to Account and Case?")
    assert "Opportunity" in result
    assert "Account" in result or "Case" in result
