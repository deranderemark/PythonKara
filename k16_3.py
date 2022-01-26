l = 3
b = 2

# Ausmessung des zu kopierenden Rechtecks.
while not kara.treeFront():
    kara.move()
    b = b + 1

# Ein-/Ausgang auf Höhe 1
if kara.treeRight():
    kara.turnLeft()

    while not kara.treeFront():
        kara.move()
        l = l + 1
# Alle anderen Fälle.
else:
    kara.turnRight()
    
    while not kara.treeFront():
        kara.move()
    
    kara.turnRight()
    kara.turnRight()
    
    while not kara.treeFront():
        kara.move()
        l = l + 1

# Verlassen des zu kopierenden Rechtecks.
kara.turnLeft()

while not kara.treeFront():
    kara.move()

kara.turnLeft()

while kara.treeRight() and not kara.treeFront():
    kara.move()

kara.turnRight()
kara.move()
kara.move()

# Übergabe an den Nachbildungs-Algorithmus.
kara.turnLeft()
kara.move()

while kara.treeLeft():
    kara.move()

kara.turnRight()
kara.turnRight()
kara.move()
kara.turnLeft()

# Nachbildung des Rechtecks
i = 2
while i > 0:
    b_h = b
    l_h = l

    while b_h > 1:
        kara.putLeaf()
        kara.move()
        
        b_h = b_h - 1
    
    kara.turnRight()

    while l_h > 1:
        kara.putLeaf()
        
        kara.move()
            
        l_h = l_h - 1
    
    kara.turnRight()

    i = i - 1

# Ab hier nur noch Änderung von Karas Endposition.
kara.turnRight()

while kara.treeRight():
    kara.move()

kara.removeLeaf()

kara.turnLeft()