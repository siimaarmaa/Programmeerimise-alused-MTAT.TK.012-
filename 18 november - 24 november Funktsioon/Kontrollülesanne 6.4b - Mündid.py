# Funktsioon pronksikarva_summa, mis arvutab pronksikarva müntide summa
def pronksikarva_summa(myndid):
    summa = 0
    for mynt in myndid:
        if mynt in [1, 2, 5]:  # Kontrollime, kas münt on pronksikarva väärtusega
            summa += mynt
    return summa

# Peaprogramm
# Küsime kasutajalt faili nime, kus on müntide väärtused
faili_nimi = input("Sisesta faili nimi, kus asuvad sentide väärtused: ")

# Loeme faili ja moodustame järjendi täisarvudest
with open(faili_nimi, "r") as fail:
    sentide_vaartused = [int(rida.strip()) for rida in fail]

# Rakendame funktsiooni pronksikarva_summa ja arvutame pronksikarva müntide kogusumma
pronks_summa = pronksikarva_summa(sentide_vaartused)

# Väljastame pronksikarva müntide summa
print("Pronksikarva sentide summa on:", pronks_summa)
