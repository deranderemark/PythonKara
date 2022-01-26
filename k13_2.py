while not (kara.treeLeft() and kara.treeRight()):
    while not kara.onLeaf() and not (kara.treeLeft() and kara.treeRight()):
        kara.move()

    if kara.treeRight() and not kara.treeLeft():
        kara.move()
        kara.turnRight()
        kara.move()
        kara.move()
        kara.turnRight()
    elif kara.treeLeft() and not kara.treeRight():
        kara.move()
        kara.turnLeft()
        kara.move()
        kara.move()
        kara.turnLeft()