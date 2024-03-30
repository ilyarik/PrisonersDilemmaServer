from Decision import Decision
from .BasePlayer import BasePlayer


class TitForTatPlayer(BasePlayer):
    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration == 0:
            return Decision.Cooperate
        return Decision.Cooperate if opponent.decisions[-1] == Decision.Cooperate else Decision.Defect