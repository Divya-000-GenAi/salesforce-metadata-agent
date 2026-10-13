class Validator:
    def validate(self, answer: str) -> str:
        cleaned = answer.strip()
        if not cleaned:
            return "No answer produced."
        return cleaned
