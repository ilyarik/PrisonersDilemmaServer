from .BaseEnvironment import BaseEnvironment


class RaiderEnvironment(BaseEnvironment):
    creature = "raider"
    creatures = "raiders"
    backstory = """Your adventure led you to an old city of cursed gossips. 
This place is swarming of terrible creatures dominating this Godforsaken lands. 
These creatures, made from the slime and rotten flesh of their victims, exude an animalistic hatred of all living things. 
And in the center of this place - the lord of these creatures and the scariest one. 
It is... a travesty - a blundering mountain of hatred... and rage. Beacons in the darkness, stars in the emptiness of the void. 
A sickened, sensitive shadow writhing in hands that are not hands, and whirled blindly past ghastly midnights of rotting creation, corpses of dead worlds with sores that were cities, charnel winds that brush the pallid stars and make them flicker low. 
Beyond the worlds vague ghosts of monstrous things; half-seen columns of unsanctified temples that rest on nameless rocks beneath space and reach up to dizzy vacua above the spheres of light and darkness. 
And through this revolting graveyard of the universe the muffled, maddening beating of drums, and thin, monotonous whine of blasphemous flutes from inconceivable, unlighted chambers beyond Time; 
the detestable pounding and piping whereunto dance slowly, awkwardly, and absurdly the gigantic, tenebrous ultimate gods—the blind, voiceless, mindless gargoyles whose soul is Nyarlathotep. 
Malkavian creature of tremendous size radiates antediluvian horror. Your companions felt uneasy even thinking about a contact to this creature. 
During the suicidal attempt to achieve and slay this horrible creature you can either Defect (D) or Cooperate (C) with your companions. 
If both of you Cooperate (C) you maximize your chances to survival lowering the risk being ambushed or being hit from the back. 
If any one of you is Defecting (D), the other will likely be perished in the abyss, the survivor likely gets away with all the reward... if there's any.
In condition where both decided to Defect (D) and betray the companion, the Malkavian creatures will overcome your combat skills. 
Will you manage to survive at this great peril?"""
    lose_text = BaseEnvironment.lose_text + [
        "Another soul battered and broken, cast aside like a spent torch. ",
        "Another life wasted in the pursuit of glory and gold. ",
        "You died. And now... the darkness holds dominion - black as death. ",
        "You died silently in a dark puddle of mud. The thing is even more horrible than death. Liquefaction cannot come soon enough. ",
        "You died. More bones returned to rest - devils remanded to their abyss. "
    ]
    win_text = BaseEnvironment.win_text + [
        "Even reanimated bones can fall. Even the dead... can die again. ",
        "The match is struck, a star is born. ",
        "The bigger the beast. The greater the glory. "
    ]
    d_c_texts = BaseEnvironment.d_c_texts + [
        "Alone in the woods or tunnels, survival is the same. Prepare, persist, and overcome. ",
        "They must learn more than brutal blood-letting - they must learn to survive. ",
        "More arrive... foolishly seeking fortune and glory, in this domain of the damned. ",
        "Leave nothing unchecked, there is much to be found in forgotten places. ",
        "The cost of preparedness measured now in gold... later in blood. ",
        "Self-preservation is paramount at any cost! ",
        "Terrors may indeed stalk these shadows, but yonder - a glint of gold. ",
        "The most contrarian thing of all is not to oppose the crowd but to think for yourself. "
    ]
    c_d_texts = BaseEnvironment.c_d_texts + [
        "Every creature has a weakness - the wise hero trains for what he will face. ",
        "This is no place for the weak or the foolhardy. ",
        "Staying on the brink, facing the abyss. ",
        "Cornered, trapped, and force to fight on! ",
        "No chance for egress, will this be a massacre? ",
        "The sin is not in being outmatched - but failing to recognize it. ",
        "There can be no bravery without madness. ",
        "Ambushed by foul conspiracy! ",
    ]
    c_c_texts = BaseEnvironment.c_c_texts + [
        "To fight the abyss... one must to know it. ",
        "In the end every plan relies upon a strong arm and tempered steel. ",
        "A sharper sword, a stronger shield - anything to prolong a soldier's life. ",
        "Success depends on survival. ",
        "Great heroes can be found even here - in the mud and rain. ",
        "And now the true test. Hold fast! Or expire. ",
        "Regroup! Reassemble! Evil is... timeless after-all. ",
        "Good fortune and hard work may yet arrests this plague. ",
        "Together we are the flame! "
    ]
    d_d_texts = BaseEnvironment.d_d_texts + [
        "A strict regimen is paramount if one is to master the brutal arithmetic of combat. ",
        "A mecca of madness and morbidity... your work begins. ",
        "Where for heroism? ",
        "Survival is a tenuous proposition... in this sprawling tomb. ",
        "Injury and despondent set the stage for heroism... or cowardice. ",
        "True desperation is known, only when escape is impossible. ",
        "The darkness holds much worst than mere trickery... and boogeymen. ",
        "Darkness closes in, hunting the hearts of men. ",
        "A moment of valour shines brightest against the backdrop of despair. ",
        "Huddled together, furtive and vulnerable - rats in a maze. ",
        "Darkness closes in, haunting the hearts of men. ",
        "There can be no hope in this hell, no hope at all. ",
        "The oldest and strongest emotion of mankind is fear, and the oldest and strongest kind of fear is fear of the unknown. "
    ]