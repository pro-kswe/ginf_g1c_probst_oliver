import random as rd

# Liste beginnt mit eckigen Klammern
emotionen = [":-)", ":-(", ":-o", ":-|"]  # Liste
anzahl = rd.randrange(1, 11)
for _ in range(anzahl):
    emotion = rd.choice(emotionen)  # choice benötigt eine Liste
    print(f"Heute geht es mir {emotion} und morgen {emotion}")
