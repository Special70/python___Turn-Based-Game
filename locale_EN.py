import time
import settings

def mainMenu_startMsg_0():
    text = "Special70 Presents...."
    for i in range(len(text)):
        print(text[:i+1], end="\r")
        time.sleep(0.1)
        
def mainMenu_startMsg_1():
    text = '''
================================
Welcome to the Epic Turn-Based Game!

Press keybinds to select options!
► "P": Play
► "E": Exit
► "S": Settings
    '''
    print(text)
    
# =================[Settings Locale]=================
# =================[Settings Locale]=================
# =================[Settings Locale]=================

def settings_page01():
    text = '''
============================
Settings:

► "B": Back
► "K": Keybinds
    '''
    print(text)
    
def settings_page01_keybindEditor():
    text = '''
====================================
Keybinds:
<Select what keybind you want to press>
Player1 Keybinds:
► "0": {p1_choice1}
► "1": {p1_choice2}
► "2": {p1_choice3}
► "3": {p1_choice4}
► "4": {p1_choice5}

Player2 Keybinds: (For P1 vs P2 Mode)
► "5": {p2_choice1}
► "6": {p2_choice2}
► "7": {p2_choice3}
► "8": {p2_choice4}
► "9": {p2_choice5}

► "B": Back
    '''.format(
        p1_choice1 = settings.keybinds["p1choice1"],
        p1_choice2 = settings.keybinds["p1choice2"],
        p1_choice3 = settings.keybinds["p1choice3"],
        p1_choice4 = settings.keybinds["p1choice4"],
        p1_choice5 = settings.keybinds["p1choice5"],
        p2_choice1 = settings.keybinds["p2choice1"],
        p2_choice2 = settings.keybinds["p2choice2"],
        p2_choice3 = settings.keybinds["p2choice3"],
        p2_choice4 = settings.keybinds["p2choice4"],
        p2_choice5 = settings.keybinds["p2choice5"]
        )
    print(text)
    
def settings_page01_keybindEditor_selectKeybind(keybind):
    text = '''
Type any key to change the keybind for this specific keybind: {}
    '''.format(keybind)
    print(text)

# =================[Game Selector]=================
# =================[Game Selector]=================
# =================[Game Selector]=================