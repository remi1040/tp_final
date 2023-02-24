import pytest
from src.arena_damage_calculator import *
@pytest.fixture
def heros():
    hero_fire=Hero(HeroElement.FIRE,5,3750,2500,100,10)
    hero_earth=Hero(HeroElement.EARTH,5,3750,2500,100,10)
    hero_water=Hero(HeroElement.WATER,5,3750,2500,100,10)
    hero_fire_adv=Hero(HeroElement.FIRE,5,3750,2500,100,10)
    hero_earth_adv=Hero(HeroElement.EARTH,5,3750,2500,100,10)
    hero_water_adv=Hero(HeroElement.WATER,5,3750,2500,100,10)
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
    assert hero_fire_adv.lp==4
def test_fire_attack_earth_lp(heros):
    hero_fire=heros["hero_fire"]
    hero_earth_adv=heros["hero_earth_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_earth_adv])
    assert hero_earth_adv.lp==4
def test_earth_attack_water_lp(heros):
    hero_earth=heros["hero_earth"]
    hero_water_adv=heros["hero_water_adv"]
    ArenaDamageCalculator().computeDamage(hero_earth,[hero_water_adv])
    assert hero_water_adv.lp==4
def test_fire_attack_water_lp(heros):
    hero_fire=heros["hero_fire"]
    hero_water_adv=heros["hero_water_adv"]
    ArenaDamageCalculator().computeDamage(hero_fire,[hero_water_adv])
    assert hero_water_adv.lp==6
def test_earth_attack_fire_lp(heros):
    hero_earth=heros["hero_earth"]
    hero_fire_adv=heros["hero_fire_adv"]
    ArenaDamageCalculator().computeDamage(hero_earth,[hero_fire_adv])
    assert hero_fire_adv.lp==6
def test_water_attack_earth_lp(heros):
    hero_water=heros["hero_water"]
    hero_earth_adv=heros["hero_earth_adv"]
    ArenaDamageCalculator().computeDamage(hero_water,[hero_earth_adv])
    assert hero_earth_adv.lp==6


