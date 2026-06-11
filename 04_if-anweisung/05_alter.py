alter = int(input("Wie alt sind Sie?"))

print(f"Sie sind {alter} Jahre alt.")

if alter < 14:
    print("Sie dürfen noch kein Fahrzeug führen.")

if alter == 14:
    print("Fahrzeuge der Kategorie M und G.")

if alter == 15:
    print("Fahrzeuge der Kategorie M und G.")
    print("Kleine Fahrzeuge der Kategorie A1.")

if alter == 16:
    print("Fahrzeuge der Kategorie M und G.")
    print("Alle Fahrzeuge der Kategorie A1.")

if alter == 17:
    print("Fahrzeuge der Kategorie M und G.")
    print("Alle Fahrzeuge der Kategorie A1.")
    print("Fahrzeuge der Kategorie B mit Begleitung.")

if alter > 17:
    print("Fahrzeuge der Kategorie M und G.")
    print("Alle Fahrzeuge der Kategorie A1.")
    print("Fahrzeuge der Kategorie B.")
    