from enum import Enum


class Decision(Enum):
    Cooperate = "C"
    Defect = "D"


class SocketDecision(Enum):
    Quit = "Q"


AnyDecisionType = Decision|SocketDecision


WEIGHTS: list[list[int]] = [[3,3], [5,0], [0,5], [1,1]] # [[C,C], [D,C], [C,D], [D,D]]


def get_points(v1: AnyDecisionType, v2: AnyDecisionType) -> list[int]:
    if isinstance(v1, SocketDecision) \
    or isinstance(v2, SocketDecision):
        return [0, 0]
        
    match (v1, v2):
        case Decision.Cooperate, Decision.Cooperate:
            return WEIGHTS[0]
        case Decision.Defect, Decision.Cooperate:
            return WEIGHTS[1]
        case Decision.Cooperate, Decision.Defect:
            return WEIGHTS[2]
        case Decision.Defect, Decision.Defect:
            return WEIGHTS[3]
        case _:
            raise NotImplementedError()

