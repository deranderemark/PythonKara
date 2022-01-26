# Funktion t nimmt Parameter "times" und "turnval"
# "times" bestimmt die Anzahl der Iterationen.
# "turnval" die Richtung in die Kara sich am Anfang
# jedes Intervals (nicht) drehen soll.
def t(times, turnval):
    
    for i in range(0, times, 1):
            
            # Links- oder Rechtsdrehung
            if turnval == "left":
                kara.turnLeft()
            
            elif turnval == "right":
                kara.turnRight()
            
            # Geradeaus gehen
            else:
                pass

            kara.move()


def main():
    
    kara.turnRight()
    kara.move()
    
    t(3, "left")

    t(2, "right")

    t(1, 0)

    kara.turnLeft()
    kara.move()
    
    t(2, "right")

    kara.turnLeft()
    kara.move()

    kara.turnRight()
    kara.move()
    
    kara.turnLeft()
    
    
main()

# Mark Steffes