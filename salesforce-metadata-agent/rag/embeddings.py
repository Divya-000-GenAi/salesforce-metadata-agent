class Embeddings:
    def __init__(self) -> None:
        self.model_name = "simple-keyword-embedding"

    def embed(self, text: str) -> list[float]:
        tokens = text.lower().split()
        return [float(len(tokens) * (idx + 1)) for idx in range(min(len(tokens), 10))]
