class Retriever:
    def retrieve(self, question: str, docs: list[str]) -> list[str]:
        query = question.lower()
        matches: list[str] = []
        for doc in docs:
            content = doc.lower()
            if any(term in content for term in ["account", "opportunity", "case", "salesforce", "relationship"]):
                if any(term in query for term in ["account", "opportunity", "case", "relationship", "salesforce"]):
                    matches.append(doc)
        return matches[:3]
