 import random as rd

print("Würfelspass!")
zahl = rd.randrange(1, 10)
print(f"Sie haben eine {zahl} gewürfelt.")

if zahl > 5:
    print("Sie dürfen gleich nochmal würfeln.")
