import settings

# Refer to this py file for editing default user stats
class No_Selected_Skill:
    def __repr__(self):
        return "None"
    def __init__(self):
        self.description = "None"
    def performSkill(self, user, target):
        print(user,"attacks",target,"!")
        

    
# User:
class Player:
    def __init__(self, name):
        self.name = str(name)
        
        self.hp = 20
        self.atk = 2
        self.defense = 2
        self.energy = 3
        
        self.skills = [No_Selected_Skill(), No_Selected_Skill(), No_Selected_Skill(), No_Selected_Skill(), No_Selected_Skill()]
        self.keybind1 = ""
        self.keybind2 = ""
        self.keybind3 = ""
        self.keybind4 = ""
        self.keybind5 = ""        
    def __repr__(self):
        return self.name
# Default value and for declaration purposes and stuff. 
player01 = Player("Player 1")
player02 = Player("Player 2")

def loadPlayerKeybinds():
    player01.keybind1 = settings.keybinds["p1choice1"]
    player01.keybind2 = settings.keybinds["p1choice2"]
    player01.keybind3 = settings.keybinds["p1choice3"]
    player01.keybind4 = settings.keybinds["p1choice4"]
    player01.keybind5 = settings.keybinds["p1choice5"]
    player02.keybind1 = settings.keybinds["p2choice1"]
    player02.keybind2 = settings.keybinds["p2choice2"]
    player02.keybind3 = settings.keybinds["p2choice3"]
    player02.keybind4 = settings.keybinds["p2choice4"]
    player02.keybind5 = settings.keybinds["p2choice5"]
    