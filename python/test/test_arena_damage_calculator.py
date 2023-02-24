from src.arena_damage_calculator import*



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