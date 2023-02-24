from src.arena_damage_calculator import*



hero_feu = Hero(HeroElement.FIRE, 15, 50, 25, 23, 150)
hero_eau = Hero(HeroElement.WATER, 30, 75, 30, 29, 200)
hero_terre = Hero(HeroElement.EARTH, 5, 25, 50, 10, 300)

def test_faiblaisses_feu():
    cbt = ArenaDamageCalculator()
    cbt.computeDamage(hero_feu,[hero_terre,hero_eau,hero_feu])
    #print (str(hero_terre.lp) + " - "+ str(hero_eau.lp)+ " - " + str(hero_feu.lp))
    
    assert hero_terre.lp == 283
    assert hero_eau.lp == 200
    assert hero_feu.lp == 150
    
    
    cbt2 = ArenaDamageCalculator()
    cbt2.computeDamage(hero_feu,[hero_feu,hero_eau])
    
    assert hero_terre.lp == 283
    assert hero_eau.lp == 200
    assert hero_feu.lp == 136
    
    cbt3 = ArenaDamageCalculator()
    cbt3.computeDamage(hero_feu,[hero_eau,hero_eau])
    
    assert hero_terre.lp == 283
    assert hero_eau.lp == 189
    assert hero_feu.lp == 136