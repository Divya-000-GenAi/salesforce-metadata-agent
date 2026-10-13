class RAGAgent:
    def answer(self, question: str) -> str:
        return (
            "This question is best answered from the documentation and metadata references. "
            "Use the document store to retrieve context about the object semantics and business process."
        )
