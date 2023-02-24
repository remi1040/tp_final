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
    HOLY = 3
    TURNCOAT = 4
class Hero:
    def __init__(self, element: HeroElement, power, defense, leth, crtr, lp):
        # element du heros
        self.element = element
        # puissance du hero 
        self.pow = power
        #defense du hero
        self.defense = defense
        # surcroits des degats critique 
        self.leth = leth
        # taux critique 
        self.crtr = crtr
        # point de vie
        self.lp = lp
        # liste des buffs
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
    def superieur(self,element1,element2):
        if self.attacker.element == element1:
            for defender in self.defenders:
                if defender.lp!=0 and defender.element==element2:
                    self.degats_superieurs.append(defender)
    def inferieur(self,element1,element2):
        if self.attacker.element == element1:
            for defender in self.defenders:
                if defender.lp!=0 and defender.element==element2:
                    self.degats_inferieurs.append(defender)
    def egalite(self,element1,element2):
        if self.attacker.element== element1:
            for defender in self.defenders:
                if defender.lp!=0 and defender.element==element2:
                    self.degats_egaux.append(defender)
    def verifier_bonus(self):
        for element1 in HeroElement:
            for element2 in HeroElement:
                if (element1,element2) in self.bonus:
                    self.superieur(element1,element2)
                elif (element2,element1) in self.bonus:
                    self.inferieur(element1,element2)
                else:
                    self.egalite(element1,element2)
    def estCritique(self):
        return random.random() * 100 < self.attacker.crtr
    def computeDamage(self, attacker:Hero, defenders: list[Hero]):
        self.defenders=defenders
        self.attacker=attacker
        self.degats_superieurs = list()
        self.degats_egaux = list()
        self.degats_inferieurs = list()
        self.bonus = list()
        self.bonus.append((HeroElement.WATER,HeroElement.FIRE))
        self.bonus.append((HeroElement.FIRE,HeroElement.EARTH))
        self.bonus.append((HeroElement.EARTH,HeroElement.WATER))
        if Buff.HOLY not in attacker.buffs:
            self.verifier_bonus()
            attacked=self.attacked()
        else:
            attacked=defenders[0]
            attacked.defense=0
            attacker.pow/=1.2
        damage = 0
        if self.estCritique():
            damage = (attacker.pow + (0.5 + attacker.leth / 5000) * attacker.pow) * (1-attacked.defense /7500)
        else:
            damage = attacker.pow * (1-attacked.defense / 7500)

        ## BUFFS
        if Buff.ATTACK in attacker.buffs:
            damage*=1.25
        if Buff.DEFENSE in attacked.buffs:
            damage*=0.75

        damage = max(damage, 0)
        if damage > 0:
            if attacked in self.degats_superieurs:
                damage = damage + damage * 20/100
            elif attacked in self.degats_egaux:
                pass
            else:
                damage = damage - damage *20/100

        damage = math.floor(damage)

        if damage > 0:
            print(damage)
            attacked.lp = attacked.lp - damage
            if attacked.lp < 0:
                attacked.lp = 0

        return defenders