from custom_mechanics import effects

# Basic Attack 
class Basic_Attack:
    name = "Basic Attack"
    def __repr__(self):
        return self.name
    description = "Attacks target based on user ATK. +1 Energy"
    
    def assignTarget(self, target, caster):
        self.target = target
        self.caster = caster
        
    def action(self):
        effects.harmFunction(self.target, (self.caster.atk * self.caster.amplifier))
        self.caster.amplifier = 1
        self.caster.energy += 1
        
class Heal:
    name = "Heal"
    def __repr__(self):
        return self.name
    description = "Heals user. -1 Energy"
    energyCost = 1
    
    def assignTarget(self, caster):
        self.caster = caster
        self.target = caster
    
    def action(self):
        self.caster.hp += 2 * self.caster.amplifier
        self.caster.amplifier = 1
        self.caster.energy -= 1
        
class Amplify:
    name = "Amplify"
    def __repr__(self):
        return self.name
    description = "Boosts skill effects"
    
    def assignTarget(self, caster):
        self.caster = caster
        self.target = caster
        
    def action(self):
        self.caster.amplifier += 1
        
class Defense:
    name = "Defense"
    def __repr__(self):
        return self.name
    description = "Boost Defense. -1 Energy"
    energyCost = 1
    
    def assignTarget(self, caster):
        self.caster = caster
        self.target = caster
        
    def action(self):
        self.caster.defense += 2 * self.caster.amplifier
        self.caster.amplifier = 1
        self.caster.energy -= 1
        
class Burn:
    name = "Burn"
    def __repr__(self):
        return self.name
    description = "Burn Target Overtime. -1 Energy"
    energyCost = 1
    
    def assignTarget(self, target, caster):
        self.caster = caster
        self.target = target
        
        self.damage = self.caster.amplifier
    
    def action(self):
        effects.effectList.append(effects.Burn(self.caster, self.target, 3))
        self.caster.energy -= 1
        
class Weaken:
    name = "Weaken"
    def __repr__(self):
        return self.name
    description = "Weaken Target's ATK and Amplifier. -2 Energy"
    energyCost = 2
    
    def assignTarget(self, target, caster):
        self.caster = caster
        self.target = target
        
    def action(self):
        self.target.atk = int(self.target.atk/2)
        self.target.amplifier = int(self.target.amplifier/2)
        self.caster.energy -= 2
        
class Energize:
    name = "Energize"
    def __repr__(self):
        return self.name
    description = "Gain +2 Energy. 4 Turn Cooldown"
    
    def assignTarget(self, caster):
        self.caster = caster
        self.target = caster
    
    def action(self):
        self.caster.energy += 2
        effects.effectList.append(effects.AbilityCooldown(self.caster, self.name, 4))
        
class Strengthen:
    name = "Strengthen"
    def __repr__(self):
        return self.name
    description = "Gain +2 ATK"
    
    def assignTarget(self, caster):
        self.caster = caster
        self.target = caster
    
    def action(self):
        self.caster.atk += 2
        