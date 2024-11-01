# Küsime kasutajalt eesnime(d) ja perekonnanime
nimi = input("Sisesta eesnimi(d) ja perekonnanimi: ")

# Jagame sisestatud nime sõnadeks
nimi_osad = nimi.split()

# Eeldame, et viimane sõna on perekonnanimi
perekonnanimi = nimi_osad[-1]

# Ülejäänud osad on eesnimed
eesnimed = nimi_osad[:-1]

# Koostame eesnimede lühendid
eesnimede_luhendid = []
for eesnimi in eesnimed:
    if '-' in eesnimi:
        # Kui eesnimes on sidekriips, võtame esimese tähe mõlemast osast
        osad = eesnimi.split('-')
        luhend = osad[0][0] + '-' + osad[1][0]
    else:
        # Kui eesnimes pole sidekriipsu, võtame lihtsalt esimese tähe
        luhend = eesnimi[0]
    eesnimede_luhendid.append(luhend + '.')

# Ühendame lühendid tühikuga
luhendid_koos = ' '.join(eesnimede_luhendid)

# Väljastame perekonnanimi ja eesnimede lühendid
print(f"{perekonnanimi} {luhendid_koos}")
