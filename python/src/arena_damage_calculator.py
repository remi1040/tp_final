import math
import random
from enum import Enum

class HeroElement(Enum):
    FIRE = 1
    WATER = 2
    EARTH = 3

class Buff(Enum):
    ATTACK = 1
    DEFENSE = 2

class Hero:
    def __init__(self, element: HeroElement, power, defense, leth, crtr, lp):
        self.element = element
        self.pow = power
        self.defense = defense
        self.leth = leth
        self.crtr = crtr
        self.lp = lp
        self.buffs = list()

class ArenaDamageCalculator:
    def attacked(self):
        if len(self.degats_superieurs)>0:
            attacked = random.choice(self.degats_superieurs)
        if len(self.degats_egaux)>0:
            attacked=random.choice(self.degats_egaux)
        if len(self.degats_inferieurs)>0:
            attacked=random.choice(self.degats_inferieurs)
        return attacked
    def computeDamage(self, attacker:Hero, defenders: list[Hero]):
        power = attacker.pow

        self.degats_superieurs = list()
        self.degats_egaux = list()
        self.degats_inferieurs = list()

        if attacker.element == HeroElement.WATER:
            for h in defenders:
                if h.lp == 0:
                    continue
                if h.element == HeroElement.FIRE:
                    self.degats_superieurs.append(h)
                elif h.element == HeroElement.WATER:
                    self.degats_egaux.append(h)
                else:
                    self.degats_inferieurs.append(h)
        elif attacker.element == HeroElement.FIRE:
            for h in defenders:
                if h.lp == 0:
                    continue
                if h.element == HeroElement.FIRE:
                    self.degats_egaux.append(h)
                elif h.element == HeroElement.WATER:
                    self.degats_inferieurs.append(h)
                else:
                    self.degats_superieurs.append(h)
        else:   # Hero is of type water
            for h in defenders:
                if h.lp == 0:
                    continue
                if h.element == HeroElement.FIRE:
                    self.degats_inferieurs.append(h)
                elif h.element == HeroElement.WATER:
                    self.degats_superieurs.append(h)
                else:
                    self.degats_egaux.append(h)

        
        attacked=self.attacked()
        c = random.random() * 100 < attacker.crtr
        dmg = 0
        if c:
            dmg = (attacker.pow + (0.5 + attacker.leth / 5000) * attacker.pow) * (1-attacked.defense /7500)
        else:
            dmg = attacker.pow * (1-attacked.defense / 7500)

        ## BUFFS
        if Buff.ATTACK in attacker.buffs:
            if c:
                dmg += (attacker.pow * 0.25 + (0.5 + attacker.leth / 5000) * attacker.pow * 0.25) * (1-attacked.defense/7500)
            else:
                dmg += attacker.pow * 0.25* (1-attacked.defense/7500)

        if Buff.DEFENSE in attacked.buffs:
            dmg = dmg / (1-attacked.defense/7500) * (1-attacked.defense/7500 -0.25)

        dmg = max(dmg, 0)
        if dmg > 0:
            if attacked in self.degats_superieurs:
                dmg = dmg + dmg * 20/100
            elif attacked in self.degats_egaux:
                pass
            else:
                dmg = dmg - dmg *20/100

        dmg = math.floor(dmg)

        if dmg > 0:
            attacked.lp = attacked.lp - dmg
            if attacked.lp < 0:
                attacked.lp = 0

        return defenders