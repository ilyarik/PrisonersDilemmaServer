from .BasePlayer import BasePlayer
from Decision import Decision


class AlwaysDefectPlayer(BasePlayer):
    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        return Decision.Defect
        