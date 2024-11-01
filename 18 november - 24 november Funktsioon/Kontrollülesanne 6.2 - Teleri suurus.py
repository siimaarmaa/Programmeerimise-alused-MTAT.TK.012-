# Funktsioon teleri_diagonaal, mis arvutab teleri sobiva diagonaali tollides
def teleri_diagonaal(kaugus):
    diagonaal = kaugus * 100 * 0.39 / 2.5  # Arvutame diagonaali tollides
    return round(diagonaal)  # Tagastame ümardatud väärtuse täisarvuni

# Peaprogramm
# Küsime kasutajalt kauguse diivanist telerini meetrites
kaugus = float(input("Sisesta kaugus diivanist telerini meetrites: "))

# Kasutame funktsiooni teleri_diagonaal ja väljastame tulemuse ekraanile
sobiv_diagonaal = teleri_diagonaal(kaugus)
print("Sobiv teleri diagonaal on:", sobiv_diagonaal, "tolli")
