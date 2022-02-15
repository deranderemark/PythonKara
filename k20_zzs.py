belegt = [0] * 4

i = 0
while i <= 3:
  kara.move()
  if kara.onLeaf():
    kara.removeLeaf()
    belegt[i] = 1
i = i + 1

kara.turnLeft()
kara.turnLeft()

i = 0
while i <= 3:
  if belegt[i-3] == 1:
    kara.putLeaf()
  kara.move()
i = i + 1
      
