class VectorStore:
    def __init__(self) -> None:
        self._documents: list[str] = []

    def add(self, docs: list[str]) -> None:
        self._documents.extend(docs)

    def search(self, query: str) -> list[str]:
        q = query.lower()
        return [doc for doc in self._documents if q in doc.lower()][:5]
