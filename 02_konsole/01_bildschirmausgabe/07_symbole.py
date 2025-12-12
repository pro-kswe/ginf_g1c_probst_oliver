import random as rd

# Variante A
symbole = ["****", "€€€€", "$$$$"]
symbol = rd.choice(symbole)
for _ in range(4):
    print(symbol)

# Variante B
symbole = ["*", "€", "$"]
symbol = rd.choice(symbole)
for _ in range(4):
    print(4 * symbol)
