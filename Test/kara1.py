# BEFEHLE:  kara.
#   move()  turnRight()  turnLeft()
#   putLeaf()  removeLeaf()
#
# SENSOREN: kara.
#   treeFront()  treeLeft()  treeRight()
#   mushroomFront()  onLeaf()

# Variablen
Leaf_Sum = 6

# Methoden | turn_lf muss noch optimiert werden; bleibt in Ecke unten links h�ngen
def turn_around(self):
	kara.turnRight()
	kara.turnRight() 

def check_leaf(leaf_sum):
	if kara.onLeaf():
		kara.removeLeaf()
		leaf_sum -= 1
		return leaf_sum
	else:
		pass
		return leaf_sum


# Automatisiertes Bewegen und Einsammeln
while Leaf_Sum > 0:
	if not kara.treeFront():
		kara.move()
		Leaf_Sum = check_leaf(Leaf_Sum)
	elif not kara.treeLeft():
		kara.turnLeft()
	elif not kara.treeRight():
		kara.turnRight()
	else:
		turn_around()