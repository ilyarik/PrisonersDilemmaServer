from Decision import Decision
from .BasePlayer import BasePlayer


class StatisticPlayer(BasePlayer):
    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if opponent.decisions.count(Decision.Cooperate) >= iteration//2:
            return Decision.Cooperate
        else:
            return Decision.Defect

