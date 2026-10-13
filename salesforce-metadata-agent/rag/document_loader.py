from pathlib import Path


class DocumentLoader:
    def __init__(self, folder: str | None = None) -> None:
        self.folder = Path(folder) if folder else Path(__file__).resolve().parent.parent / "data" / "documents"

    def load(self) -> list[str]:
        documents: list[str] = []
        if not self.folder.exists():
            return documents

        for file in sorted(self.folder.glob("*.md")):
            documents.append(file.read_text(encoding="utf-8"))
        return documents
