# Karas Ausgangsposition wird dahinbgehend angepasst,
# dass sie neben einen Baum gestellt wird, damit die
# Befehle der while-Schleife unten ausgeführt werden können.
kara.move()
kara.putLeaf()
kara.turnRight()
kara.move()
kara.putLeaf()

# Der Zähler dient als Abbruchbedingung für das gesamte
# Programm, da es sich umm ein Viereck handelt 4.
zaehler = 4

while zaehler != 0: # Hier wird der Zähler genutzt.
    # Kara bewegt sich nach vorne und legt ggf. ein
    # Kleeblatt ab, wie rechts von ihr ein Baum ist.
    while kara.treeRight():
        kara.move()
        if not kara.onLeaf(): # Reine Vorsichtsmaßnahme
            kara.putLeaf() # Ggf. wird ein Kleeblatt gesetzt
        
        # Am Ende muss sie sich natürlich noch in Richtung
        # der nächsten Baumreihe drehen.
        if not kara.treeRight():
            kara.turnRight()

    # Nach dem Drehen ist es nötig sie einen Schritt nach
    # vorne zu bringen, da sie sich sonst nicht rechts neben
    # sich einen Baum vorfindet und somit Baumreihe durch
    # die while-Schleife nicht umgangen werden kann.
    kara.move()
    if not kara.onLeaf(): # Reine Vorsichtsmaßnahme
        kara.putLeaf() # Ggf. wird ein Kleeblatt gesetzt
    
    # Der Zähler wird bei jeder Iteration um 1 verringert
    # um die while-Schleife zu beenden.
    zaehler = zaehler - 1

# Kara wird in die gewünschte Endposition gebracht.
kara.move()
kara.putLeaf()

kara.move()
kara.turnRight()

kara.move()

# Kara wird umgedreht.
kara.turnRight()
kara.turnRight()