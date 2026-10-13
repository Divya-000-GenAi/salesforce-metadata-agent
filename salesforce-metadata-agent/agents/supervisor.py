from agents.graph_agent import GraphAgent
from agents.planner import Planner
from agents.rag_agent import RAGAgent
from agents.validator import Validator


class Supervisor:
    def __init__(self) -> None:
        self.planner = Planner()
        self.graph_agent = GraphAgent()
        self.rag_agent = RAGAgent()
        self.validator = Validator()

    def run(self, question: str) -> str:
        route = self.planner.route(question)
        if route == "rag":
            answer = self.rag_agent.answer(question)
        else:
            answer = self.graph_agent.answer(question)
        return self.validator.validate(answer)
