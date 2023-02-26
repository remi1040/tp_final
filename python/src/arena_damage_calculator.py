import math
import random
from random import randint
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
        self.element = element
        self.pow = power
        self.defense = defense
        self.leth = leth
        self.crtr = crtr
        self.lp = lp
        self.buffs = list()

class ArenaDamageCalculator:
    def computeDamage(self, attacker:Hero, defenders: list[Hero]):
        
        adv = list()
        eq = list()
        dis = list()
        
        if Buff.TURNCOAT in attacker.buffs:
            if attacker.element==HeroElement.FIRE:
                attacker.element=HeroElement.WATER
            elif attacker.element==HeroElement.WATER:
                attacker.element=HeroElement.EARTH
            elif attacker.element==HeroElement.EARTH:
                attacker.element=HeroElement.FIRE
        
        for i in defenders:
            if Buff.TURNCOAT in i.buffs:
                if i.element==HeroElement.FIRE:
                    i.element=HeroElement.WATER
                elif i.element==HeroElement.WATER:
                    i.element=HeroElement.EARTH
                elif i.element==HeroElement.EARTH:
                    i.element=HeroElement.FIRE
        
        for h in defenders:
            if h.lp != 0:
                if attacker.element == HeroElement.WATER:
                    if h.element == HeroElement.FIRE:
                        adv.append(h)
                    elif h.element == HeroElement.WATER:
                        eq.append(h)
                    else:
                        dis.append(h)
                elif attacker.element == HeroElement.FIRE:
                    if h.element == HeroElement.FIRE:
                        eq.append(h)
                    elif h.element == HeroElement.WATER:
                        dis.append(h)
                    else:
                        adv.append(h)
                else:   
                    if h.element == HeroElement.FIRE:
                        dis.append(h)
                    elif h.element == HeroElement.WATER:
                        adv.append(h)
                    else:
                        eq.append(h)
        
        attacked = adv[math.floor(random.random() * len(adv))] if len(adv) > 0 else eq[math.floor(random.random() * len(eq))] if len(eq) > 0 else dis[math.floor(random.random() * len(dis))]
        
        if Buff.HOLY in attacker.buffs:
            attacked=defenders[randint(1,len(defenders))-1]
            while attacked.lp == 0:
                attacked=defenders[randint(1,len(defenders))-1]
            attacked.defense=0
            attacker.pow*=0.8 
        
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

        if dmg > 0:
            if attacked in adv:
                dmg += dmg * 20/100
            if attacked in dis:
                dmg -= dmg *20/100
            
            attacked.lp = attacked.lp - math.floor(dmg)
            if attacked.lp < 0:
                attacked.lp = 0

        return defenders