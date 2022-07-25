"""Level instance."""
class Level():
    def __init__(
            self,
            level: int,
            threshold: int,
            description: str) -> None:
        self.level = level
        self.threshold = threshold
        self.description = description