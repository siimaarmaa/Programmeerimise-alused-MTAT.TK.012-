from datetime import datetime

# Küsime kasutajalt ühe päevikusissekande
sissekanne = input("Sisesta päevikusissekanne: ")

# Saame praeguse kuupäeva ja kellaaja
kuupäev_kellaeg = datetime.today()

# Avame faili 'paevik.txt' ja kirjutame sissekande lõppu
with open("paevik.txt", "a", encoding="utf-8") as fail:
    # Kirjutame faili praeguse kuupäeva ja kellaaja
    fail.write(str(kuupäev_kellaeg) + "\n")
    # Kirjutame faili kasutaja sisestatud sissekande
    fail.write(sissekanne + "\n")
    # Lisame tühja rea
    fail.write("\n")

print("Sissekanne lisatud päevikusse.")
