from Decision import Decision
from .BasePlayer import BasePlayer


class FlexiblePlayer(BasePlayer):
    """
    Flexible one combines different strategies and applies it at a different stage. 
    First ten rounds: it cooperates as TRANQUILIZER does, no matter what the opponent does.
    Rounds[10:-20]: Then it continues to cooperate until and if the opponent suddenly defects first.
    20 steps before the average round length: Flexible one defects once and checks whether the opponent retaliated or not. Similar to DOWNING.
    If the opponent retaliated it retuns to TITFORTAT until the end. If the opponent defects twice in a row Flexible player defects until the end.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.got_retaliated: bool = False
        self.got_defect: bool = False
        self.trigger: bool = False

    def round_starts(self) -> None:
        super().round_starts()
        self.got_retaliated = False
        self.got_defect = False
        self.trigger = False

    def turn(self, opponent: BasePlayer, iteration: int = 0) -> Decision:
        if iteration > 10:
            if opponent.decisions[-1] == Decision.Defect:
                self.got_defect = True

        if iteration == 0:
            return Decision.Cooperate
        if iteration in range(1, 80):
            return Decision.Cooperate if opponent.decisions[-1] == Decision.Cooperate else Decision.Defect
        elif iteration == 80:
            if not self.got_defect:
                return Decision.Defect
            else:
                return Decision.Cooperate if opponent.decisions[-1] == Decision.Cooperate else Decision.Defect
        elif iteration == 81:
            if not self.got_defect:
                return Decision.Cooperate
            else:
                return Decision.Cooperate if opponent.decisions[-1] == Decision.Cooperate else Decision.Defect
        elif iteration == 82:
            if opponent.decisions[-1] == Decision.Defect and Decision.Defect not in opponent.decisions[:-1]:
                self.got_retaliated = True
                return Decision.Cooperate
            elif opponent.decisions[-1] == Decision.Cooperate and Decision.Defect not in opponent.decisions[:-1]:
                return Decision.Defect
            else:
                return Decision.Cooperate if opponent.decisions[-1] == Decision.Cooperate else Decision.Defect
        else:
            if opponent.decisions[-1] == Decision.Defect and Decision.Defect not in opponent.decisions[:-1]:
                self.got_retaliated = True
                return Decision.Cooperate

            if self.trigger:
                return Decision.Defect
            elif opponent.decisions[-2:] == [Decision.Defect, Decision.Defect]:
                self.trigger = True
                return Decision.Defect
            elif self.got_retaliated:
                return Decision.Cooperate if opponent.decisions[-1] == Decision.Cooperate else Decision.Defect
            else:
                return Decision.Defect
