from .BasePlayer import BasePlayer
from Decision import Decision


class TitForTwoTatsPlayer(BasePlayer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tats: int = 0

    def round_starts(self) -> None:
        super().round_starts()
        self.tats = 0

    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration == 0:
            return Decision.Cooperate
        
        if opponent.decisions[-1] == Decision.Defect:
            self.tats += 1
        
        if self.tats == 2:
            self.tats = 0
            return Decision.Defect
        return Decision.Cooperate