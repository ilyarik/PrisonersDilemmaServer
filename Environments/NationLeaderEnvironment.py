from .BaseEnvironment import BaseEnvironment


class NationLeaderEnvironment(BaseEnvironment):
    creature = "nation leader"
    creatures = "nation leaders"
    backstory = "You have to rule your nation to prosperity. You can do it via developing robust relationships with your neighbours, trading goods and establishing supply chains. " \
                +"In other words, to Cooperate (C). On the other hand, you can choose the way of brutal force and conquer the rivals enslaving their people and utilizing the resources. " \
                +"In other words, to Defect (D). The one who Defects (D) on Cooperation (C) gets a free win... for one turn. Both would lose on protracted mutual Defection (D). " \
                +"What path will you choose for your people? Your turn, Sovereign. "
    lose_text = BaseEnvironment.lose_text + [
        "You are a deadman and the disgrace of your people. Shame on you. ",
        "Your deeds will be purged from the pages of history. ",
        "You can still see their angry faces as they stormed the citadel. But you was dead found before they found you, and the condemn later was on its way. ",
        "Only successful leaders write history. "
    ]
    win_text = BaseEnvironment.win_text + [
        "Your people are thriving and you are writing history. How long will the peace last? ",
        "The lion cannot defend himself against snares and the fox cannot defend himself against wolves. Therefore, it is necessary to be a fox to discover the snares and a lion to terrify the wolves. "
    ]
    c_c_texts = BaseEnvironment.c_c_texts + [
        "Gilded icons and dogmatic rituals... for some, a tonic against the bloodshed. ",
        "Rarity and curios... sold at a profit of-course. ",
        "An increasing stockpile of curios trinkets... gathered from forbidden places. ",
        "Experimental techniques and tonics can overcome things a sharpened sword cannot. ",
        "Trinkets and charms, gathered from all-the-forgotten-corners of the earth. ",
        "Glittering gold, trinkets and baubles... Paid for in blood. ",
        "Darkness closes in, haunting the hearts of men. ",
        "Diplomacy is crucial in men relationships. "
    ]
    d_c_texts = BaseEnvironment.d_c_texts + [
        "Barbaric rage and unrelenting savagery make for a powerful ally. ",
        "Most will end up here, covered in a poisoned earth, awaiting merciful oblivion. ",
        "Make no mistake; we will face ever greater threat - our soldiers must be ready. ",
        "Aha-ha-ha-ha! Let those dirty beasts worship the mud now. ",
        "Room by room, hall by hall, we reclaim what is ours. ",
        "Their squeals fade, their confident is shaken. ",
        "The most contrarian thing of all is not to oppose the crowd but to think for yourself. "
    ]
    c_d_texts = BaseEnvironment.c_d_texts + [
        "I remember days when the sun shone, and laughter could be heard from the tavern. ",
        "An ambushed! Send these vermin a message; the rightful owner has returned and their kind is no longer welcome. ",
        "Such a terrible assault cannot be left unanswered. ",
        "Failure tests the metal of heart, brain, and body. "
    ]
    d_d_texts = BaseEnvironment.d_d_texts + [
        "What better laboratory than a blood-soaked battlefield? ",
        "Fan the flames, mould the metal; we are raising an army. ",
        "The frontline of this war is not in the dungeon, but rather inside the mind. ",
        "The bellows blasts once again, the forge stands ready to make weapons of war. ",
        "Frustration and fury! More destructive than a hundred cannons. ",
        "More blood soaks the soil... feeding the evil they're in. "
    ]