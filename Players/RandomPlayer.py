from .BasePlayer import BasePlayer
from Decision import Decision
from random import choice


class RandomPlayer(BasePlayer):
    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        return choice(list(Decision))