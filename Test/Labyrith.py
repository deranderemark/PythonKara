def main():
    
    if kara.treeRight():
        
        if not kara.treeFront():
            kara.move()

        else:
            kara.turnLeft()

    else:
        if kara.treeFront():
            kara.turnRight()
            kara.move()
            
        else:
            
            kara.move()
        
        
while not kara.onLeaf():
    main()