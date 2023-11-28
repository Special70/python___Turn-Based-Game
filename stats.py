import settings

# Refer to this py file for editing default user stats
class No_Selected_Skill:
    def __repr__(self):
        return "None"
    def __init__(self):
        self.description = "None"
        self.name = ""
    def performSkill(self, user, target):
        print(user,"attacks",target,"!")
    def action(self):
        print("None")
    
    
# User:
class Player:
    def __init__(self, name):
        self.name = str(name)
        self.amplifier = 1
        
        self.hp = 20
        self.atk = 2 * self.amplifier
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