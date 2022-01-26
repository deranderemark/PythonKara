# Länge der mittleren Blattreihe (Startwert natürlich 0)
l = 0


# Legt mittlere Blattreihe aus
while not kara.treeFront():
    if not kara.onLeaf():
        kara.putLeaf()

    kara.move()

    # Zählt Länge dieser.
    l = l + 1

# Für das letzte Feld ganz oben.
if not kara.onLeaf():
        kara.putLeaf()

# Kara wird umgedreht.
kara.turnRight(); kara.turnRight()

# Kara geht jetzt entlang der mittleren Blattreihe zurück.
# Die länge ist ihr durch Auszählen von vorhin bereits bekannt.
while l > 0:
    # Unten angekommen, ggf. "eingeklemmt" merzen wir hier ein potentielles
    # Problem aus, indem wir die while-Schleige innerhalb einer bedingten
    # Anweisung ggf. beenden.
    if kara.treeFront() and kara.treeLeft() and kara.treeRight() and kara.onLeaf():
        break # Hier wird die while-Schleife SOFORT beendet.

    # Kara markiert sich die mittlere Blattreihe mit Hilfe des Entfernens
    # eines Kleeblattes.
    kara.removeLeaf()

    # Sie legt links von sich nun Kleeblätter auf alle Felder.
    kara.turnLeft()
    while not kara.treeFront():
        kara.move()
        kara.putLeaf()
    
    # Kara wird um 180° gedreht...
    kara.turnRight(); kara.turnRight()

    # ... und geht bis zur mittleren Blattreihe, die sie markiert hat.
    while kara.onLeaf():
        kara.move()

    # Tut selbiges in die andere Richtung, die Bäume sind ja symetrisch.
    while not kara.treeFront():
        kara.move()
        kara.putLeaf()

    # Kara wird um 180° gedreht...
    kara.turnRight(); kara.turnRight()

    # ... und geht bis zur mittleren Blattreihe, die sie markiert hat.
    while kara.onLeaf() and not kara.treeFront():
        kara.move()

    # Dreht sich dann wieder nach "unten".
    kara.turnRight()

    # "Entfernt" die Markierung durch Wiederherstellen des Kleeblatts.
    kara.putLeaf()

    # Anschließend geht sie zur nächsten horizontalen Reihe die
    # in der nächsten Iteration bearbeitet werden soll.
    if not kara.treeFront():
        kara.move()