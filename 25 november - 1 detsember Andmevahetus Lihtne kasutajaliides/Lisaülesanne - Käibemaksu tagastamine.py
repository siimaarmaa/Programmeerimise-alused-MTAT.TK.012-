def hind_käibemaksuga(kmta_hind, km_protsent):
    # Arvutame käibemaksuga hinna
    return kmta_hind * (1 + km_protsent / 100)

def main():
    # Küsi kasutajalt failinimi, käibemaksu protsent ja summa, millest alates saab käibemaksu tagasi
    failinimi = input("Sisestage failinimi: ")
    km_protsent = float(input("Sisestage riigi käibemaks: "))
    summa_taggasi = float(input("Sisestage summa, millest alates saab käibemaksu tagasi: "))

    try:
        # Loe failist ilma käibemaksuta hinnad
        with open(failinimi, encoding="utf-8") as fail:
            hinnad = [float(rida.strip()) for rida in fail]
    except FileNotFoundError:
        print(f"Faili '{failinimi}' ei leitud.")
        return

    # Arvuta hinnad koos käibemaksuga ja kogu summa
    kmga_hinnad = [hind_käibemaksuga(hind, km_protsent) for hind in hinnad]
    kokku_summa = round(sum(kmga_hinnad), 2)
    print(f"Kokku on kulutatud: {kokku_summa}")

    # Arvuta tagasi saadav käibemaksu summa
    tagastatav_summa = sum(hind for hind in kmga_hinnad if hind > summa_taggasi)
    tagasi_kaibemaks = round(tagastatav_summa - tagastatav_summa / (1 + km_protsent / 100), 2)
    print(f"Tagasi saab: {tagasi_kaibemaks}")

if __name__ == "__main__":
    main()
