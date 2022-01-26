# Wiederhole "times"-Male: Kara beweget sich einen
# Schritt und setzt ein Kleeblatt
def pLmove(times):
	
	for i in range(0, times, 1):
	    kara.move()
	    kara.putLeaf()
	
	kara.turnRight()

        
def main():
      
    kara.putLeaf()
    kara.turnLeft()
    
    # Funktionsaufrufe mit entsprechenden
    # Parametern
    
    pLmove(1)
    pLmove(2)
    pLmove(2)
    pLmove(2)


main()
# Mark Steffes