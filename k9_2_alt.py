l = 1 # Länge des Spielfelds (Startwert 1 wegen Feld vor Spielfeldecke.)
b = 2 # Breite des Spielfelds (Startwert 1 wegen Feld vor Spielfeldecke.)
courners = 4 # Es handelt sich ja um ein Rechteck.


# Kara zwischen die Spielfeldecken bringen.
kara.move()
kara.turnRight()
kara.move()
kara.turnLeft()

# Möchtegern for-Schleife für Spielfeldrand (Rechteckig).
while courners > 0:
    # Kleeblatt auslegen; normal:
    while not kara.treeFront():
        if not kara.onLeaf():
            kara.putLeaf()

        if courners == 4:
            l = l + 1
        elif courners == 3:
            b = b + 1

        kara.move()
    
    # Kleeblatt auslegen; Feld vor dem Baum:
    if not kara.onLeaf():
        kara.putLeaf()

    # Um Spielfeldecke gehen.
    kara.turnRight()
    kara.move()

    kara.turnLeft()
    kara.move()

    kara.turnRight()

    courners = courners - 1

# Damit Kara später hoch und runter gehen kann
# muss die Länge für sie immer ungerade sein.
if l % 2 == 0:
    l = l + 1

kara.turnRight()
kara.move()

while not kara.onLeaf():
    kara.putLeaf()
    kara.move()
    
    if kara.onLeaf():
        kara.turnLeft()
        kara.move()
        kara.turnLeft()
        
[...]

# Ab hier dient der Code nur dazu sie zur Endposition zu bringen.
while kara.onLeaf() and not kara.treeFront():
    kara.move()

kara.turnRight()

while not kara.treeRight() and not kara.treeLeft():
    kara.move()

kara.turnRight()
kara.turnRight()

if kara.treeLeft():
    kara.move()
    kara.turnLeft()
    kara.move()

    while kara.onLeaf() and not kara.treeFront():
        kara.move()

    kara.turnRight()

    while not kara.treeRight():
        kara.move()