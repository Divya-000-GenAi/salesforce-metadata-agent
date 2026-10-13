import re


class Planner:
    def route(self, question: str) -> str:
        lowered = question.lower()

        if any(keyword in lowered for keyword in [
            "related", "relationship", "connect", "connected", "depends", "dependency",
            "object", "field", "lookup", "master-detail", "schema", "metadata"
        ]):
            return "graph"

        if any(keyword in lowered for keyword in [
            "document", "policy", "definition", "reference", "explain", "what is"
        ]):
            return "rag"

        return "graph"
