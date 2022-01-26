class Clock:
    def restricted_tick(self):
        """
        Verhindert, dass Kara einen Pilz verschiebt wenn sie
        einen Schritt macht. -> "Abgesicherter" Schritt
        """
        if not kara.mushroomFront():
            kara.move()
        else:
            pass

    def clock_hand_tick(self):
        """
        Kara bewegt sich einen Schritt nach vorne wie kein
        Pilz vor ihr ist. Sollte dem so sein verschiebt sie ihn
        über die Funktion change_time() aus der selben Klasse.
        """

        # Zählt die Ticks/ die Anzahle des Tickens der "Uhr".
        self.ticks += 1

        # Kara steht neben einem Baum und vor ihr ist kein Pilz.
        if not kara.mushroomFront() and kara.treeRight():
            kara.move()
            self.clock_hand_tick() # Selbstaufruf
        #  Wenn auf 12 Uhr kein Pilz ist. (Da kann natürlich auch kein Pilz sein)
        # (Der "Spezialfall")
        elif self.ticks == 1 and not kara.mushroomFront():
            kara.move()

            kara.turnLeft()
            # Wird statt kara.move() verwendet, da nach der Drehung die Position
            # des Pilzes nicht bekannt ist.
            # Gegebenenfalls muss aber, falls der Pilz nicht vor ihr ist,
            # ein Schritt möglich sein, daher nur der "abgesicherte" Schritt.
            self.restricted_tick()
            self.clock_hand_tick() # Selbstaufruf
        elif not kara.mushroomFront():
            kara.turnRight()
            self.restricted_tick()
            self.clock_hand_tick() # Selbstaufruf
        # Im Zweifel entscheidet sich die Uhr den Zeiger umzulegen.
        else:
            self.change_time()
    
    def change_time(self):
        """Verschiebt Pilz, um Uhrzeit zu ändern"""

        # Supi... unser alter "Spezialfall" von 12:00 auf 13:00.
        # Kara geht von uns aus gesehen links außenrum.
        if self.ticks == 1:
            kara.turnRight()
            kara.move()
            kara.turnLeft()
            kara.move()
            kara.turnLeft()
            kara.move()
        # Alle anderen Fälle werden "weitergeleitet".
        else:
            # Alle Fälle? Nein!
            # Falls ein Baum rechts oder links von Kara steht, d.h. sie
            # zwischen zweier der 4 Ecken steht, so muss sie von außen den
            # Pilz verschieben, da dieser sich folgerichtig auf der Ecke vor
            # Kara befindet und daher aus einer anderen Richtung, als der aktuellen
            # Blick- und Bewegungsrichtung Karas angeschoben werden muss.
            if kara.treeLeft() or kara.treeRight():
                kara.turnLeft()
                kara.move()
                kara.turnRight()
                kara.move()
                kara.turnRight()
                kara.move()
            # Jetzt werden aber wirklich alle Fälle "weitergeleitet".
            # Der realistisch gesehen einzige mögliche weitere Fall ist
            # der, bei dem sich Kara auf einer der 4 Ecken befindet und
            # der Pilz zwischen zweien der 4 Ecken. Daher darf hier gar nicht
            # der "Weg von Außen" genutzt werden, sondern schlicht ein Schritt
            # nach vorn, der auf jedenfall von der restricted_tick() nicht 
            # ausgeführt wurde, sonst hätten wir nämlich unerklärbare Probleme.
            else:
                kara.move()

def main():
    """Main-Funktion (Führt das Programm aus)"""

    # Reset des "Schrittzählers". Er wird genutzt, um 
    # zu erkennen, ob es sich um den ersten Schritt Karas handelt, 
    # dieser beinhaltet nämlich einen "Spezialfall".
    # (mir ist bewusst, dass es nach Python-Zen keine "Spezialfälle" gibt...)
    clock.ticks = 0
    # Aufruf der move()-Funktion aus der Clock-Klasse.
    clock.clock_hand_tick()

# Um die Funktionen aus Clock zu nutzen müssen wir sie instanzieren.
clock = Clock()
# Danach beginnt das Elend unserer Sklavin Kara.
main()
