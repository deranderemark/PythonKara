seite = 5
for height in range(0, seite, 1):
  for width in range(0, height + 1, 2):
    world.setLeaf(height, width, True)