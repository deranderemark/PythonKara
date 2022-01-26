n = 10
breite = 0
while breite != n +1 :
    hoehe = n  
    while breite <= hoehe :
        world.setLeaf(hoehe, breite, True)
        hoehe = hoehe -1
    breite = breite +2
