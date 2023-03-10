from src.arena_damage_calculator import Hero,ArenaDamageCalculator,HeroElement,Buff
import pytest

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

def test_fire_attack_fire_lp_and_earth(heros):
    hero_fire=heros["hero_fire"]
    hero_fire_adv=heros["hero_fire_adv"]
    hero_earth_adv=heros["hero_earth_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv,hero_earth_adv])
    assert hero_fire_adv.lp==40
    assert hero_earth_adv.lp==16
    
def test_buff_attack(heros):
    hero_fire=heros["hero_fire"]
    hero_fire.buffs=[Buff.ATTACK] 
    hero_fire_adv=heros["hero_fire_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==15
    
def test_buff_defense_crit(heros):
    hero_fire=heros["hero_fire"]    
    hero_fire_adv=heros["hero_fire_adv"]
    hero_fire_adv.buffs=[Buff.DEFENSE] 
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==30
    
def test_buff_holy(heros):
    hero_fire=heros["hero_fire"]
    hero_water_adv=heros["hero_water_adv"]
    hero_fire.buffs=[Buff.HOLY]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv])
    assert hero_water_adv.lp==15
    
def test_buff_turncoat_elements(heros):
    hero_fire=heros["hero_fire"]
    hero_water=heros["hero_water"]
    hero_earth=heros["hero_earth"]
    hero_fire_adv=heros["hero_fire_adv"]
    hero_water_adv=heros["hero_water_adv"]
    hero_earth_adv=heros["hero_earth_adv"]
    hero_fire.buffs=[Buff.TURNCOAT]
    hero_water.buffs=[Buff.TURNCOAT]
    hero_earth.buffs=[Buff.TURNCOAT] 
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    ArenaDamageCalculator().computeDamage(hero_water,[hero_earth_adv])
    ArenaDamageCalculator().computeDamage(hero_earth,[hero_water_adv])
    assert hero_fire_adv.lp==16
    assert hero_earth_adv.lp==20
    assert hero_water_adv.lp==24

def test_buff_turncoat_elements_def(heros):
    hero_fire=heros["hero_fire"]
    hero_water=heros["hero_water"]
    hero_earth=heros["hero_earth"]
    hero_fire_adv=heros["hero_fire_adv"]
    hero_water_adv=heros["hero_water_adv"]
    hero_earth_adv=heros["hero_earth_adv"]
    hero_fire_adv.buffs=[Buff.TURNCOAT]
    hero_water_adv.buffs=[Buff.TURNCOAT]
    hero_earth_adv.buffs=[Buff.TURNCOAT] 
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    ArenaDamageCalculator().computeDamage(hero_water,[hero_earth_adv])
    ArenaDamageCalculator().computeDamage(hero_earth,[hero_water_adv])
    assert hero_fire_adv.lp==24
    assert hero_earth_adv.lp==16
    assert hero_water_adv.lp==20
    
def test_damage_is_not_critical_egalite(heros):
    hero_fire=heros["hero_fire"]
    hero_fire.crtr=0
    hero_fire_adv=heros["hero_fire_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==30
    
def test_damage_is_not_critical_inferieur(heros):
    hero_fire=heros["hero_fire"]
    hero_fire.crtr=0
    hero_water_adv=heros["hero_water_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv])
    assert hero_water_adv.lp==32
    
def test_damage_is_not_critical_superieur(heros):
    hero_fire=heros["hero_fire"]
    hero_fire.crtr=0
    hero_earth_adv=heros["hero_earth_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_earth_adv])
    assert hero_earth_adv.lp==28
    
def test_lp_inferieur_0(heros):
    hero_fire=heros["hero_fire"]    
    hero_fire_adv=heros["hero_fire_adv"]
    hero_fire_adv.lp=1
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==0
    
def test_damage_egal_0(heros):
    hero_fire=heros["hero_fire"]
    hero_fire.pow=0
    hero_fire_adv=heros["hero_fire_adv"]    
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==40

def test_lp_0_earth(heros):
    hero_fire=heros["hero_fire"]    
    hero_fire_adv=heros["hero_fire_adv"]
    hero_earth_adv=heros["hero_earth_adv"]
    hero_earth_adv.lp=0
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv,hero_earth_adv])
    assert hero_earth_adv.lp==0
    assert hero_fire_adv.lp==20


def test_buff_attack_defense(heros):
    hero_fire=heros["hero_fire"]
    hero_fire.buffs=[Buff.ATTACK] 
    hero_fire_adv=heros["hero_fire_adv"]
    hero_fire_adv.buffs=[Buff.DEFENSE]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_fire_adv])
    assert hero_fire_adv.lp==28

def test_buff_holy_0(heros):
    hero_fire=heros["hero_fire"]
    hero_water_adv=heros["hero_water_adv"]
    hero_earth_adv=heros["hero_earth_adv"]
    hero_fire.buffs=[Buff.HOLY]
    hero_earth_adv.lp = 0
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv,hero_earth_adv])
    assert hero_water_adv.lp==15
    assert hero_earth_adv.lp==0






