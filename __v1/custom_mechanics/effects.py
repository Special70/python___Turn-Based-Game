def harmFunction(target, dmg): # Main function that helps implement damaging target defense then hp and to avoid excessive duplicate code lines when dealing with damaging hp and defense
    if target.defense > 0:
        target.defense -= dmg
        if target.defense < 0:
            target.defense = 0
    else:
        target.hp -= dmg
        target.amplifier = 1

effectList = []
def effectLoaderStart(): # Performs extra actions every start of turn
    for i in effectList:
        i.action() # Execute effect action
        if i.duration == 0:
            effectList.remove(i)
        else:
            i.duration -= 1

class AbilityCooldown:
    def __init__(self, caster, skillname, duration):
        self.skillname = skillname
        self.caster = caster
        self.target = caster
        self.duration = duration
    def __repr__(self):
        return "Cooldown: "+self.skillname+" ("+str(self.duration)+")"
    def action(self):
        pass

class Burn:
    def __init__(self, caster, target, duration):
        self.caster = caster
        self.target = target
        self.duration = duration * self.caster.amplifier
        self.damage = self.caster.amplifier
        
        self.targetName = target.name
    def __repr__(self):
        return "Burn ("+str(self.duration)+")"
    def action(self):
        harmFunction(self.target, (self.caster.atk * self.caster.amplifier))