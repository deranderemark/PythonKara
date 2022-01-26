def main():

    while not kara.treeFront():

        if kara.onLeaf():
            kara.removeLeaf()
        
        else:
            pass

        kara.move()
    
    if kara.onLeaf():
        kara.removeLeaf()
        

main()