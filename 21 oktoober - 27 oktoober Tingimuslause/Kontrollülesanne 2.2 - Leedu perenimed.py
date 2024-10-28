# Küsi kasutajalt Leedu perekonnanime
nimi = input("Sisesta Leedu perekonnanimi: ")

# Kontrolli nime lõppu ja anna sobiv teade
if nimi[-2:] == "ne":
    print("Abielus.")
elif nimi[-2:] == "te":
    print("Vallaline.")
elif nimi[-1] == "e":
    print("Määramata.")
else:
    print("Pole ilmselt leedulanna perekonnanimi.")
