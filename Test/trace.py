print("Aufgabe a): ")

# Iterrationszähler
sd = 0

# Hier den zu "tracenden" Code einfügen:
erg = 0
i = 1

while i <= 3:
    j = 0

    while j <= 2:
        if i != j:
            erg += j
       
        j += 1
    
    i += 1

    sd += 1

    # Am Ende der zu "tracenden" Schleife einfach mit der Print-Funktion
    # ausgeben.
    print("erg = " + str(erg))
    print("j = " + str(j))
    print("i = " + str(i))
    print("SD = " + str(sd))

    input("PRESS ENTER")


# Aufgabe 2
print("Aufgabe b): ")

# Iterationszähler
sd = 0

# Hier den zu "tracenden" Code einfügen:
erg = 0
i = 1

while i <= 3:
    j = i + 1
    
    while j <= 4:
        erg = erg + (i * j)
        j += 1
    i += 1

    sd += 1

    print("erg = " + str(erg))
    print("j = " + str(j))
    print("i = " + str(i))
    print("SD = " + str(sd))

    input("PRESS ENTER")