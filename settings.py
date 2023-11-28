import system_lib
import locale_EN as lang
import settings
import os
import stats

arrowSelection = ['◄','','','','','','','','' ,'','','','','','','','',''] 
arrowSelectionMaxIndex = 17 # Made to be adjustable to prevent singleplayer editor from selecting Opponent AI skills

recentOpponentMove = "None" # Used for singleplayer to let the user know what the computer randomly picked
# Variable below is for the keybind editor
keybinds = {
    "p1choice1": "A",
    "p1choice2": "S",
    "p1choice3": "D",
    "p1choice4": "F",
    "p1choice5": "G",
    
    "p2choice1": "7",
    "p2choice2": "8",
    "p2choice3": "9",
    "p2choice4": "4",
    "p2choice5": "6",
}

def loadPlayerKeybinds():
    stats.player01.keybind1 = settings.keybinds["p1choice1"]
    stats.player01.keybind2 = settings.keybinds["p1choice2"]
    stats.player01.keybind3 = settings.keybinds["p1choice3"]
    stats.player01.keybind4 = settings.keybinds["p1choice4"]
    stats.player01.keybind5 = settings.keybinds["p1choice5"]
    stats.player02.keybind1 = settings.keybinds["p2choice1"]
    stats.player02.keybind2 = settings.keybinds["p2choice2"]
    stats.player02.keybind3 = settings.keybinds["p2choice3"]
    stats.player02.keybind4 = settings.keybinds["p2choice4"]
    stats.player02.keybind5 = settings.keybinds["p2choice5"]
    
