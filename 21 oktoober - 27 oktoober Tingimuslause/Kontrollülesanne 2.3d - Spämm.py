# Küsi kasutajalt kirja suurust megabaitides
kirja_suurus = float(input("Sisesta kirja suurus megabaitides: "))

# Küsi kasutajalt teema pealkirja (võib olla tühi)
teema_pealkiri = input("Sisesta teema pealkiri (võib olla tühi): ").strip()

# Küsi kasutajalt, kas kirjaga on kaasas fail
kas_manus = input("Kas kirjaga on kaasas fail? (jah/ei): ").strip().lower()

# Kontrolli tingimusi ühe tingimuslausega
if teema_pealkiri == "" or (kas_manus == "jah" and kirja_suurus > 1.0):
    print("Kiri on spämm.")
else:
    print("Kiri ei ole spämm.")
