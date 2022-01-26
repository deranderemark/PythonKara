# BEFEHLE:  kara.
#   move()  turnRight()  turnLeft()
#   putLeaf()  removeLeaf()
#
# SENSOREN: kara.
#   treeFront()  treeLeft()  treeRight()
#   mushroomFront()  onLeaf()

# Variablen
max_leaf_sum = 3


# Methoden
def check_leaf(mls):
	if kara.onLeaf():
		kara.removeLeaf()
		mls -= 1
		return mls
	else:
		return mls

def main(mls):
	while mls > 0:
		if not kara.treeFront():
			kara.move()
			mls = check_leaf(mls)
		elif not kara.treeRight():
			kara.turnRight()
			kara.move()
			mls = check_leaf(mls)
		elif not kara.treeLeft:
			kara.turnLeft()
			kara.move()
			mls = check_leaf(mls)
		else:
			kara.turnRight()
			kara.turnRight()

main(max_leaf_sum)