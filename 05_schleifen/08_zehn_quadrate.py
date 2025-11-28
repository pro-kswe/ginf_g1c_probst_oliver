import turtle as t
import random as rd

farbe = "blue"
t.pencolor(farbe)
stärke = rd.randrange(1, 6)
t.pensize(stärke)
a = rd.randrange(25, 51)
for _ in range(10):
    for _ in range(4):
        t.fd(a)
        t.lt(90)
    t.fd(a)
