n = 5

for x in range(0, n, 1):
    for y in range(0, n, 1):
        if (y % 2) == 0:
            world.setLeaf(x, y, True)