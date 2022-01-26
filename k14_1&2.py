x = 0

while not kara.treeFront():
    kara.move()

    if kara.onLeaf():
        x = x + 1
        kara.removeLeaf()

kara.turnLeft(); kara.turnLeft()

while x > 0:
    kara.putLeaf()
    kara.move()