from graph.neo4j_client import Neo4jClient


def test_neo4j_client_reports_configuration(monkeypatch):
    monkeypatch.setenv("NEO4J_URI", "neo4j+s://example.databases.neo4j.io")
    monkeypatch.setenv("NEO4J_USERNAME", "neo4j")
    monkeypatch.setenv("NEO4J_PASSWORD", "secret")

    client = Neo4jClient()
    assert client.is_configured() is True
