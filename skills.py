# Basic Attack
class Basic_Attack:
    def __repr__(self):
        return "Basic Attack"
    description = "Attacks target based on user ATK"
    
    def assignTarget(self, target):
        self.target = target
        
    def action(self):
        self.target.hp -= 2