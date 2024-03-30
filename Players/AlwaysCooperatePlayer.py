from Decision import Decision
from .BasePlayer import BasePlayer


class AlwaysCooperatePlayer(BasePlayer):
    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        return Decision.Cooperate

