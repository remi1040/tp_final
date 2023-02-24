import pytest
from src.arena_damage_calculator import *
@pytest.fixture
def heros():
    hero_fire=Hero(HeroElement.FIRE,20,3750,2500,100,40)
    hero_earth=Hero(HeroElement.EARTH,20,3750,2500,100,40)
    hero_water=Hero(HeroElement.WATER,20,3750,2500,100,40)
    hero_fire_adv=Hero(HeroElement.FIRE,20,3750,2500,100,40)
    hero_earth_adv=Hero(HeroElement.EARTH,20,3750,2500,100,40)
    hero_water_adv=Hero(HeroElement.WATER,20,3750,2500,100,40)
    return {"hero_fire":hero_fire,
            "hero_earth":hero_earth,
            "hero_water":hero_water,
            "hero_fire_adv":hero_fire_adv,
            "hero_earth_adv":hero_earth_adv,
            "hero_water_adv":hero_water_adv}
def test_water_attack_fire_lp(heros):
    hero_water=heros["hero_water"]
    hero_fire_adv=heros["hero_fire_adv"]
    ArenaDamageCalculator().computeDamage(hero_water,[hero_fire_adv])
    assert hero_fire_adv.lp==16
def test_fire_attack_earth_lp(heros):
    hero_fire=heros["hero_fire"]
    hero_earth_adv=heros["hero_earth_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_earth_adv])
    assert hero_earth_adv.lp==16
def test_earth_attack_water_lp(heros):
    hero_earth=heros["hero_earth"]
    hero_water_adv=heros["hero_water_adv"]
    ArenaDamageCalculator().computeDamage(hero_earth,[hero_water_adv])
    assert hero_water_adv.lp==16
def test_fire_attack_water_lp(heros):
    hero_fire=heros["hero_fire"]
    hero_water_adv=heros["hero_water_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv])
    assert hero_water_adv.lp==24
def test_earth_attack_fire_lp(heros):
    hero_earth=heros["hero_earth"]
    hero_fire_adv=heros["hero_fire_adv"]
    ArenaDamageCalculator().computeDamage(hero_earth,[hero_fire_adv])
    assert hero_fire_adv.lp==24
def test_water_attack_earth_lp(heros):
    hero_water=heros["hero_water"]
    hero_earth_adv=heros["hero_earth_adv"]
    ArenaDamageCalculator().computeDamage(hero_water,[hero_earth_adv])
    assert hero_earth_adv.lp==24
def test_earth_attack_earth_lp(heros):
    hero_earth=heros["hero_earth"]
    hero_earth_adv=heros["hero_earth_adv"]
    ArenaDamageCalculator().computeDamage(hero_earth,[hero_earth_adv])
    assert hero_earth_adv.lp==20
def test_water_attack_water_lp(heros):
    hero_water=heros["hero_water"]
    hero_water_adv=heros["hero_water_adv"]
    ArenaDamageCalculator().computeDamage(hero_water,[hero_water_adv])
    assert hero_water_adv.lp==20
def test_fire_attack_fire_lp(heros):
    hero_fire=heros["hero_fire"]
    hero_fire_adv=heros["hero_fire_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==20
def test_buff_attack(heros):
    hero_fire=heros["hero_fire"]
    hero_fire.buffs=[Buff.ATTACK] 
    hero_fire_adv=heros["hero_fire_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==15
def test_buff_defense(heros):
    hero_fire=heros["hero_fire"]    
    hero_fire_adv=heros["hero_fire_adv"]
    hero_fire_adv.buffs=[Buff.DEFENSE] 
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==24
def test_buff_holy(heros):
    hero_fire=heros["hero_fire"]
    hero_water_adv=heros["hero_water_adv"]
    hero_fire.buffs=[Buff.HOLY]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv])
    assert hero_water_adv.lp==14
hero_feu = Hero(HeroElement.FIRE, 100, 75, 0, 0, 150)
hero_eau = Hero(HeroElement.WATER, 100, 75, 0, 0, 200)
hero_terre = Hero(HeroElement.EARTH, 100, 75, 0, 0, 300)

def test_faiblaisses_feu():
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_feu,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    assert hero_terre.lp == 182
    assert hero_eau.lp == 200
    assert hero_feu.lp == 150
    
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_feu,[hero_feu,hero_eau])
    
    # assert hero_terre.lp == 182
    assert hero_eau.lp == 200
    assert hero_feu.lp == 51
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_feu,[hero_eau])
    
    # assert hero_terre.lp == 182
    assert hero_eau.lp == 121
    # assert hero_feu.lp == 101
