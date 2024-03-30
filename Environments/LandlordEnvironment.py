from .BaseEnvironment import BaseEnvironment


class LandlordEnvironment(BaseEnvironment):
    creature = "landlord"
    creatures = "landlords"
    backstory = "You have opulent possessions in your domain. Your closes neighbours aren't agreed to admit your legitimacy on your lands. " \
                +"Rule the business on the lands that are yours and achieve prosperity despite the envy conspirators around you. " \
                +"Choose the strategy how you are going to achieve that. Will you try to Cooperate (C) with the neighbours in a hope of them admitting your sovereign on the lands? " \
                +"Or you can Defecting (D) knitting political intrigues, blackmailing and corrupting the statesmen to weaken their lord families. " \
                +"Spoiling life to each others won't benefic anyone. "
    lose_text = BaseEnvironment.lose_text + [
        "You was lord of this place, before the crows and rats made it their domain. ",
        "Our family name once so well-regarded is now barely whispered aloud by decent folk. ",
        "A Lannister always pays his debts. "
    ]
    win_text = BaseEnvironment.win_text + [
        "Courage taught you no matter how bad a crisis gets ... any sound investment will eventually pay off.",
        "Your diplomacy has led to prosperity of your lands, you have become the most powerful man in the kingdom. Your barns and treasury are full. "
    ]
    d_c_texts = BaseEnvironment.d_c_texts + [
        "Even the aged oak will fall to the tempest's winds. ",
        "To fall for such a little thing - a bite of bread. ",
        "Know what you own, and know why you own it. "
    ]
    c_d_texts = BaseEnvironment.c_d_texts + [
        "Twisted and maniacal - a sluddering testament to the power of corruption. ",
        "Knowing hunger sets in, turning the body against itself, weakening the mind... ",
        "To fall for such a little thing - a bite of bread. ",
        "Driving out corruption is an endless battle, but one that must be fought. ",
        "The sin is not in being outmatched - but failing to recognize it. ",
    ]
    c_c_texts = BaseEnvironment.c_c_texts + [
        "Once our estate was the envy of this land. ", 
        "A little hope, however desperate is never without worth. ",
        "All-manner of diversion and dalliance await those cross the threshold with coin in hand. ",
        "The cobwebs had been dusted; the pews set straight... the abbey calls to the faithful. ",
        "To those with a keen eye, gold gleams like a dagger's point. ",
        "Shimmering golds for both of us. ",
        "Glittering gold, trinkets and baubles... Paid for in blood. ",
        "Diplomacy is crucial in men relationships. "
    ]
    d_d_texts = BaseEnvironment.d_d_texts + [
        "He will be laughing still... at the end. ",
        "This man understands that adversity and existence... are one and the same. "
    ]