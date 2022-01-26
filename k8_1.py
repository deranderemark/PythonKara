def movewhile():
    """Kara geht solange einen Schritt wie kein Baum vor ihr ist"""

    # Wenn vor Kara kein Baum ist geht sie einen Schritt
    # und ruft danach solange sich selbst auf, wie vor
    # ihr kein Baum ist.
    if not kara.treeFront():
        kara.move()

        movewhile()
    else:
        pass


def main():
    """Main-Funktion (Führt Programm aus)"""
    
    # "Geradeaus gehen"
    movewhile()
    kara.turnLeft()

    # "Nach oben gehen"
    movewhile()
    # Von Aufgabe definierte Endposition einnehmen
    kara.turnRight()
    kara.turnRight()

# Bringe mia de Stein innett Rolle...
main()