class Copier(object):
    # Ermittlung der Groesse der Welt
    # Beachte: Nullbasierte Numerierung
    size_x = world.getSizeX()
    size_y = world.getSizeY()

    # Baumliste
    # X- durch " " von Y-Koordinate getrennt.
    tree_locations = []

    # Finden und Speichern der Position der Baeume
    def parse_trees(self):
        # Jedes Feld wird nach einem Baum abgesucht.
        for x in range(0, self.size_x, 1):
            for y in range(0, self.size_y, 1):
                if world.isTree(x, y):
                    # Alle gefundenen Baeume werden in einer Liste gespeichert.
                    self.tree_locations.append(str(x) + " " + str(y))

        return self.tree_locations

    # Ermittlung des ersten Baumes "tree0".
    def locate_tree0(self):
        pos_tree0 = self.tree_locations[0].strip()
        
        # Zweistellige Zahlen werden leider in der Liste in ihre
        # Einzelzahlen zerlegt, daher muessen ggf. die ersten beiden
        # Zahlen in der Liste zu einer Zusammengefügt werden.
        if pos_tree0[1] != " ":
            x_tree0 = int(pos_tree0[0] + "" + pos_tree0[1])
            y_tree0 = pos_tree0[2]
        else:
            x_tree0 = int(pos_tree0[0])
            y_tree0 = pos_tree0[1]
        
        return [x_tree0, y_tree0]

    # Achsenspieglung der Baeume.
    def copy(self):
        # Erkennung, ob überhaupt Bäume in der Welt sind.
        if len(self.parse_trees()) <= 0:
            tools.showMessage("ERROR: There are no trees to copy in your world!")

        # Ermittlung der Spiegelachse über den "tree0".
        mirror_axis = self.locate_tree0()[0] - 1

        # Momentan funktioniert Copier.copy() nur von rechts nach links.
        # Dadurch, dass der "tree0" in der rechten Hälfte der Welt sein muss
        # wird Fehlern vorgebeugt, die aus zu wenig Platz resultieren. 
        if (int(self.locate_tree0()[0]) - 1) >= (self.size_x / 2):
            # Jeder Baum in der Liste wird kopiert.
            for tree in range(0, len(self.tree_locations), 1):
                pos_org = self.tree_locations[tree].strip()

                # Auch hier wird nach ein- und zweistelligen Zahlen unterschieden.
                if pos_org[1] != " ":
                    x_org = int(pos_org[0] + "" + pos_org[1])

                    if len(self.tree_locations) == 5:
                        y_org = int(pos_org[3] + "" + pos_org[4])
                    else:
                        y_org = int(pos_org[3])
                else:
                    x_org = int(pos_org[0])
                    
                    if len(self.tree_locations) == 4:                
                        y_org = int(pos_org[2] + "" + pos_org[3])
                    else:
                        y_org = int(pos_org[2])
                
                # Die neuen Koordinaten für die Kopie wird über die Spiegel-
                # achse berechnet.
                x_mirror = (mirror_axis - (x_org - mirror_axis)) + 1
                # Bei der Achsenspieglung entsprechen sich ursrpüngliche und
                # neue Y-Koordinate.
                y_mirror = y_org

                # Schließlich wird der Baum durch ein Kleeblatt kopiert.
                world.setLeaf(x_mirror, y_mirror, True)

            return [x_mirror, y_mirror]
        else:
            return "ERROR"

def main():
    if copier.copy() == "ERROR":
        tools.showMessage("ERROR")


copier = Copier()
main()

# Damit Pythonkara das Programm beenden kann.
tools.checkState()