from .BaseEnvironment import BaseEnvironment


class BrokerEnvironment(BaseEnvironment):
    creature = "real estate broker"
    creatures = "real estate brokers"
    backstory = "You live in a medieval kingdom. Your job is to make deals on houses. " \
                +"You can try to Defect (D) and steal clients from your rivaling colleagues, but the colleagues will not be happy and they will probably Defect (D) back. " \
                +"When you both Defect (D), clients get irritated, because no one likes annoying salesmen and quarrels, some clients will be gone. " \
                +"If only one Defects (D), he can get away with it and serve an additional client, if the opponent brokers tried to Cooperate (C). " \
                +"Alternatively, if you both Cooperate (C), each of you gets the same moderate income from the deals. " \
                +"Who is the biggest fish and who will become a medieval Barren Wuffet? "
    lose_text = BaseEnvironment.lose_text + [
        "There's always a bigger fish. ",
        "You died in poverty after your debts became unbearable. ",
        "Only losing everything we gain freedom. "
    ]
    win_text = BaseEnvironment.win_text + [
        "A smart strategy is the condition of success. ",
        "What do you say to this, Melon Tusk? ",
        "The life is a theater of tragicomedy and the market is the scene of this theater. You were successful on it and you are getting all the applauds today. "
    ]
    c_c_texts = BaseEnvironment.c_c_texts + [
        "Shimmering golds for both of us. ",
        "Good deals is a mutual interest. "
    ]
    c_d_texts = BaseEnvironment.c_d_texts + [
        "The sin is not in being outmatched - but failing to recognize it. ",
        "Be fearful when others are greedy. Be greedy when others are fearful."
    ]
    d_c_texts = BaseEnvironment.d_c_texts + [
        "To those with a keen eye, gold gleams like a dagger's point. ",
        "Illusive. Evasive. Persistent. Righteous traits for a swindler. ",
        "Cruel machinations spring to life... with a singular purpose. ",
    ]
    d_d_texts = BaseEnvironment.d_d_texts + [
        "The human-mind... fragile, like a robin's egg. ",
        "The mind cannot hope to withstand such an assault. "
    ]