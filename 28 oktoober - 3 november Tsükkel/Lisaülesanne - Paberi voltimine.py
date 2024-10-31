# Küsi kasutajalt, mitu korda paberit voltida (mittenegatiivne täisarv)
voltimiste_arv = int(input("Palun sisesta, mitu korda soovid paberit voltida: "))

# Algväärtustame paberi paksuse (algne paksus 0,01 cm)
paberi_paksus = 0.01  # cm

# Arvuta paberi paksus pärast kõiki voltimisi, kasutades while-tsüklit
korrad = 0
while korrad < voltimiste_arv:
    paberi_paksus *= 2
    korrad += 1

# Teisenda paberi paksus vastavalt meetriteks või jäta sentimeetriteks
if paberi_paksus > 100:
    paberi_paksus_meetrites = paberi_paksus / 100  # teisenda cm-st meetriteks
    # Ümarda paberi paksus kahe komakohani
    paberi_paksus_meetrites = round(paberi_paksus_meetrites, 2)
    print("Paberi paksus on", paberi_paksus_meetrites, "meetrit.")
else:
    # Ümarda paberi paksus kahe komakohani
    paberi_paksus = round(paberi_paksus, 2)
    print("Paberi paksus on", paberi_paksus, "sentimeetrit.")
