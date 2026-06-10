import PIL.Image as img
import random as rd

bild = img.new("RGB", (1000, 1000))

for x in range(0, bild.width):
    for y in range(0, bild.height):
        r = (x // 30 * 40) % 256
        g = (y // 30 * 60) % 256
        b = ((x + y) // 30 * 20) % 256
        bild.putpixel((x, y), (r, g, b))
        
bild.save("08_verlauf_2_ergebnis.png")
