from __future__ import annotations

from typing import Any

from neo4j import GraphDatabase

from config.config import settings


class Neo4jClient:
    def __init__(self) -> None:
        self._driver = None
        self._configured = bool(
            settings.neo4j_uri and settings.neo4j_username and settings.neo4j_password
        )
        if self._configured:
            try:
                self._driver = GraphDatabase.driver(
                    settings.neo4j_uri,
                    auth=(settings.neo4j_username, settings.neo4j_password),
                )
                self._driver.verify_connectivity()
            except Exception:
                self._driver = None
                self._configured = False

    def is_configured(self) -> bool:
        return self._configured

    def get_relationships(self) -> list[dict[str, Any]]:
        if self._driver is None:
            return [
                {
                    "source": "Opportunity",
                    "relationship": "RELATED_TO",
                    "target": "Account",
                    "details": "Opportunity is linked to the Account that owns the customer relationship.",
                },
                {
                    "source": "Opportunity",
                    "relationship": "HAS_CASE",
                    "target": "Case",
                    "details": "Opportunity can generate support cases during onboarding or service escalations.",
                },
                {
                    "source": "Case",
                    "relationship": "BELONGS_TO",
                    "target": "Account",
                    "details": "Case records are associated with the Account experiencing the issue.",
                },
            ]

        with self._driver.session(database="neo4j") as session:
            result = session.run(
                """
                MATCH (s)-[r]->(t)
                RETURN coalesce(s.name, labels(s)[0], 'Unknown') AS source,
                       type(r) AS relationship,
                       coalesce(t.name, labels(t)[0], 'Unknown') AS target,
                       properties(r) AS details
                LIMIT 25
                """
            )
            return [
                {
                    "source": record["source"],
                    "relationship": record["relationship"],
                    "target": record["target"],
                    "details": record["details"],
                }
                for record in result
            ]

    def close(self) -> None:
        if self._driver is not None:
            self._driver.close()
