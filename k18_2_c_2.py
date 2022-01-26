n = 5

x = 0
while x != n:
    y = x
    while y != n:
        world.setLeaf(x, y, True)
        y = y + 1
    x = x + 1
    
    tools.showMessage(str(x))