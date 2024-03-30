from Decision import Decision
from .BasePlayer import BasePlayer
from random import random


class JossPlayer(BasePlayer):
    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration == 0:
            return Decision.Cooperate
        if opponent.decisions[-1] == Decision.Defect or random() < 0.1:
            return Decision.Defect
        return Decision.Cooperate