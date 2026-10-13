import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    neo4j_uri: str | None = os.getenv("NEO4J_URI")
    neo4j_username: str | None = os.getenv("NEO4J_USERNAME")
    neo4j_password: str | None = os.getenv("NEO4J_PASSWORD")
    project_root: Path = Path(__file__).resolve().parent.parent


settings = Settings()
