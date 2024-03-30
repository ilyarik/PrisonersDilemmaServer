from .BaseEnvironment import BaseEnvironment


class LemmingEnvironment(BaseEnvironment):
    creature = "lemming"
    creatures = "lemmings"
    backstory = "You live in a big family where everyone has his unique role. However, rivalry is a thing within family ties. " \
                +"When you cooperate (C) and your opponent cooperates (C) you both get a decent amount of food and drinks. " \
                +"If you defect (D) during your hunts while your opponent tried to cooperate (C) you have a chance to get away with all the food and drinks. " \
                +"However, if your opponent is the one who defected (D) on you trying to cooperate (C) then he gets everything. " \
                +"Finally, if you both decided to trick each other, you both eat crumbs. Will you be able to survive in this ruthless world? "
    lose_text = BaseEnvironment.lose_text + [
        "You're not the smartest lemming in the world. Your siblings survived and you did not. ",
        "The laws of nature doesn't favour to the week ones. ",
        "Nature doesn't favour to weak lemmings. "
    ]
    win_text = BaseEnvironment.win_text + [
        "You will have a chance to pass on your genes to the ancestors of future generations. ",
        "Successful hunters win, the failed ones - lost in the grass. "
    ]
    c_c_texts = BaseEnvironment.c_c_texts + [
        "The thrill of the hunt... the promise of payment. ",
        "Strong drink, a game of chance, and companionship... the rush of life. ",
        "Loyal mates and a trembling prey are the ones a predator needs. "
    ]
    c_d_texts = BaseEnvironment.c_d_texts + [
        "Fear and frailty finally claim their due. ",
        "Perched at the very precipice of oblivion. ",
        "Even the colds stone seems bent on preventing passage. ",
        "Wounds to be tended, lessons to be learned. ",
        "No force of will can overcome a failing body. "
    ]
    d_d_texts = BaseEnvironment.d_d_texts + [
        "Those who covet injury, find it in no short-supply. ",
        "As life ebbs, terrible vistas of emptiness reveal themselves. "
    ]
    d_c_texts = BaseEnvironment.d_c_texts + [
        "Daze. Reeling. About to break... ",
        "The requirements of survival cannot be met on an empty stomach. ",
    ]
    
