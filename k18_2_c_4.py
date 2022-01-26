n = 5
i = 0
counter = 0

x = 0
while x != n:
    y = 0
    while y != n:
        if (y % 2) == 0 and x >= i:
            world.setLeaf(x, y, True)
        y = y + 1
    x = x + 1
   
# ALTERNATIVE
n = 10
breite = 0
while breite != n +1 :
    hoehe = n  
    while breite <= hoehe :
        world.setLeaf(hoehe, breite, True)
        hoehe = hoehe -1
    breite = breite +2
