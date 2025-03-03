import random

import stats
import settings
from custom_mechanics import skills
from custom_mechanics import effects

def loadComputerEnemySkills():
    for i in range(5):
        selectedSkill = 0
        pickedSkills = []
        if i == 0:
            selectedSkill = 1
            pickedSkills.append(1)
        else: 
            while True:
                selectedSkill = random.randint(2, 7)
                if selectedSkill in pickedSkills:
                    continue
                else:
                    pickedSkills.append(selectedSkill)
                    break
                
        match(selectedSkill):
            case 1:
                stats.player02.skills[i] = skills.Basic_Attack()
                stats.player02.skills[i].assignTarget(stats.player01, stats.player02)
            case 2:
                stats.player02.skills[i] = skills.Heal()
                stats.player02.skills[i].assignTarget(stats.player02)
            case 3:
                stats.player02.skills[i] = skills.Amplify()
                stats.player02.skills[i].assignTarget(stats.player02)
            case 4:
                stats.player02.skills[i] = skills.Defense()
                stats.player02.skills[i].assignTarget(stats.player02)
            case 5:
                stats.player02.skills[i] = skills.Burn()
                stats.player02.skills[i].assignTarget(stats.player01, stats.player02)
            case 6:
                stats.player02.skills[i] = skills.Weaken()
                stats.player02.skills[i].assignTarget(stats.player01, stats.player02)
            case 7:
                stats.player02.skills[i] = skills.Energize()
                stats.player02.skills[i].assignTarget(stats.player02)
            case 8:
                stats.player02.skills[i] = skills.Strengthen()
                stats.player02.skills[i].assignTarget(stats.player02)
                
def randomOpponentSkillSelect():
    while True:
        enemyChoice = random.randint(1, 5)
        match(enemyChoice):
            case 1:
                if stats.player02.energy >= getattr(stats.player02.skills[0], "energyCost", 0) and stats.player02.skills[0].name not in [getattr(x, "skillname", "") for x in effects.effectList]: 
                    stats.player02.skills[0].action()
                    settings.recentOpponentMove = stats.player02.skills[0]
                    break
            case 2:
                if stats.player02.energy >= getattr(stats.player02.skills[1], "energyCost", 0) and stats.player02.skills[1].name not in [getattr(x, "skillname", "") for x in effects.effectList]: 
                    stats.player02.skills[1].action()
                    settings.recentOpponentMove = stats.player02.skills[1]
                    break
            case 3:
                if stats.player02.energy >= getattr(stats.player02.skills[2], "energyCost", 0) and stats.player02.skills[2].name not in [getattr(x, "skillname", "") for x in effects.effectList]: 
                    stats.player02.skills[2].action()
                    settings.recentOpponentMove = stats.player02.skills[2]
                    break
            case 4:
                if stats.player02.energy >= getattr(stats.player02.skills[3], "energyCost", 0) and stats.player02.skills[3].name not in [getattr(x, "skillname", "") for x in effects.effectList]: 
                    stats.player02.skills[3].action()
                    settings.recentOpponentMove = stats.player02.skills[3]
                    break
            case 5:
                if stats.player02.energy >= getattr(stats.player02.skills[4], "energyCost", 0) and stats.player02.skills[4].name not in [getattr(x, "skillname", "") for x in effects.effectList]: 
                    stats.player02.skills[4].action()
                    settings.recentOpponentMove = stats.player02.skills[4]
                    break