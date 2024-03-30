from Decision import Decision
from .BasePlayer import BasePlayer


class TranquilizerPlayer(BasePlayer):
    """
    TRANQUILIZER tends to wait a dozen or two moves before defecting to see if the other player would let itself be lulled and occasionally exploited. 
    If so, TRANQUILIZER throws in additional defections at more frequent intervals, until it was forced to back off by the other's response.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.max_cooperate: int = 10
        self.cooperated_row: int = 10

    def round_starts(self) -> None:
        super().round_starts()
        self.max_cooperate = 10
        self.cooperated_row = 0

    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration < 10:
            self.cooperated_row += 1
            return Decision.Cooperate

        if self.decisions[-2] == Decision.Defect:
            if opponent.decisions[-1] == Decision.Defect:
                self.max_cooperate = 10
            elif self.max_cooperate > 1:
                self.max_cooperate -= 1

        if self.cooperated_row >= self.max_cooperate:
            self.cooperated_row = 0
            return Decision.Defect

        self.cooperated_row += 1
        return Decision.Cooperate
