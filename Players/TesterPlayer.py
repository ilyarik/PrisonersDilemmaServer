from Decision import Decision
from .BasePlayer import BasePlayer


class TesterPlayer(BasePlayer):
    """
    On 1st round, defect. If the opponent retaliated, then play TIT-FOR-TAT. 
    Otherwise intersperse cooperation and defection.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.got_retaliated: bool = False

    def round_starts(self) -> None:
        super().round_starts()
        self.got_retaliated = False

    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration == 0:
            return Decision.Defect
        elif iteration == 1:
            return Decision.Cooperate

        if opponent.decisions[-1] == Decision.Defect:
            self.got_retaliated = True
                
        if iteration == 2:
            return Decision.Cooperate

        if self.got_retaliated:
            return Decision.Cooperate if opponent.decisions[-1] == Decision.Cooperate else Decision.Defect
        else:
            return Decision.Defect
