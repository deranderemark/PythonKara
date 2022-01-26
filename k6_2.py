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

        movewhile() # Die Funktion ruft sich, wie obige Bedingung erfüllt ist selbst auf.
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

def turn_to_end_pos():
    """Endblickrichtung wird eingenommen"""

    # Im Uhrzeigersinn
    if kara.treeRight():
        if not kara.onLeaf():
            kara.putLeaf()
        else:
            pass

        kara.turnLeft()
    # Gegen Uhrzeigersinn
    elif kara.treeLeft():
        if not kara.onLeaf():
            kara.putLeaf()
        else:
            pass

        kara.turnRight()
    # Wurde keine bekannten Endposition von Kara erkannt,
    # bleibt ihre Blickrichtung und Position unverändert.
    else:
        pass

def main(config):
    """
    Main-Funktion (Führt Programm aus)
    
    :param config: ganze Runde -> "full"; halbe Runde -> None
    """

    # Drehen von Kara in eine Ausganglage
    turn("left")

    # Ab hier beginnt die Umrundung des Baumhindernisses
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