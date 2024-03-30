from Players.AllPlayers import *
from PrisonersGame import PrisonersGame
from Formatter import Formatter
from Decision import get_points
from itertools import combinations


if __name__=="__main__":
    players: dict[BasePlayer, int] = {
        TitForTatPlayer(): 0,
        TitForTatPlayer(): 0,
        TitForTatPlayer(): 0,
        TitForTwoTatsPlayer(): 0,
        TitForTwoTatsPlayer(): 0,
        TitForTwoTatsPlayer(): 0,
        TitForTwoTatsInARowPlayer(): 0,
        TitForTwoTatsInARowPlayer(): 0,
        TitForTwoTatsInARowPlayer(): 0,
        GrimTriggerPlayer(): 0,
        GrimTriggerPlayer(): 0,
        GrimTriggerPlayer(): 0,
        DowningPlayer(): 0,
        DowningPlayer(): 0,
        DowningPlayer(): 0,
        ResponsiveDowningPlayer(): 0,
        ResponsiveDowningPlayer(): 0,
        ResponsiveDowningPlayer(): 0,
        JossPlayer(): 0,
        JossPlayer(): 0,
        JossPlayer(): 0,
        TesterPlayer(): 0,
        TesterPlayer(): 0,
        TesterPlayer(): 0,
        TranquilizerPlayer(): 0,
        TranquilizerPlayer(): 0,
        TranquilizerPlayer(): 0,
        AlwaysDefectPlayer(): 0,
        AlwaysDefectPlayer(): 0,
        AlwaysDefectPlayer(): 0,
        AlwaysCooperatePlayer(): 0,
        AlwaysCooperatePlayer(): 0,
        AlwaysCooperatePlayer(): 0,
        RandomPlayer(): 0,
        RandomPlayer(): 0,
        RandomPlayer(): 0,
        FlexiblePlayer(): 0,
        FlexiblePlayer(): 0,
        FlexiblePlayer(): 0,
        StatisticPlayer(): 0,
        StatisticPlayer(): 0,
        StatisticPlayer(): 0
    }
    for player in players:
        player.display_name = player.__class__.__name__

    weights: list[list[int]] = [[3,3], [5,0], [0,5], [1,1]] # [[C,C], [D,C], [C,D], [D,D]]

    for player1, player2 in combinations(players, 2):
        game = PrisonersGame(player1, player2)
        game.play_round(iterations=100)
        sums: list[int] = [0,0]
        for v1, v2 in zip(player1.decisions, player2.decisions):
            points = get_points(v1, v2)
            sums[0] += points[0]
            sums[1] += points[1]
        players[player1] += sums[0]
        players[player2] += sums[1]
        print(Formatter.format_round(
            player1_name = player1.__class__.__name__, 
            player2_name = player2.__class__.__name__,
            decisions1 = player1.decisions,
            decisions2 = player2.decisions,
            sums1 = sums[0],
            sums2 = sums[1]
        ))

    print(Formatter.format_results(players))