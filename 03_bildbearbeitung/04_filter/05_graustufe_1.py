import PIL.Image as img

bild = img.open("portland.png")

for x in range(0, bild.width):
    for y in range(0, bild.height):
        r, g, b = bild.getpixel((x, y))

        graustufe = (r + g + b) // 3
        
        bild.putpixel((x, y), (graustufe, graustufe, graustufe))
bild.save("05_graustufe_1.png")
