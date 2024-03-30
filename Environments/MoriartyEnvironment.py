from .BaseEnvironment import BaseEnvironment


class MoriartyEnvironment(BaseEnvironment):
    creature = "network security specialist"
    creatures = "network security specialists"
    backstory = "Evil hacker Moriarty stole students' accounts and took control over the whole University. " \
                +"No news for a red or blueteamer: people and organizations can't keep secrets. " \
                +"The stolen credentials have been changed, only Moriarty has the access for now. " \
                +"He encrypted the files and even physical access wouldn't help to recover the stored information. " \
                +"However, the situation is not completely desperate. If you attack your University's infrastructure, " \
                +"get the access back in its running state, then you can recover the encryption codes. " \
                +"The University principals hired another specialists to multiply their chances to succeed. " \
                +"You can Cooperate (C) with them and distribute the necessary attack measures and the defense efforts among two. " \
                +"But the first proofed the recovered documents or databases fact would get the bonus tip from the principals. " \
                +"So, you can refuse to cooperate and Defect (D) on a particular step appropriating the success and claim the reward. The competitor wouldn't be happy after that. " \
                +"When both Defect (D) too often it would be barely possible to disrupt the villain plan. " \
                +"Who will become the most successful redteamer, who will get an offer and who will save the University from informational fiasco? "
    lose_text = BaseEnvironment.lose_text + [
        "There's always a bigger fish. ",
        "Most of the scientific works were lost. The principals blame you for this. ",
        "Another specialist tended to do a better job. He will have something to eat this month and you will not. ",
        "On the verge of ignorance and carelessness, any sharp mind will find something to profit from. The principals taught this lesson for sure. ",
        "Most people will assume everything is secure until provided strong evidence to the contrary. The principals taught this lesson for sure. "
    ]
    win_text = BaseEnvironment.win_text + [
        "You secured the breach and expelled the villain from the local data center. The principals have started haggling for your tip immediately. ",
        "The sneaky computer genius was caught before he could erase his tracks and was identified by security authorities. You've got offers from several reputable organizations. "
    ]
    c_c_texts = BaseEnvironment.c_c_texts + [
        "Low-tech attacks work. ",
        "We shouldn't worry about getting hacked, that's illegal. "
    ]
    c_d_texts = BaseEnvironment.c_d_texts + [
        "Security by obscurity will not give you the guarantees. ",
        "Give a man a zero-day and he'll have access for a day, teach a man to phish and he'll have access for life. ",
        "If you can't afford security, you can't afford a breach. "
    ]
    d_c_texts = BaseEnvironment.d_c_texts + [
        "The problem with common sense is that it is not all that common. ",
        "Don't put a $100 lock on a glass door. ",
        "People, the weakest link. "
    ]
    d_d_texts = BaseEnvironment.d_d_texts + [
        "The more money that can be made from defeating a technology, the more attacks, attackers, and hackers will appear. ",
        "The most secure computer is the computer that's off. "
    ]
