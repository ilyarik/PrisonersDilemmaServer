from .BasePlayer import BasePlayer
from Decision import Decision


class GrimTriggerPlayer(BasePlayer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.is_triggered: bool = False

    def round_starts(self) -> None:
        super().round_starts()
        self.is_triggered = False

    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration == 0:
            return Decision.Cooperate
        elif not self.is_triggered and opponent.decisions[-1] == Decision.Defect:
            self.is_triggered = True
        return Decision.Defect if self.is_triggered else Decision.Cooperate