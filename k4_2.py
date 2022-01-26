# Bewegt Kara um einen Schritt nach vorne und dreht sie ggf. um.
# Die Funktion gibt zurück, ob ihre bedingte Anweisung erfüllt worden
# ist, oder nicht.
# Nimmt keine Parameter.
def picknturn():
    kara.move()

    # Falls unter Kara ein Kleeblatt ist nimmt sie es sich und
    # dreht sich um 180° nach rechts um.
    if kara.onLeaf():
        kara.removeLeaf()
        
        kara.turnRight()
        kara.turnRight()

        # Bedingung erfüllt
        return True
    
    else:
        # Bedingung nicht erfüllt.
        return None


# "Hauptfunktion"; Nimmt keine Parameter.
def main():

    if picknturn() == True:    
        # Wenn ein Blatt erkannt und entfernt wurde, d.h. dass picknturn
        # True zur�ckgibt, geht Kara selbstständig zurück.
        kara.move()
    
    # Ist das nicht der Fall gibt die picknturn()-Funktion None wieder,
    # die Bedingung ist also nicht erfüllt, wodurch das Programm den
    # entsprechenden nachfolgenden Code ausfährt.
    else:
        # ""    ""
        if picknturn() == True:
            # In diesem Fall sind zum Zurückgehen 2 Schritte nötig.
            kara.move()
            kara.move()

        # ""    ""
        else:
            if picknturn() == True:
                # Hier sogar 3 Schritte.
                kara.move()
                kara.move()
                kara.move()

            # Hier könnte das Programm erweitert werden, um
            # die "Baumtrasse" zu erweitern oder um im Falle eines
            # vom Programm nicht betrachteten Fall zu "melden".
            else:
                # Dieser Fall wird in der Aufgabe nicht explizit
                # betrachtet.
                pass
                ## Kara hat Entzugserscheinungen, weil sie kein Kleeblatt
                ## finden kann.
                # for i in range(0, 12, 1):
                #   kara.turnRight()
    
    kara.putLeaf()


# "Startet" Programm (Ruft main()-Funktion auf.)
main()


## "Normale Variante, ohne 'Schi-Schi'."

# kara.move()

# if kara.onLeaf():
# kara.removeLeaf()
# kara.turnRight()
# kara.turnRight()

# kara.move()

# kara.putLeaf()
# else:
# kara.move()

# if kara.onLeaf():
#     kara.removeLeaf()
#     kara.turnRight()
#     kara.turnRight()
    
#     kara.move()
#     kara.move()

#     kara.putLeaf()
# else:
#     kara.move()

#     if kara.onLeaf():
#         kara.removeLeaf()
#         kara.turnRight()
#         kara.turnRight()

#         kara.move()
#         kara.move()
#         kara.move()

#         kara.putLeaf()
#     else:
#         pass