def main():

    # Solange Kara keinen Baumstumpf vor sich hat.
    while not kara.treeFront():
        
        # Kara geht einen Schritt nach Vorne.
        kara.move()
        
        # Wenn kara auf einem Kleeblatt ist
        # nimmt sie es sich.
        if kara.onLeaf():
            kara.removeLeaf()
            
            kara.turnRight()
            kara.turnRight()
            kara.turnRight()
            kara.turnRight()
            kara.turnRight()
            kara.turnRight()
            kara.turnRight()
            kara.turnRight()
        
        else:
            pass
        

main()

# Mark Steffes