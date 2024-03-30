from .BasePlayer import BasePlayer
from Decision import Decision


class DowningPlayer(BasePlayer):
    """
    It will try to understand its opponent and then make the choice to maximize its score in the long run.
    If the other player is not responsive to what DOWNING wasdoing, 
    DOWNING will try to get away with whatever it can by defecting.
    If the other player seems responsive, it will cooperate.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.responsiveness: float = 0.5

    def round_starts(self) -> None:
        super().round_starts()
        self.responsiveness = 0.5

    def _check_bounds(self) -> None:
        if self.responsiveness > 1.0:
            self.responsiveness = 1
        elif self.responsiveness < 0.0:
            self.responsiveness = 0

    def _inc_responsiveness(self) -> None:
        self.responsiveness += 0.1
        self._check_bounds()

    def _dec_responsiveness(self) -> None:
        self.responsiveness -= 0.1
        self._check_bounds()

    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration == 0:
            return Decision.Defect
        elif iteration == 1:
            return Decision.Defect
        elif iteration == 2:
            if opponent.decisions[-1] == Decision.Defect:
                self._inc_responsiveness()
        else:
        
            # correct responsiveness
            if self.decisions[-3] != self.decisions[-2] and opponent.decisions[-2] != opponent.decisions[-1]:
                self._inc_responsiveness()  
            elif self.decisions[-3] == self.decisions[-2] and opponent.decisions[-2] != opponent.decisions[-1]:
                self._dec_responsiveness()
            elif self.decisions[-3] != self.decisions[-2] and opponent.decisions[-2] == opponent.decisions[-1]:
                self._dec_responsiveness()
            else:
                if self.decisions[-2] == opponent.decisions[-1] == Decision.Cooperate:
                    self._inc_responsiveness()
                # else:
                #     self._dec_responsiveness()
        
        if self.responsiveness > 0.5:
            return Decision.Cooperate
        else:
            return Decision.Defect
