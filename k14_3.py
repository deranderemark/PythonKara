zähler = 0

while not kara.treeFront():
    kara.move()

    if kara.onLeaf():
        zähler = zähler + 1
        kara.removeLeaf()

while (zähler * 2) > 0:
    kara.putLeaf()
    kara.move()