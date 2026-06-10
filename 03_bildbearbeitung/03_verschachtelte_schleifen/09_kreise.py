import PIL.Image as img
import random as rd

bild = img.new("RGB", (1000, 1000))

for x in range(0, bild.width):
    for y in range(0, bild.height):
        r = (x * x + y * y) % 256
        g = (x * x + y * y) % 256
        b = (x * x + y * y) % 256
        bild.putpixel((x, y), (r, g, b))
        
bild.save("09_kreise_ergebnis.png")
