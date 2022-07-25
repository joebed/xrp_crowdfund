"""Fundraiser instance."""
from models.level import Level

class Fundraiser():
    def __init__(
            self,
            name: str,
            goal: int,
            drops_raised: int,
            levels: Level,
            host: str) -> None:
        self.name = name
        self.goal = goal
        self.drops_raised = drops_raised
        self.levels = levels
        self.host = host
    
    def pledge(
            self,
            sender: str):
        pass
