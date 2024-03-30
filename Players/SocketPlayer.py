from Decision import Decision, AnyDecisionType, SocketDecision, get_points
from .BasePlayer import BasePlayer
from Environments.BaseEnvironment import BaseEnvironment
from MySocket import NEWLINE, MySocket
from Formatter import Formatter
from MyLogger import MyLogger
from random import randint, choice


class SocketPlayer(BasePlayer):
    def __init__(self, sock: MySocket, game_env: BaseEnvironment, logger: MyLogger | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mysock: MySocket = sock
        self.game_env: BaseEnvironment = game_env
        self.logger = logger
        self.last_phrase: str = ""

    def round_starts(self) -> None:
        super().round_starts()
        self.decisions = []

    def round_ends(self, opponent: BasePlayer) -> None:
        round_stat = self._get_round_stat(opponent)
        self.mysock.mysendline(round_stat)
        self.mysock.mysendline("End of the round")
        self.mysock.mysendline("----------------")
        if self.logger:
            self.logger.info(f"Round ended: {round_stat}")

    def _get_round_stat(self, opponent: BasePlayer) -> str:
        sums: list[int] = [0, 0]
        for v1, v2 in zip(opponent.decisions, self.decisions):
            points = get_points(v1, v2)
            sums[0] += points[0]
            sums[1] += points[1]
        return Formatter.format_round(
            player1_name=opponent.display_name,
            player2_name="You",
            decisions1=opponent.decisions,
            decisions2=self.decisions,
            sums1=sums[0],
            sums2=sums[1]
        )

    def _get_phrase(self, opponent: BasePlayer) -> str:
        phrase = ""
        for _ in range(5):
            if self.decisions[-1] == opponent.decisions[-1] == Decision.Cooperate:
                phrase = choice(self.game_env.c_c_texts)
            elif self.decisions[-1] == opponent.decisions[-1] == Decision.Defect:
                phrase = choice(self.game_env.d_d_texts)
            elif self.decisions[-1] == Decision.Cooperate and opponent.decisions[-1] == Decision.Defect:
                phrase = choice(self.game_env.c_d_texts)
            elif self.decisions[-1] == Decision.Defect and opponent.decisions[-1] == Decision.Cooperate:
                phrase = choice(self.game_env.d_c_texts)
            
            if phrase != self.last_phrase:
                self.last_phrase = phrase
                break

        return phrase

    def turn(self, opponent: BasePlayer, iteration: int = 0) -> AnyDecisionType:
        self.mysock.mysendline(NEWLINE + self._get_round_stat(opponent))
        if iteration > 0 and randint(0,100) < 5:
            phrase = self._get_phrase(opponent)
            if phrase:
                self.mysock.mysendline(phrase)
        while True:
            self.mysock.mysend("Your turn: ")
            cmd = self.mysock.myrecv()
            if self.logger:
                self.logger.debug(f"Player said: {repr(cmd)}")
            match cmd.strip():
                case "C":
                    return Decision.Cooperate
                case "D":
                    return Decision.Defect
                case "Q":
                    return SocketDecision.Quit
                case "":
                    pass
                case _:
                    self.mysock.mysendline(f"Unknown command. Please, use one of: {[e.value for e in Decision]+[e.value for e in SocketDecision]}")
