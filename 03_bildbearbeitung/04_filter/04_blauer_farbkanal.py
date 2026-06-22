import PIL.Image as img

bild = img.open("portland.png")

for x in range(0, bild.width):
    for y in range(0, bild.height):
        r, g, b = bild.getpixel((x, y))
        
        r_neu = 0
        g_neu = 0
        b_neu = b
        
        bild.putpixel((x, y), (r_neu, g_neu, b_neu))
bild.save("03_grüner_farbkanal_ergebnis.png")
