import PIL.Image as img
import random as rd

bild = img.new("RGB", (256, 256))

for x in range(0, bild.width):
    for y in range(0, bild.height):
        r = x
        g = x
        b = x
        bild.putpixel((x, y), (r, g, b))
        
bild.save("06_graustufen_ergebnis.png")
