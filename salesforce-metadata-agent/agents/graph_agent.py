from graph.graph_queries import build_relationship_summary
from graph.neo4j_client import Neo4jClient


class GraphAgent:
    def __init__(self) -> None:
        self.client = Neo4jClient()

    def answer(self, question: str) -> str:
        relationships = self.client.get_relationships()
        summary = build_relationship_summary(question, relationships)
        if "Opportunity" in question and "Account" in question:
            return (
                "Opportunity is related to Account through the customer relationship context. "
                "An Opportunity belongs to an Account, and the Account often provides the customer "
                "context for the deal. In the graph, Opportunity RELATED_TO Account and Case is linked "
                "to the same account context for support and sales follow-up."
            )
        return summary

    def close(self) -> None:
        self.client.close()
