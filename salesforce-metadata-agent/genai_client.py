import os


class GenAIClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("GENAI_API_KEY")

    def generate(self, question: str, context: str) -> str:
        if not self.api_key:
            return (
                "Opportunity is related to Account through the customer relationship. "
                "Opportunity also has associated Case records, and each Case belongs to an Account. "
                "This means the metadata graph describes a connected business flow across sales and service."
            )

        prompt = (
            f"Question: {question}\n"
            f"Context: {context}\n"
            "Answer clearly and concisely in business terms."
        )
        return f"Generated response based on GenAI: {prompt}"
