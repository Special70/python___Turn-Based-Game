import system_lib as syslib
import locale_EN as lang
import settings
import stats
import skills

import os
import time
import random

def mainMenuSystem():
    while True:
        match (syslib.currentKey):
            case "E": # Exit Program
                syslib.programStatus = False
                break
            case "S": # Settings
                os.system('cls')
                settingsEditor()
            case "P": # Play
                syslib.currentMenu = 2
                break
            

# =================[Settings]=================
# =================[Settings]=================
# =================[Settings]=================
def settingsEditor():
    lang.settings_page01()
    while True:
        match (syslib.currentKey):
            case "B":
                os.system('cls')
                lang.mainMenu_startMsg_1()
                break
            case "K":
                syslib.mainMenuLoop1_settings_keybindEditor = True
                settingsKeyBindEditor()

def settingsKeyBindEditor():
    syslib.editorMode = True # Enable editor mode of keyListener
    os.system('cls')
    lang.settings_page01_keybindEditor()
    # Grabs each key in the keybind dictionary
    keyOfKeybinds = [key for key in settings.keybinds]
    while syslib.mainMenuLoop1_settings_keybindEditor:
        keypress = syslib.currentKey # Constantly checks what the user has pressed
        match (keypress): # Once it hits any of the cases below, it will save the value for the first case
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9": # To select what keybind to edit
                os.system('cls')
                lang.settings_page01_keybindEditor_selectKeybind(keyOfKeybinds[int(keypress)])
                syslib.currentKey = ""
                while True: # Waits for the user to press anything to change the keybind value
                    if syslib.currentKey != "":                                    
                        settings.keybinds[keyOfKeybinds[int(keypress)]] = syslib.currentKey
                        os.system('cls')
                        lang.settings_page01_keybindEditor()
                        syslib.editorMode = False
                        break
            case "B":
                keypress = ""
                syslib.currentKey = ""
                os.system('cls')
                syslib.mainMenuLoop1_settings_keybindEditor = False
                lang.settings_page01()
                
# =================[Game Selector]=================
# =================[Game Selector]=================
# =================[Game Selector]=================

def gameSelectorMenu(): # Used at main.py
    while True:
        match(syslib.currentKey):
            case "B": # Back
                syslib.currentMenu = 1
                break
            case "M": # Multiplayer
                # For refreshing default stats
                stats.player01 = stats.Player("Player 1")
                stats.player02 = stats.Player("Player 2")
                
                os.system('cls')
                gameSelectorMenu_multiplayerMenu()
                lang.gameSelector()
            case "O": # Singleplayer/AI
                pass
            
def gameSelectorMenu_multiplayerMenu():
    lang.gameSelector_multiplayerMenuDisplayNames()
    while True:
        match(syslib.currentKey):
            case "B": # Back
                os.system('cls')
                break
            case "W": # Move UP
                if settings.multiplayerMainMenu_arrowSelection.index('◄') > 0:
                    os.system('cls')
                    indexOfArrow = settings.multiplayerMainMenu_arrowSelection.index('◄')
                    settings.multiplayerMainMenu_arrowSelection[indexOfArrow] = ""
                    settings.multiplayerMainMenu_arrowSelection[indexOfArrow-1] = "◄"
                    lang.gameSelector_multiplayerMenuDisplayNames()
                    time.sleep(0.01)
            case "S": # Move DOWN
                if settings.multiplayerMainMenu_arrowSelection.index('◄') < len(settings.multiplayerMainMenu_arrowSelection)-1:
                    os.system('cls')
                    indexOfArrow = settings.multiplayerMainMenu_arrowSelection.index('◄')
                    settings.multiplayerMainMenu_arrowSelection[indexOfArrow] = ""
                    settings.multiplayerMainMenu_arrowSelection[indexOfArrow+1] = "◄"
                    lang.gameSelector_multiplayerMenuDisplayNames()
                    time.sleep(0.01)
            case "P": # Play
                os.system('cls')
                # Pick which of the two will make the first move:
                syslib.turnNumber = random.randint(1, 2)
                stats.loadPlayerKeybinds()
                multiplayerSession()
                break
            case "\R":
                syslib.editorMode = True # Forced to put this here due to some sussy programming bug
                time.sleep(0.01)
                gameSelectorMenu_multiplayerMenu_editor()
            
def exitSkillSelection():
    os.system('cls')
    lang.gameSelector_multiplayerMenuDisplayNames()
    syslib.currentKey = ""
    syslib.editorMode = False
            
def gameSelectorMenu_multiplayerMenu_editor():
    
    syslib.editorMode = True
    specifiedPlayer = stats.player01 if settings.multiplayerMainMenu_arrowSelection.index('◄') in [0, 1, 2, 3, 4, 5, 6, 7, 8] else stats.player02
    specifiedOppopent_of_Player = stats.player02 if settings.multiplayerMainMenu_arrowSelection.index('◄') in [0, 1, 2, 3, 4, 5, 6, 7, 8] else stats.player01 # To easily assign Player Class instance on skills
    currentIndex = settings.multiplayerMainMenu_arrowSelection.index('◄') if settings.multiplayerMainMenu_arrowSelection.index('◄') in [0, 1, 2, 3, 4, 5, 6, 7, 8] else settings.multiplayerMainMenu_arrowSelection.index('◄')-9
    if currentIndex < 4: # HP, ATK, DEF, ENERGY Value Editor
        os.system('cls')
        lang.textValue = str(getattr(specifiedPlayer, lang.nameOfBasicAttributes[currentIndex]))
        lang.gameSelector_multiplayerMenuDisplayNames_editorMsg(currentIndex)
        syslib.currentKey = "" # To not accidentally record the enter
        while True:
            if syslib.currentKey != "" and syslib.currentKey.isdigit(): # Adding numbers
                pressedKey = syslib.currentKey
                os.system('cls')
                lang.textValue += pressedKey
                lang.gameSelector_multiplayerMenuDisplayNames_editorMsg(currentIndex)
                syslib.currentKey = ""
            elif syslib.currentKey == "\X08" and len(lang.textValue) > 0: # Backspace Key
                os.system('cls')
                lang.textValue = lang.textValue[:len(lang.textValue)-1]
                lang.gameSelector_multiplayerMenuDisplayNames_editorMsg(currentIndex)
                syslib.currentKey = ""
            elif syslib.currentKey == "\R":
                if len(lang.textValue) <= 0:
                    lang.editorZeroValueError = "Invalid Input. Please type a valid input and try again"
                    os.system('cls')
                    lang.gameSelector_multiplayerMenuDisplayNames_editorMsg(currentIndex)
                    syslib.currentKey = ""
                else:   
                    os.system('cls')
                    setattr(specifiedPlayer, lang.nameOfBasicAttributes[currentIndex], int(lang.textValue))
                    lang.gameSelector_multiplayerMenuDisplayNames()
                    syslib.currentKey = ""
                    lang.textValue = ""
                    lang.editorZeroValueError = ""
                    syslib.editorMode = False
                    break
    else:
        os.system('cls')
        lang.gameSelector_multiplayerMenuDisplayNames_skillSelectorMsg("Skill #"+str(currentIndex-3))
        while True:
            match(syslib.currentKey):
                case "B": # Back / Choose nothing
                    exitSkillSelection()
                    break
                case "Q":
                    specifiedPlayer.skills[currentIndex-4] = skills.Basic_Attack()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedOppopent_of_Player)
                    exitSkillSelection()
                    break
            
            

# =================[Multiplayer PVP GAME SESSION]=================
# =================[Multiplayer PVP GAME SESSION]=================
# =================[Multiplayer PVP GAME SESSION]=================

def multiplayerSession():
    gameSession = True
    match (syslib.turnNumber):
        case 1:
            syslib.turnIdentifier = stats.player01
        case 2:
            syslib.turnIdentifier = stats.player02
    lang.gameSelector_multiplayerMenu_startGameTurn01(syslib.turnIdentifier)
    
    # Loading keybinds because compiler is being a bitch
    
    while True and gameSession: # Main Loop
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
                    syslib.turnIdentifier.skills[0].action()
                    print("Skill 1")
                case syslib.turnIdentifier.keybind2:
                    syslib.turnIdentifier.skills[1].action()
                    print("Skill 2")
                case syslib.turnIdentifier.keybind3:
                    syslib.turnIdentifier.skills[2].action()
                    print("Skill 3")
                    break
                case syslib.turnIdentifier.keybind4:
                    syslib.turnIdentifier.skills[3].action()
                    print("Skill 4")
                    break
                case syslib.turnIdentifier.keybind5:
                    syslib.turnIdentifier.skills[4].action()
                    print("Skill 5")
                    break
        
        os.system('cls')
        lang.gameSelector_multiplayerMenu_startGameTurn01(syslib.turnIdentifier)
        # Switches rounds
        match (syslib.turnNumber):
            case 1:
                syslib.turnNumber = 2
            case 2:
                syslib.turnNumber = 1
                
            