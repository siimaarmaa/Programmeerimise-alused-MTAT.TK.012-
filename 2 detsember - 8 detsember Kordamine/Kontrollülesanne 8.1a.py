def juurdekasv(pindala_aakrites, juurdekasv_hektari_kohta):
    # Arvutame metsatüki juurdekasvu ja ümardame sajandikeni
    return round(pindala_aakrites * 0.4047 * juurdekasv_hektari_kohta, 2)

def main():
    # Küsi kasutajalt failinimi, puuliigi aastane juurdekasv ja pindala piir
    failinimi = input("Sisestage failinimi: ")
    juurdekasv_hektari_kohta = float(input("Sisestage puuliigi aastane juurdekasv hektari kohta (tm/ha): "))
    pindala_piir = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

    try:
        # Loe failist metsatükkide pindalad
        with open(failinimi, encoding="utf-8") as fail:
            pindalad = [float(rida.strip()) for rida in fail]
    except FileNotFoundError:
        print(f"Faili '{failinimi}' ei leitud.")
        return

    arvutatud_juurdekasvude_arv = 0

    # Arvuta ja väljastame metsatükkide juurdekasvu, kui pindala on suurem kui piir
    for pindala in pindalad:
        if pindala > pindala_piir:
            kasv = juurdekasv(pindala, juurdekasv_hektari_kohta)
            print(f"Metsatüki pindala: {pindala} aakrit, aastane juurdekasv: {kasv} tm")
            arvutatud_juurdekasvude_arv += 1
        else:
            print(f"Metsatükki ei võeta arvesse (pindala: {pindala} aakrit)")

    # Väljastame kokkuvõtte
    print(f"Arvutati {arvutatud_juurdekasvude_arv} metsatüki juurdekasv.")

if __name__ == "__main__":
    main()
