import PIL.Image as img
import random as rd

bild = img.new("RGB", (256, 256))

for x in range(0, bild.width):
    for y in range(0, bild.height):
        r = x
        g = x
        b = 128
        bild.putpixel((x, y), (r, g, 128))
        
bild.save("07_verlauf_1_ergebnis.png")
