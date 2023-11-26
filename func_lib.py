import system_lib as syslib
import locale_EN as lang
import settings
import stats

import os
import msvcrt
import time

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
    keypress = ""
    os.system('cls')
    lang.settings_page01_keybindEditor()
    # Grabs each key in the keybind dictionary
    keyOfKeybinds = [key for key in settings.keybinds]
    while syslib.mainMenuLoop1_settings_keybindEditor:
        keypress = str(msvcrt.getch()).split("'")[1].upper()
        match (keypress):
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                syslib.disableKeyListener = True
                os.system('cls')
                lang.settings_page01_keybindEditor_selectKeybind(keyOfKeybinds[int(keypress)])
                settingsKeyBindEditor_setupKeybind(keyOfKeybinds[int(keypress)])
                keypress = "" # Answer Clearer
            case "B":
                keypress = ""
                syslib.currentKey = ""
                os.system('cls')
                syslib.mainMenuLoop1_settings_keybindEditor = False
                lang.settings_page01()

# NOTE: The current main.keyListener() is not compatible with this design as it instantly clears the syslib.currentKey variable's value upon giving it a value and it's too fast for the function to capture any values, giving this function its own keypress reader
def settingsKeyBindEditor_setupKeybind(x):
    while True:
        if msvcrt.kbhit():
            keypress = str(msvcrt.getch()).split("'")[1].upper()
            settings.keybinds[x] = keypress
            os.system('cls')
            lang.settings_page01_keybindEditor()
            syslib.disableKeyListener = False
            break
            
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
            case "S": # Move DOWN
                if settings.multiplayerMainMenu_arrowSelection.index('◄') < len(settings.multiplayerMainMenu_arrowSelection)-1:
                    os.system('cls')
                    indexOfArrow = settings.multiplayerMainMenu_arrowSelection.index('◄')
                    settings.multiplayerMainMenu_arrowSelection[indexOfArrow] = ""
                    settings.multiplayerMainMenu_arrowSelection[indexOfArrow+1] = "◄"
                    lang.gameSelector_multiplayerMenuDisplayNames()
            case "P": # Play
                os.system('cls')
                lang.gameSelector_multiplayerMenu_startGameTurn01()
                multiplayerSession()
                break

def multiplayerSession():
    gameSession = True
    while True and gameSession:
        match (syslib.currentKey):
            case "Q":
                os.system('cls')
                print("Are you sure? Y/N")
                while True:
                    match (syslib.currentKey):
                        case "N":
                            os.system('cls')
                            lang.gameSelector_multiplayerMenu_startGameTurn01()
                            break
                        case "Y":
                            os.system('cls')
                            gameSession = False
                            break
            