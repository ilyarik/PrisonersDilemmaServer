from abc import ABC, abstractmethod
from typing import Self
from Decision import AnyDecisionType


class BasePlayer(ABC):
    def __init__(self, display_name: str = "") -> None:
        super().__init__()
        self.display_name: str = display_name if display_name else __class__.__name__
        self.decisions: list[AnyDecisionType] = []

    def round_starts(self) -> None:
        self.iteration = 0
        self.decisions = []

    def round_ends(self, opponent: Self) -> None:
        pass

    @abstractmethod
    def turn(self, opponent: Self, iteration: int = 0) -> AnyDecisionType:
        pass