def build_relationship_summary(question: str, relationships: list[dict]) -> str:
    ordered = []
    for item in relationships:
        ordered.append(
            f"- {item['source']} {item['relationship']} {item['target']}: {item['details']}"
        )

    context = "\n".join(ordered)
    return (
        "Based on the metadata graph, this relationship is modeled as follows:\n"
        f"{context}\n\n"
        f"Question: {question}"
    )
