# Code aus k6_2.py mit gewissen Modifikationen in main()-Funktion
# und vorallem der turn_to_end_pos()-Funktion.


def plmove():
    """Gleichzeitiges Gehen und Kleeblatt ablegen."""

    # Wenn keine Blatt da ist wird eins abgelegt.
    if not kara.onLeaf():
        kara.putLeaf()
    # In allen anderen Fällen muss nichts passieren.
    else:
        pass

    # Danach muss Kara wieder einen Schritt gehen.
    kara.move()

def movewhile():
    """Lässt Kara an Baumreihen vorbeiziehen, sowohl rechts als auch links."""

    # Sollte rechts oder links ein Baum sein geht Kara einen Schritt.
    if kara.treeRight() or kara.treeLeft():
        plmove()

        movewhile() # Die Funktion ruft sich, solange selbst auf, wie Bedingung erfüllt.
    else:
        pass

def turn(direction):
    """
    Lässt Kara sich in eine durch "direction" festgelegte Richtung gehen.

    :param direction: Rechts herum drehen -> "right"; Links herum drehen -> "left"
    """

    if direction == "right":
        # Durch das Aufrufen der Funktion movewhile() wird die vertikale
        # und horizontale Skalierbarkeit des "Baumhindernisses" ermöglicht.
        movewhile()

        kara.turnRight()
        plmove()
    elif direction == "left":
        movewhile()

        kara.turnLeft()
        plmove()
    # Falls kein Parameter beim Funktionsaufruf übergeben wird passiert
    # nichts und man hat halt Pech gehabt.
    else:
        pass

def turn_to_end_pos(): # Modifiziert für Situation k8_2.py, daher unpassender Name.
    """Endposition wird eingenommen"""

    turn("right") # Kara geht in die "Ausgangslücke" zurück.

    # Kara dreht sich um 180°.
    kara.turnRight()
    kara.turnRight()

def main(config):
    """
    Main-Funktion (Führt Programm aus)
    
    :param config: ganze Runde -> "full"; halbe Runde -> None
    """

    # Ausgangsposition modifizieren, um Situation für Code aus k6_2.py
    # kompatibel zu halten.
    kara.move()

    # Ab hier beginnt die Umrundung des Baumhindernisses
    turn("right")
    turn("right")
    turn("right")

    # Wird die ganze Runde beim Funktionsaufruf über den Parameter
    # "config" durch übergeben des Strings "full" gewünscht wird das
    # auch gemacht.
    if config == "full":
        turn("right")
        turn("right")
    else:
        pass

    turn_to_end_pos()


# Funktionsaufruf von main(), um das Programm zum Laufen zu bringen.
main("full")