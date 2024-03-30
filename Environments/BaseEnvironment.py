from abc import ABC


class BaseEnvironment(ABC):
    creature: str
    creatures: str # plural
    backstory: str
    # you Cooperate (C) and the opponent Cooperates (C)
    c_c_texts: list[str] = [
        "Affirmative actions. ",
        "Profitable for both of us. ",
        "A spark without kindling is a goal without hope. "
    ]
    # you Cooperate (C) and the opponent Defects (D)
    c_d_texts: list[str] = [
        "A setback, but not the end of things! ",
        "You will endure this lost and learn from it. ",
        "Adversity can foster hope, and resilience. ",
        "Remind yourself that overconfidence is a slow and insidious killer. ",
        "The biggest risk of all is not taking one. ",
    ]
    # you Defects (D) and the opponent Cooperates (C)
    d_c_texts: list[str] = [
        "A naive decision was to believe to such a sly prick you are. ",
        "Trust is built by ages and lost in a moment. ",
        "One has the profit when the other side didn't punish. "
    ]
    # you Defect (D) and the opponent Defects (D)
    d_d_texts: list[str] = [
        "Huh?! ",
        "Both of you lost on that decision. ",
    ]
    lose_text: list[str] = [
        "You died. Horribly...",
        "Life is a hideous thing, and from the background behind what we know of it peer demonical hints of truth which make it sometimes a thousandfold more hideous. "
    ]
    win_text: list[str] = [
        "Winner, winner, chicken dinner! "
    ]