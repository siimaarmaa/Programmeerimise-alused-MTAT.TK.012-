# Funktsioon kuu_nimi, mis tagastab kuu nime kuu järjekorranumbri põhjal
def kuu_nimi(kuu_nr):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni",
            "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[kuu_nr - 1]  # Tagastame õige kuu nime järjendist

# Funktsioon kuupäev_sõnena, mis teisendab kuupäeva sõne kujule
def kuupäev_sõnena(kuupäev):
    osad = kuupäev.split(".")  # Jagame kuupäeva päevaks, kuuks ja aastaks
    päev = osad[0]
    kuu = kuu_nimi(int(osad[1]))  # Kasutame kuu_nimi funktsiooni, et saada kuu nimi
    aasta = osad[2]
    return f"{päev}. {kuu} {aasta}. a"  # Koostame ja tagastame soovitud kuupäeva kujul

# Peaprogramm
# Küsime kasutajalt kuupäeva kujul "DD.MM.YYYY"
sisestatud_kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

# Kasutame funktsiooni kuupäev_sõnena ja väljastame tulemuse
kuupäev_sõnena_kujul = kuupäev_sõnena(sisestatud_kuupäev)
print("Kuupäev sõnena:", kuupäev_sõnena_kujul)
