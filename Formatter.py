from Decision import AnyDecisionType
from MySocket import NEWLINE


class Formatter:
    @staticmethod
    def format_round(player1_name: str, player2_name: str, decisions1: list[AnyDecisionType], decisions2: list[AnyDecisionType], sums1: int, sums2: int) -> str:
        if len(decisions1) > 80 and len(decisions2) > 80:
            decisions1_str = "".join([d.value for d in decisions1[:40]]) + "..." + "".join([d.value for d in decisions1[-40:]])
            decisions2_str = "".join([d.value for d in decisions2[:40]]) + "..." + "".join([d.value for d in decisions2[-40:]])
        else:
            decisions1_str = "".join([d.value for d in decisions1])
            decisions2_str = "".join([d.value for d in decisions2])

        max_name_length: int = max(len(player1_name), len(player2_name))
        player1_name_indents: str = " "*(max_name_length - len(player1_name))
        player2_name_indents: str = " "*(max_name_length - len(player2_name))
        
        msg = ""
        msg = player1_name + player1_name_indents + " " + decisions1_str
        msg += " " + str(sums1) + NEWLINE
        msg += player2_name + player2_name_indents + " " + decisions2_str
        msg += " " + str(sums2) + NEWLINE
        return msg

    @staticmethod
    def format_results(players: dict) -> str:
        max_name_length: int = max(len(p.display_name) for p in players)
        max_score: int = max(s for s in players.values())
        msg = ""
        for player in sorted(players, key=lambda p: players[p], reverse=True):
            player_name_indent: str = " "*(max_name_length - len(player.display_name))
            score_bar: str = "#"*int(100*players[player]/max_score)
            msg += f"{player.display_name}{player_name_indent} {score_bar} {players[player]}{NEWLINE}"
        return msg
