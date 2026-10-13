from genai_client import GenAIClient


def test_genai_client_falls_back_to_graph_summary_when_api_key_missing():
    client = GenAIClient()
    answer = client.generate(
        "How is Opportunity related to Account and Case?",
        "Opportunity RELATED_TO Account; Opportunity HAS_CASE Case; Case BELONGS_TO Account"
    )
    assert "Opportunity" in answer
    assert "Account" in answer or "Case" in answer
