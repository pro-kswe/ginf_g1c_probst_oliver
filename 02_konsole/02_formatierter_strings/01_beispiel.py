import random as rd

# Zufallszahl zwischen 1 und 6
note = rd.randrange(1, 7)
# Eckige Klammer bedeutet Liste
# Eine Liste speichert mehrere Strings oder Ints
faecher = ["Informatik", "Mathematik", "Deutsch"]
# choice wählt in einer Liste zufällig ein Element aus
# Element kann ein String oder Int sein
fach = rd.choice(faecher)
# f steht für formatierter String
print(f"Notenwürfel für das Fach {fach}")
print(f"Ihre gewürfelte Note lautet: {note}")
