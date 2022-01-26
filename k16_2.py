# Abmessungen des Rechtechs
breite = 6
hoehe = 4

# Zweimal, da nur zwei Schenkel eines 90° Winkels
# ausgelegt werden.
i = 2
while i > 0:    
    # Variablen werden zweimal benutzt und
    # dürfen daher an sich nicht geändert werden.
    breite_hilf = breite
    hoehe_hilf =  hoehe    

    # Der Breite nach Auslegen
    while breite_hilf > 1:
        kara.putLeaf()
        kara.move()

        breite_hilf = breite_hilf - 1

    kara.turnRight()

    # Nach Länge nach Auslegen
    while hoehe_hilf > 1:

        kara.putLeaf()
        kara.move()

        hoehe_hilf = hoehe_hilf - 1

    kara.turnRight()

    i = i - 1