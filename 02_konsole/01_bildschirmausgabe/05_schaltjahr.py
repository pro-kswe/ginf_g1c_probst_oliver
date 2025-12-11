import random as rd
import calendar as cal

jahr = rd.randrange(1900, 2026)
print("Zufälliges Jahr:")
print(jahr)
antwort = cal.isleap(jahr)
print("Ist es ein Schaltjahr?")
print(antwort)
