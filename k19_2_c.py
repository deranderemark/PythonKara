position = []
i = 1
while i <= 4:
    kara.move()
    if kara.onLeaf():
        position.append(kara.getPosition())
        
    i = i + 1
    anzahl = len(position)

tools.showMessage(str(position))
tools.showMessage(str(anzahl))