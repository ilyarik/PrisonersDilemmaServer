from Players.BasePlayer import BasePlayer
from Decision import Decision


class PrisonersGame:
    def __init__(self, player1: BasePlayer, player2: BasePlayer) -> None:
        self.player1 = player1
        self.player2 = player2
        self.interrupt: bool = False

    def play_round(self, iterations: int = 1) -> None:
        for i in range(iterations):
            self.play(i)
            # if SocketDecision.Quit in [self.decisions[0][-1], self.decisions[1][-1]] \
            # or SocketDecision.PrintQuit in [self.decisions[0][-1], self.decisions[1][-1]]:
            if self.player1.decisions[-1] not in Decision \
            or self.player2.decisions[-1] not in Decision:
                break
        self.player1.round_ends(self.player2)
        self.player2.round_ends(self.player1)

    def play(self, iteration: int = 0) -> None:
        if iteration == 0:
            self.player1.round_starts()
            self.player2.round_starts()
        assert all(isinstance(d, Decision) is True for d in self.player2.decisions), "Can't play after non-game decision"
        decision0 = self.player1.turn(self.player2, iteration)
        assert all(isinstance(d, Decision) is True for d in self.player1.decisions), "Can't play after non-game decision"
        decision1 = self.player2.turn(self.player1, iteration)
        self.player1.decisions.append(decision0)
        self.player2.decisions.append(decision1)
