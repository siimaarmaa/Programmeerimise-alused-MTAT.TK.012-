# Avame faili lugemiseks
with open("konto.txt", "r") as fail:
    # Käime läbi kõik failis olevad read
    for rida in fail:
        # Muudame rea ujukomaarvuks ja eemaldame tühikud
        arv = float(rida.strip())
        
        # Kui arv on positiivne, siis väljastame selle ekraanile
        if arv > 0:
            print(arv)
