#import pytest
from src.arena_damage_calculator import Hero,ArenaDamageCalculator,HeroElement,Buff
# @pytest.fixture
# def heros():
#     hero_fire=Hero(HeroElement.FIRE,20,3750,2500,100,40)
#     hero_earth=Hero(HeroElement.EARTH,20,3750,2500,100,40)
#     hero_water=Hero(HeroElement.WATER,20,3750,2500,100,40)
#     hero_fire_adv=Hero(HeroElement.FIRE,20,3750,2500,100,40)
#     hero_earth_adv=Hero(HeroElement.EARTH,20,3750,2500,100,40)
#     hero_water_adv=Hero(HeroElement.WATER,20,3750,2500,100,40)
#     return {"hero_fire":hero_fire,
#             "hero_earth":hero_earth,
#             "hero_water":hero_water,
#             "hero_fire_adv":hero_fire_adv,
#             "hero_earth_adv":hero_earth_adv,
#             "hero_water_adv":hero_water_adv}
# def test_water_attack_fire_lp(heros):
#     hero_water=heros["hero_water"]
#     hero_fire_adv=heros["hero_fire_adv"]
#     ArenaDamageCalculator().computeDamage(hero_water,[hero_fire_adv])
#     assert hero_fire_adv.lp==16
# def test_fire_attack_earth_lp(heros):
#     hero_fire=heros["hero_fire"]
#     hero_earth_adv=heros["hero_earth_adv"]
#     ArenaDamageCalculator().computeDamage(hero_fire,[hero_earth_adv])
#     assert hero_earth_adv.lp==16
# def test_earth_attack_water_lp(heros):
#     hero_earth=heros["hero_earth"]
#     hero_water_adv=heros["hero_water_adv"]
#     ArenaDamageCalculator().computeDamage(hero_earth,[hero_water_adv])
#     assert hero_water_adv.lp==16
# def test_fire_attack_water_lp(heros):
#     hero_fire=heros["hero_fire"]
#     hero_water_adv=heros["hero_water_adv"]
#     ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv])
#     assert hero_water_adv.lp==24
# def test_earth_attack_fire_lp(heros):
#     hero_earth=heros["hero_earth"]
#     hero_fire_adv=heros["hero_fire_adv"]
#     ArenaDamageCalculator().computeDamage(hero_earth,[hero_fire_adv])
#     assert hero_fire_adv.lp==24
# def test_water_attack_earth_lp(heros):
#     hero_water=heros["hero_water"]
#     hero_earth_adv=heros["hero_earth_adv"]
#     ArenaDamageCalculator().computeDamage(hero_water,[hero_earth_adv])
#     assert hero_earth_adv.lp==24
# def test_earth_attack_earth_lp(heros):
#     hero_earth=heros["hero_earth"]
#     hero_earth_adv=heros["hero_earth_adv"]
#     ArenaDamageCalculator().computeDamage(hero_earth,[hero_earth_adv])
#     assert hero_earth_adv.lp==20
# def test_water_attack_water_lp(heros):
#     hero_water=heros["hero_water"]
#     hero_water_adv=heros["hero_water_adv"]
#     ArenaDamageCalculator().computeDamage(hero_water,[hero_water_adv])
#     assert hero_water_adv.lp==20
# def test_fire_attack_fire_lp(heros):
#     hero_fire=heros["hero_fire"]
#     hero_fire_adv=heros["hero_fire_adv"]
#     ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
#     assert hero_fire_adv.lp==20
# def test_buff_attack(heros):
#     hero_fire=heros["hero_fire"]
#     hero_fire.buffs=[Buff.ATTACK] 
#     hero_fire_adv=heros["hero_fire_adv"]
#     ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
#     assert hero_fire_adv.lp==15
# def test_buff_defense(heros):
#     hero_fire=heros["hero_fire"]    
#     hero_fire_adv=heros["hero_fire_adv"]
#     hero_fire_adv.buffs=[Buff.DEFENSE] 
#     ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
#     assert hero_fire_adv.lp==25
# def test_buff_holy(heros):
#     hero_fire=heros["hero_fire"]
#     hero_water_adv=heros["hero_water_adv"]
#     hero_fire.buffs=[Buff.HOLY]
#     ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv])
#     assert hero_water_adv.lp==14

def test_faiblaisses_feu():
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 0, 0, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 0, 0, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 0, 0, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_feu,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_feu,[hero_feu,hero_eau])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_feu,[hero_eau])
    
    assert hero_terre.lp == 182
    assert hero_eau.lp == 121
    assert hero_feu.lp == 51

def test_faiblaisses_eau():
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 0, 0, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 0, 0, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 0, 0, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_eau,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_eau,[hero_eau,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_eau,[hero_terre])
    
    assert hero_terre.lp == 221
    assert hero_eau.lp == 101
    assert hero_feu.lp == 32
    
def test_faiblaisses_terre():
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 0, 0, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 0, 0, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 0, 0, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_terre,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_terre,[hero_feu,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_terre,[hero_feu])
    
    assert hero_terre.lp == 201
    assert hero_eau.lp == 82
    assert hero_feu.lp == 71
    
def test_faiblaisses_feu_crit():
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 100, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 100, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 100, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_feu,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_feu,[hero_feu,hero_eau])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_feu,[hero_eau])
    
    assert hero_terre.lp == 121
    assert hero_eau.lp == 81
    assert hero_feu.lp == 1
    
def test_faiblaisses_eau_crit():
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 100, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 100, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 100, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_eau,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_eau,[hero_eau,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_eau,[hero_terre])
    
    assert hero_terre.lp == 181
    assert hero_eau.lp == 51
    assert hero_feu.lp == 0
    
def test_faiblaisses_terre_crit():
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 100, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 100, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 100, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_terre,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_terre,[hero_feu,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_terre,[hero_feu])
    
    assert hero_terre.lp == 151
    assert hero_eau.lp == 21
    assert hero_feu.lp == 31
    
def test_feu_zero():
    hero_terre_att = Hero(HeroElement.EARTH, 100, 75, 50, 0, 300,())
    
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 0, 100,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 0, 0,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 100, 0,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_terre_att,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_terre_att,[hero_terre,hero_eau,hero_feu])
    
    assert hero_terre.lp == 0
    assert hero_eau.lp == 0
    assert hero_feu.lp == 0
    
def test_buff_attaque():
    
    hero_terre_att = Hero(HeroElement.EARTH, 100, 75, 50, 0, 300,[Buff.ATTACK])
    #print(hero_terre_att.buffs)
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 0, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 0, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 0, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_terre_att,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_terre_att,[hero_feu,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_terre_att,[hero_feu])
    
    assert hero_terre.lp == 177 
    assert hero_eau.lp == 52
    assert hero_feu.lp == 51
    
    
def test_buff_defense():
    hero_terre_att = Hero(HeroElement.EARTH, 100, 75, 50, 0, 300,())
    
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 0, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 0, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 0, 300,[Buff.DEFENSE])
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_terre_att,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_terre_att,[hero_feu,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_terre_att,[hero_feu])
    
    assert hero_terre.lp == 226
    assert hero_eau.lp == 82
    assert hero_feu.lp == 71
    

def test_buff_attaque_crit():
    
    hero_terre_att = Hero(HeroElement.EARTH, 100, 75, 50, 100, 300,[Buff.ATTACK])
    #print(hero_terre_att.buffs)
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 0, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 0, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 0, 300,())
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_terre_att,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_terre_att,[hero_feu,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_terre_att,[hero_feu])
    
    assert hero_terre.lp == 114 
    assert hero_eau.lp == 0
    assert hero_feu.lp == 1
    
    
def test_buff_defense_crit():
    hero_terre_att = Hero(HeroElement.EARTH, 100, 75, 50, 100, 300,())
    
    hero_feu = Hero(HeroElement.FIRE, 100, 75, 50, 0, 150,())
    hero_eau = Hero(HeroElement.WATER, 100, 75, 50, 0, 200,())
    hero_terre = Hero(HeroElement.EARTH, 100, 75, 50, 0, 300,[Buff.DEFENSE])
    
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_terre_att,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_terre_att,[hero_feu,hero_terre])
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_terre_att,[hero_feu])
    
    assert hero_terre.lp == 189
    assert hero_eau.lp == 21
    assert hero_feu.lp == 31
    