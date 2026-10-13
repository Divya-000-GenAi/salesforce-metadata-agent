from ingestion.metadata_parser import MetadataParser


class SalesforceLoader:
    def __init__(self) -> None:
        self.parser = MetadataParser()

    def load(self) -> dict:
        return self.parser.load_json()
