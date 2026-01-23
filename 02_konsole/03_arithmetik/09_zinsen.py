import random as rd

print("Jahresende - Kontoauszug")
kontostand = rd.randrange(100, 1001)
zinssaetze = [0.01, 0.025, 0.03, 0.035, 0.04, 0.05]
zinssatz = rd.choice(zinssaetze)
zinsen = kontostand * zinssatz
neuer_kontostand = kontostand + zinsen
print(f"Kontostand: CHF {kontostand}")
print(f"Zinssatz: {zinssatz * 100} %")
print(f"Zinsen: CHF {zinsen}")
print(f"Neuer Kontostand: CHF {neuer_kontostand}")
print("Danke für Ihr Vertrauen in die Random-Bank")
