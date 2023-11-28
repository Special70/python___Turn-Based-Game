import system_lib as syslib
import locale_EN as lang
import settings
import stats
from custom_mechanics import skills


import os
import time
import random
import sys

from gamemodes import multiplayer

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
        keypress = syslib.currentKey # Saves keypress
        match (keypress): # Uses keypress variable as reference for the code below
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9": # Checks if user pressed keys 0 to 9
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
                syslib.gamemode = "multiplayer"
                os.system('cls')
                gameSelectorMenu_statsEditorMenu()
                lang.gameSelector()
            case "O": # Singleplayer/AI
                stats.player01 = stats.Player("Player 1")
                stats.player02 = stats.Player("Player 2")
                syslib.gamemode = "singleplayer"
                os.system('cls')
                gameSelectorMenu_statsEditorMenu()
                lang.gameSelector()
            
def gameSelectorMenu_statsEditorMenu():
    if syslib.gamemode == "multiplayer":
        settings.arrowSelectionMaxIndex = 17
    elif syslib.gamemode == "singleplayer":
        settings.arrowSelectionMaxIndex = 12
    lang.gameSelector_statsEditorMenuDisplay()
    while True:
        match(syslib.currentKey):
            case "B": # Back
                os.system('cls')
                settings.arrowSelection = ['◄','','','','','','','','' ,'','','','','','','','',''] # To patch a bug where if you select the opponent skill selection in multiplayer then switch to singleplayer
                break
            case "W": # Move UP
                if settings.arrowSelection.index('◄') > 0:
                    os.system('cls')
                    indexOfArrow = settings.arrowSelection.index('◄')
                    settings.arrowSelection[indexOfArrow] = ""
                    settings.arrowSelection[indexOfArrow-1] = "◄"
                    lang.gameSelector_statsEditorMenuDisplay()
                    time.sleep(0.01)
            case "S": # Move DOWN
                if settings.arrowSelection.index('◄') < settings.arrowSelectionMaxIndex:
                    os.system('cls')
                    indexOfArrow = settings.arrowSelection.index('◄')
                    settings.arrowSelection[indexOfArrow] = ""
                    settings.arrowSelection[indexOfArrow+1] = "◄"
                    lang.gameSelector_statsEditorMenuDisplay()
                    time.sleep(0.01)
            case "P": # Play ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
                syslib.editorMode = False
                os.system('cls')
                # Pick which of the two will make the first move:
                syslib.turnNumber = random.randint(1, 2) # Decides who's gonna get the first turn
                multiplayer.multiplayerSession()
                break
            case "\R":
                syslib.editorMode = True # Forced to put this here due to some sussy programming bug
                time.sleep(0.01)
                gameSelectorMenu_multiplayerMenu_editor()
            
def exitSkillSelection():
    os.system('cls')
    lang.gameSelector_statsEditorMenuDisplay()
    syslib.currentKey = ""
    syslib.editorMode = False
            
def gameSelectorMenu_multiplayerMenu_editor():
    syslib.editorMode = True 
    specifiedPlayer = stats.player01 if settings.arrowSelection.index('◄') in [0, 1, 2, 3, 4, 5, 6, 7, 8] else stats.player02 
    specifiedOppopent_of_Player = stats.player02 if settings.arrowSelection.index('◄') in [0, 1, 2, 3, 4, 5, 6, 7, 8] else stats.player01 # To easily assign Player Class instance on skills
    currentIndex = settings.arrowSelection.index('◄') if settings.arrowSelection.index('◄') in [0, 1, 2, 3, 4, 5, 6, 7, 8] else settings.arrowSelection.index('◄')-9
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
                    lang.gameSelector_statsEditorMenuDisplay()
                    syslib.currentKey = ""
                    lang.textValue = ""
                    lang.editorZeroValueError = ""
                    syslib.editorMode = False
                    break
    else: # SKILL SELECTION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        os.system('cls')
        lang.gameSelector_multiplayerMenuDisplayNames_skillSelectorMsg("Skill #"+str(currentIndex-3))
        while True:
            match(syslib.currentKey):
                case "B": # Back / Choose nothing
                    exitSkillSelection()
                    break
                case "Q":
                    specifiedPlayer.skills[currentIndex-4] = skills.Basic_Attack()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedOppopent_of_Player, specifiedPlayer)
                    exitSkillSelection()
                    break
                case "W":
                    specifiedPlayer.skills[currentIndex-4] = skills.Heal()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedPlayer)
                    exitSkillSelection()
                    break
                case "E":
                    specifiedPlayer.skills[currentIndex-4] = skills.Amplify()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedPlayer)
                    exitSkillSelection()
                    break
                case "R":
                    specifiedPlayer.skills[currentIndex-4] = skills.Defense()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedPlayer)
                    exitSkillSelection()
                    break
                case "T":
                    specifiedPlayer.skills[currentIndex-4] = skills.Burn()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedOppopent_of_Player, specifiedPlayer)
                    exitSkillSelection()
                    break
                case "Y":
                    specifiedPlayer.skills[currentIndex-4] = skills.Weaken()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedOppopent_of_Player, specifiedPlayer)
                    exitSkillSelection()
                    break
                case "U":
                    specifiedPlayer.skills[currentIndex-4] = skills.Energize()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedPlayer)
                    exitSkillSelection()
                    break
                case "I":
                    specifiedPlayer.skills[currentIndex-4] = skills.Strengthen()
                    specifiedPlayer.skills[currentIndex-4].assignTarget(specifiedPlayer)
                    exitSkillSelection()
                    break
                    
                    
        
                
            