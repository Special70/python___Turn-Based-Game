import time
import settings

import stats
import skills

def mainMenu_startMsg_0():
    text = "Special70 Presents...."
    for i in range(len(text)):
        print(text[:i+1], end="\r")
        #time.sleep(0.1)
        
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

def gameSelector():
    text = '''
==============================
Select Gamemode:

► "M": Multiplay (P1 vs P2)

► "O": Computer Opponent (Singleplayer)

► "B": Back
    '''
    print(text)


# =================[Multiplayer PVP]=================
# =================[Multiplayer PVP]=================
# =================[Multiplayer PVP]=================

def gameSelector_multiplayerMenuDisplayNames():
    text = '''
==========================================
Press W/S button to move the select arrow
Press ENTER to confirm selection

Player01 Stats:
► HP: {p1_1} {select0}
► ATK: {p1_2} {select1}
► DEFENSE: {p1_3} {select2}
► ENERGY: {p1_4} {select3}
► Skills:
  ► {p1_5} {select4}
  ► {p1_6} {select5}
  ► {p1_7} {select6}
  ► {p1_8} {select7}
  ► {p1_9} {select8}

Player02 Stats:
► HP: {p2_1} {select9}
► ATK: {p2_2} {select10}
► DEFENSE: {p2_3} {select11}
► ENERGY: {p2_4} {select12}
► Skills:
  ► {p2_5} {select13}
  ► {p2_6} {select14}
  ► {p2_7} {select15}
  ► {p2_8} {select16}
  ► {p2_9} {select17}
  
► "P": Play
► "B": Back
    '''.format(
        p1_1 = stats.player01.hp,
        p1_2 = stats.player01.atk,
        p1_3 = stats.player01.defense,
        p1_4 = stats.player01.energy,
        
        p1_5 = stats.player01.skills[0],
        p1_6 = stats.player01.skills[1],
        p1_7 = stats.player01.skills[2],
        p1_8 = stats.player01.skills[3],
        p1_9 = stats.player01.skills[4],
        
        p2_1 = stats.player02.hp,
        p2_2 = stats.player02.atk,
        p2_3 = stats.player02.defense,
        p2_4 = stats.player02.energy,
        
        p2_5 = stats.player02.skills[0],
        p2_6 = stats.player02.skills[1],
        p2_7 = stats.player02.skills[2],
        p2_8 = stats.player02.skills[3],
        p2_9 = stats.player02.skills[4],
        
        select0 = settings.multiplayerMainMenu_arrowSelection[0],
        select1 = settings.multiplayerMainMenu_arrowSelection[1],
        select2 = settings.multiplayerMainMenu_arrowSelection[2],
        select3 = settings.multiplayerMainMenu_arrowSelection[3],
        select4 = settings.multiplayerMainMenu_arrowSelection[4],
        select5 = settings.multiplayerMainMenu_arrowSelection[5],
        select6 = settings.multiplayerMainMenu_arrowSelection[6],
        select7 = settings.multiplayerMainMenu_arrowSelection[7],
        select8 = settings.multiplayerMainMenu_arrowSelection[8],
        select9 = settings.multiplayerMainMenu_arrowSelection[9],
        
        select10 = settings.multiplayerMainMenu_arrowSelection[10],
        select11 = settings.multiplayerMainMenu_arrowSelection[11],
        select12 = settings.multiplayerMainMenu_arrowSelection[12],
        select13 = settings.multiplayerMainMenu_arrowSelection[13],
        select14 = settings.multiplayerMainMenu_arrowSelection[14],
        select15 = settings.multiplayerMainMenu_arrowSelection[15],
        select16 = settings.multiplayerMainMenu_arrowSelection[16],
        select17 = settings.multiplayerMainMenu_arrowSelection[17]
    )
    print(text)



statSelector_text = {
        0: "Type decimal numbers to set the Health Value",
        1: "Type decimal numbers to set the Attack Value",
        2: "Type decimal numbers to set the Defense Value",
        3: "Type decimal numbers to set the Energy Value",
    
        4: "Skill #1",
        5: "Skill #2",
        6: "Skill #3",
        7: "Skill #4",
        8: "Skill #5"
    }
nameOfBasicAttributes = {
    0: "hp",
    1: "atk",
    2: "defense",
    3: "energy",
}
textValue = "" # Dedicated for the function below
editorZeroValueError = ""
def gameSelector_multiplayerMenuDisplayNames_editorMsg(selectedOption):
    text = '''
{textGuide}
{value}_
Press enter once done.
{error}
    '''.format(textGuide = statSelector_text[selectedOption],
               value = textValue,
               error = editorZeroValueError)
    print(text)
    
def gameSelector_multiplayerMenuDisplayNames_skillSelectorMsg(selectedSkillNumber):
    text = ('=================================',
            f'Select skill for {selectedSkillNumber}',
            f'► "Q": {skills.Basic_Attack()} > {skills.Basic_Attack.description}',
            f'',
            f'► "B": Back')
    finalText = '\n'.join(text)
    
    
    print(finalText)
    
# =================[Multiplayer PVP GAME SESSION]=================
# =================[Multiplayer PVP GAME SESSION]=================
# =================[Multiplayer PVP GAME SESSION]=================

def gameSelector_multiplayerMenu_startGameTurn01(playerClass):
    text = '''
=================================================
{user_name}'s Turn!
Player01 HP: {p1_hp}
Player01 ATK: {p1_atk}
Player01 DEF: {p1_defense}
Player01 ENERGY: {p1_energy}

Player02 HP: {p2_hp}
Player02 ATK: {p2_atk}
Player02 DEF: {p2_defense}
Player02 ENERGY: {p2_energy}

Select Action:
► "{c1}" : {skill0} > {skill0_desc}
► "{c2}" : {skill1} > {skill1_desc}
► "{c3}" : {skill2} > {skill2_desc}
► "{c4}" : {skill3} > {skill3_desc}
► "{c5}" : {skill4} > {skill4_desc}

► "Q": Back
    '''.format(
        user_name = playerClass.name,
        p1_hp = stats.player01.hp,
        p1_atk = stats.player01.atk,
        p1_defense = stats.player01.defense,
        p1_energy = stats.player01.energy,
        
        p2_hp = stats.player02.hp,
        p2_atk = stats.player02.atk,
        p2_defense = stats.player02.defense,
        p2_energy = stats.player02.energy,
        
        skill0 = stats.player01.skills[0],
        skill1 = stats.player01.skills[1],
        skill2 = stats.player01.skills[2],
        skill3 = stats.player01.skills[3],
        skill4 = stats.player01.skills[4],
        
        skill0_desc = playerClass.skills[0].description,
        skill1_desc = playerClass.skills[1].description,
        skill2_desc = playerClass.skills[2].description,
        skill3_desc = playerClass.skills[3].description,
        skill4_desc = playerClass.skills[4].description,
        
        c1 = playerClass.keybind1,
        c2 = playerClass.keybind2,
        c3 = playerClass.keybind3,
        c4 = playerClass.keybind4,
        c5 = playerClass.keybind5,
    )
    print(text)