kara.turnRight()
kara.turnRight()

kara.move()

kara.turnLeft()

while not kara.treeFront():
    kara.move()

kara.turnRight()
kara.turnRight()

# Kara misst die Position des Eingangs ab.
pos_y = 0
while kara.treeRight():
    kara.move()

    pos_y = pos_y + 1

kara.turnRight()
kara.move()

# Kara geht aus dem Bau heraus (Wand beliebiger dicke)
while kara.treeLeft() and kara.treeRight():
    kara.move()

kara.turnRight()

# Kara umgeht den Bau
i = 2
while i > 0:
    kara.move()

    while kara.treeRight():
        kara.move()

    kara.turnRight()

    i = i - 1

kara.move()

# Kara nutzt die Positionsdaten, um das Kleeblatt
# gegenüber von Eingang zu platzieren.
while pos_y >= 0:
    kara.move()

    pos_y = pos_y - 1

if not kara.onLeaf():
    kara.putLeaf()
kara.turnLeft()