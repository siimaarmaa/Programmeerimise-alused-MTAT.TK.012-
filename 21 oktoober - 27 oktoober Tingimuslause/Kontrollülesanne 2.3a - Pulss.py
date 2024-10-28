# Küsi kasutajalt vanus, sugu ja treeningu tüüp
vanus = int(input("Sisesta oma vanus aastates: "))
sugu = input("Sisesta oma sugu (M/m meestele, N/n naistele): ").lower()
treening_tyyp = int(input("Sisesta treeningu tüüp (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening): "))

# Maksimaalse pulsisageduse arvutamine
if sugu == 'm':
    max_pulsisagedus = 220 - vanus
elif sugu == 'n':
    max_pulsisagedus = 206 - (0.88 * vanus)
else:
    print("Vigane sisestus soo osas.")
    exit()  # Lõpeta programm, kui sisestus on vale

# Treeningu tüübi järgi pulsisageduse vahemiku määramine
if treening_tyyp == 1:
    minimaalne_pulss = round(0.50 * max_pulsisagedus)
    maksimaalne_pulss = round(0.70 * max_pulsisagedus)
elif treening_tyyp == 2:
    minimaalne_pulss = round(0.70 * max_pulsisagedus)
    maksimaalne_pulss = round(0.80 * max_pulsisagedus)
elif treening_tyyp == 3:
    minimaalne_pulss = round(0.80 * max_pulsisagedus)
    maksimaalne_pulss = round(0.87 * max_pulsisagedus)
else:
    print("Vigane sisestus treeningu tüübi osas.")
    exit()  # Lõpeta programm, kui sisestus on vale

# Väljasta pulsisageduse vahemik
print(f"Sinu soovitatav pulsisagedus on: {minimaalne_pulss} kuni {maksimaalne_pulss}")
