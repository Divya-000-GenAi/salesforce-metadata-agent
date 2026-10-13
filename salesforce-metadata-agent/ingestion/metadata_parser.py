import json
from pathlib import Path


class MetadataParser:
    def __init__(self, folder: str | None = None) -> None:
        self.folder = Path(folder) if folder else Path(__file__).resolve().parent.parent / "data" / "metadata"

    def load_json(self) -> dict:
        payload: dict = {}
        for file in sorted(self.folder.glob("*.json")):
            with file.open("r", encoding="utf-8") as handle:
                payload[file.stem] = json.load(handle)
        return payload
