import system_lib as syslib
import locale_EN as lang
import stats
import settings
from custom_mechanics import effects
from gamemodes import computer_opponent

import os

# Setting up keybinds manually because class instances have a chance to have seizures during key spam

def multiplayerSession():
    gameSession = True
    # Loading keybinds because compiler is being a bitch
    settings.loadPlayerKeybinds()
    effects.effectList = [] # Resetting effects
    
    
    # Randomizing Opponent Skills if gamemode is singleplayer
    if syslib.gamemode == "singleplayer":
        computer_opponent.loadComputerEnemySkills()
    while True and gameSession: # Main Loop
        # ▼▼▼ Put effect start loader here
        effects.effectLoaderStart()
        if syslib.gamemode == "multiplayer":
            match (syslib.turnNumber): 
                case 1:
                    syslib.turnIdentifier = stats.player01
                case 2:
                    syslib.turnIdentifier = stats.player02
        else:
            syslib.turnIdentifier = stats.player01
        lang.gameSelector_multiplayerMenu_startGameTurn01(syslib.turnIdentifier)
        while True: # Listens for key inputs
            match (syslib.currentKey):
                case "Q": # Quit
                    os.system('cls')
                    print("Are you sure? Y/N")
                    confirmBool = False
                    while True:
                        match (syslib.currentKey):
                            case "N": # No
                                os.system('cls')
                                lang.gameSelector_multiplayerMenu_startGameTurn01(syslib.turnIdentifier)
                                break
                            case "Y": # Yes
                                os.system('cls')
                                gameSession = False
                                confirmBool = True
                                break
                    if confirmBool:
                        break
                # Enter Skill
                case syslib.turnIdentifier.keybind1:
                    if syslib.turnIdentifier.energy >= getattr(syslib.turnIdentifier.skills[0], "energyCost", 0) and syslib.turnIdentifier.skills[0].name not in [getattr(x, "skillname", "") for x in effects.effectList if x.target.name == syslib.turnIdentifier.name]:
                        syslib.turnIdentifier.skills[0].action()
                        break
                case syslib.turnIdentifier.keybind2:
                    if syslib.turnIdentifier.energy >= getattr(syslib.turnIdentifier.skills[1], "energyCost", 0) and syslib.turnIdentifier.skills[1].name not in [getattr(x, "skillname", "") for x in effects.effectList if x.target.name == syslib.turnIdentifier.name]:
                        syslib.turnIdentifier.skills[1].action()
                        break
                case syslib.turnIdentifier.keybind3:
                    if syslib.turnIdentifier.energy >= getattr(syslib.turnIdentifier.skills[2], "energyCost", 0) and syslib.turnIdentifier.skills[2].name not in [getattr(x, "skillname", "") for x in effects.effectList if x.target.name == syslib.turnIdentifier.name]: 
                        syslib.turnIdentifier.skills[2].action()
                        break
                case syslib.turnIdentifier.keybind4:
                    if syslib.turnIdentifier.energy >= getattr(syslib.turnIdentifier.skills[3], "energyCost", 0) and syslib.turnIdentifier.skills[3].name not in [getattr(x, "skillname", "") for x in effects.effectList if x.target.name == syslib.turnIdentifier.name]:
                        syslib.turnIdentifier.skills[3].action()
                        break
                case syslib.turnIdentifier.keybind5:
                    if syslib.turnIdentifier.energy >= getattr(syslib.turnIdentifier.skills[4], "energyCost", 0) and syslib.turnIdentifier.skills[4].name not in [getattr(x, "skillname", "") for x in effects.effectList if x.target.name == syslib.turnIdentifier.name]:
                        syslib.turnIdentifier.skills[4].action()
                        break
        os.system('cls')
        # Switches rounds
        if syslib.gamemode == "multiplayer":
            if int(syslib.turnNumber) == 1:
                syslib.turnNumber = 2
            elif int(syslib.turnNumber) == 2:
                syslib.turnNumber = 1
        else:
            computer_opponent.randomOpponentSkillSelect()
            
        if stats.player01.hp <= 0:
            os.system('cls')
            lang.multiplayerSession_dictateWhoWon(stats.player02)
            while True:
                if syslib.currentKey != "":
                    gameSession = False
                    os.system('cls')
                    break
        elif stats.player02.hp <= 0:
            os.system('cls')
            lang.multiplayerSession_dictateWhoWon(stats.player01)
            while True:
                if syslib.currentKey != "":
                    gameSession = False
                    os.system('cls')
                    break
            
        