"""Fundraiser instance."""
from models.level import Level

class Fundraiser():
    def __init__(
            self,
            name: str,
            goal: int,
            levels: Level,
            host: str) -> None:
        self.name = name
        self.goal = goal
        self.drops_raised = 0
        self.levels = levels
        self.host = host
    
    def pledge(
            self,
            sender: str):
        pass

    def __repr__(self) -> str:
        return f"Fundraiser {self.name}\n\thost:\t{self.host}\n\tprogress:\t{self.drops_raised}/{self.goal}"
