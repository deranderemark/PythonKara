# BEFEHLE:  kara.
#   move()  turnRight()  turnLeft()
#   putLeaf()  removeLeaf()
#
# SENSOREN: kara.
#   treeFront()  treeLeft()  treeRight()
#   mushroomFront()  onLeaf()

# Methoden
def turn_around(n):
	if n > 0:
		kara.turnRight()
		kara.turnRight()
		for i in range(n):
		  kara.move()
	else:
		kara.move()

def check_leaf():
	if kara.onLeaf():
		kara.removeLeaf()
	else:
		kara.putLeaf()

def seq_1(i, n):
    turn_around(i)
    check_leaf()
    turn_around(n)

def seq_2(i, n):
    kara.putLeaf()
    turn_around(i)
    turn_around(n)


#while True:
seq_1(0, 1)
seq_1(2, 2)
seq_1(2, 0)
seq_2(4, 1)