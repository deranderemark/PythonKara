while kara.onLeaf():
    if kara.onLeaf():
        kara.removeLeaf()
    
    kara.move()

    # Kara geht dann um die Ecke, wenn dort eine Kleeblattreihe beginnt.
    kara.turnRight()
    kara.move()

    # Wenn dort eine Kleeblattreihe beginnt!
    if not kara.onLeaf():
        kara.turnRight()
        kara.turnRight()
        
        kara.move()
        
        kara.turnRight()
    # Hier ist das dann so.
    else:
        kara.turnRight()
        kara.turnRight()

        kara.move()

        kara.removeLeaf()

        kara.turnRight()
        kara.turnRight()

        kara.move()

kara.turnRight()