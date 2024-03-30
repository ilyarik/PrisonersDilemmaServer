from Environments.BaseEnvironment import BaseEnvironment
from Players.AllPlayers import *
from Environments.AllEnvironments import *
from Decision import SocketDecision, get_points, WEIGHTS
from PrisonersGame import PrisonersGame
from Formatter import Formatter
from MySocket import MySocket, NEWLINE
from threading import Thread
from typing import Callable, Mapping, Iterable, Any
from itertools import combinations
from math import comb
from random import choice, shuffle, randint
from traceback import format_exc
from time import sleep
from MyLogger import MyLogger


FLAG = "TEST"


class ClientThread(Thread):
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.mysock: MySocket = MySocket(args[0])
        address, port = args[0].getpeername()
        self.peername: str = f"{address}_{port}"

        self.game_env: BaseEnvironment = choice([
            LemmingEnvironment,
            BrokerEnvironment,
            LandlordEnvironment,
            NationLeaderEnvironment,
            RaiderEnvironment,
            MoriartyEnvironment
        ])()

        self.players: dict[BasePlayer, int] = {}
        bots = [
            RandomPlayer,
            DowningPlayer,
            GrimTriggerPlayer,
            FlexiblePlayer,
            ResponsiveDowningPlayer,
            JossPlayer,
            StatisticPlayer,
            TesterPlayer,
            TitForTatPlayer,
            TitForTwoTatsInARowPlayer,
            TitForTwoTatsPlayer,
            TranquilizerPlayer
        ]
        shuffle(bots)
        for i, bot_class in enumerate(bots):
            self.players[bot_class(display_name=f"Player {i}")] = 0
        self.socket_player = SocketPlayer(self.mysock, display_name="You", game_env = self.game_env)
        self.players[self.socket_player] = 0

        self.logger: MyLogger

    def _send_intro(self) -> None:
        self.mysock.mysendline(f"Imagine you are a {self.game_env.creature}. Your opponents will imagine they are {self.game_env.creatures} too. {self.game_env.backstory} ")
        self.mysock.mysendline("It's up to you to decide what to do. Cooperate (C) or Defect (D). Quit (Q) and try again. Score the most points to win. ")
        C_C = ",".join(str(w) for w in WEIGHTS[0])
        D_C = ",".join(str(w) for w in WEIGHTS[1])
        C_D = ",".join(str(w) for w in WEIGHTS[2])
        D_D = ",".join(str(w) for w in WEIGHTS[3])
        self.mysock.mysendline( "|---------|")
        self.mysock.mysendline( "|-Points:-|")
        self.mysock.mysendline( "|---------|")
        self.mysock.mysendline( "| | C | D |")
        self.mysock.mysendline( "|---------|")
        self.mysock.mysendline(f"|C|{C_C}|{C_D}|")
        self.mysock.mysendline(f"|D|{D_C}|{D_D}|")
        self.mysock.mysendline(f"|---------|{NEWLINE}")

    def run(self) -> None:
        """
        Initialise logger here and run the thread body
        """
        with MyLogger(self.peername) as logger:
            self.logger = logger
            self.socket_player.logger = logger
            self._run()

    def _run(self) -> None:
        """
        Work with the instance of MySocket here.
        """
        self._send_intro()

        rounds_played: int = 0
        
        self.logger.info(f"Start playing {comb(len(self.players), 2)} rounds")
        for player1, player2 in combinations(self.players, 2):
            round_length: int = 100 + randint(-10,10)
            try:
                PrisonersGame(player1, player2).play_round(iterations=round_length)
            except TimeoutError:
                self.logger.info(f"Timeouted or closed from client. ")
                self.mysock.mysendline(f"{NEWLINE}Too late... Nature will not forgive moments of timidity. ")
                break
            except BrokenPipeError:
                self.logger.info(f"Disconnected from client. ")
                break
            except Exception:
                self.logger.error(f"Got exception: {NEWLINE}{format_exc()}")
                break

            sums: list[int] = [0,0]
            for v1, v2 in zip(player1.decisions, player2.decisions):
                points = get_points(v1, v2)
                sums[0] += points[0]
                sums[1] += points[1]
            self.players[player1] += sums[0]
            self.players[player2] += sums[1]
 
            if SocketDecision.Quit == player1.decisions[-1] or SocketDecision.Quit == player2.decisions[-1]:
                break
            rounds_played += 1
            
        sleep(.1)
        if comb(len(self.players), 2) == rounds_played:
            msg = f"Results: {NEWLINE}{Formatter.format_results(self.players)}"
            self.mysock.mysendline(msg)
            if self.logger:
                self.logger.info(msg)
            if sorted(self.players, key=lambda p: self.players[p], reverse=True)[0] == self.socket_player:
                self.mysock.mysendline(f"Congratulations! {choice(self.game_env.win_text)}")
                self.mysock.mysendline(f"Flag is {FLAG}")
            else:
                self.mysock.mysendline(choice(self.game_env.lose_text))

        sleep(.1)
        self.logger.info(f"Closing socket... ")
        self.mysock.myclose("Bye")
