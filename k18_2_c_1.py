n = 5

x = 0
while x != n:
    y = 0
    while y != n:
        world.setLeaf(x, x, True)
        y = y + 1
    x = x + 1