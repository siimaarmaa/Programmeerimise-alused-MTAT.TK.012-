# Küsime kasutajalt failinime
faili_nimi = input("Sisesta failinimi: ")

# Loeme faili sisu
with open(faili_nimi, "r", encoding="utf-8") as fail:
    sonum = fail.read()

# Teeme vajalikud asendused ja muudame kõik tähed suurtähtedeks
telegrammi_sonum = (
    sonum.replace("Ä", "AE")
         .replace("ä", "AE")
         .replace("Õ", "OE")
         .replace("õ", "OE")
         .replace("Ö", "OE")
         .replace("ö", "OE")
         .replace("Ü", "UE")
         .replace("ü", "UE")
         .upper()
)

# Väljastame sõnumi telegrammi stiilis
print("Telegrammi stiilis sõnum:")
print(telegrammi_sonum)
