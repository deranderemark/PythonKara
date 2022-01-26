l = 0
b = 0


while not kara.treeFront():
    kara.move()

    l = l + 1

kara.turnRight()

while not kara.treeFront():
    kara.move()

kara.turnRight()
kara.turnRight()

while not kara.treeFront():
    kara.move()

    b = b + 1

if l % 2 == 0:
    l = l + 1

l_hilf = l

while l_hilf > 0:
    for i in range(0, b, 1): # Sorry, ging sonst nicht anders...
        if not kara.treeFront():
            kara.move()
    
    if l % 2 == 0:
        kara.turnRight()

        if not kara.treeFront():
            kara.move()

        kara.turnRight()
    else:
        kara.turnLeft()

        if not kara.treeFront():
            kara.move()

        kara.turnLeft()
        
    l_hilf = l_hilf - 1

while (kara.treeLeft() or kara.treeRight()) and not kara.treeFront():
    kara.move()

    if kara.treeRight():
        x = 0
    
if x == 0:
    kara.turnRight()
    kara.move()
else:
    kara.turnLeft()
    kara.move()