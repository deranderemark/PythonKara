n = 5                 #value determines height and width of our desired triangle
for height in range(0, n, 1):     #sets the boundries for the maximus heigt of our triangle in single steps
  for width in range(0, height+1, 2):      #sets the boundries for the width of our triangle, which is dependant on our height and therefore n-variable
    world.setLeaf(height, width, True)     # places the leafes to form our desired triangle
