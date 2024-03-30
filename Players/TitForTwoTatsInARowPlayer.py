from .BasePlayer import BasePlayer
from Decision import Decision


class TitForTwoTatsInARowPlayer(BasePlayer):
    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration == 0 or iteration == 1:
            return Decision.Cooperate
                
        if opponent.decisions[-1] == Decision.Defect and opponent.decisions[-2] == Decision.Defect:
            return Decision.Defect
        return Decision.Cooperate