from graph.neo4j_client import Neo4jClient


class Neo4jLoader:
    def __init__(self) -> None:
        self.client = Neo4jClient()

    def load(self, metadata: dict) -> list[dict]:
        if self.client is None:
            return []
        return self.client.get_relationships()
