# NOT WORKING: in Development

n = 5
poslist = []

for x in range(0, n, 1):
    for y in range(0, n, 1):
        if (y % 2) == 0:
            poslist.append([x, y])
            world.setLeaf(x, y, True)

for pos in poslist:
    world.setLeaf(pos[0], pos[1], True)
