baum1 = False
baum2 = False
baum3 = False
baum4 = False
baum5 = False

i = 1
while i <= 4:
    if kara.onLeaf():
        if i == 1:
            baum1 = True
            kara.removeLeaf()
        elif i == 2:
            baum2 = True
            kara.removeLeaf()
        elif i == 3:
            baum3 = True
            kara.removeLeaf()
        elif i == 4:
            baum4 = True
            kara.removeLeaf()
        elif i == 5:
            baum5 = True
            kara.removeLeaf()
    
    kara.move()
    i = i + 1

kara.turnRight()
kara.turnRight()

i = 1

while i <= 4:
    if i == 1 and baum5:
        kara.putLeaf()
    elif i == 2 and baum4:
        kara.putLeaf()
    elif i == 3 and baum3:
        kara.putLeaf()
    elif i == 4 and baum2:
        kara.putLeaf()
    elif i == 5 and baum1:
        kara.putLeaf()
    
    kara.move()
    i = i + 1