# Küsime kasutajalt teepikkuse koju kilomeetrites
teepikkus = float(input("Sisesta teepikkus koju kilomeetrites: "))

# Avame faili ja loeme andmed
fail = open("taksohinnad.txt", encoding="UTF-8")

# Muutujad odavaima takso ja hinna hoidmiseks
odavaim_takso = None
odavaim_hind = float('inf')

# Käime faili read läbi
for rida in fail:
    # Jagame rea komade järgi osadeks
    osad = rida.strip().split(',')
    takso_nimi = osad[0]
    sisseistumise_hind = float(osad[1])
    kilomeetri_hind = float(osad[2])
    
    # Arvutame sõidu koguhinna
    koguhind = sisseistumise_hind + (kilomeetri_hind * teepikkus)
    
    # Kontrollime, kas leitud hind on odavaim
    if koguhind < odavaim_hind:
        odavaim_hind = koguhind
        odavaim_takso = takso_nimi

# Sulgeme faili
fail.close()

# Väljastame odavaima takso nime
print(f"Kõige odavam takso on: {odavaim_takso}")
