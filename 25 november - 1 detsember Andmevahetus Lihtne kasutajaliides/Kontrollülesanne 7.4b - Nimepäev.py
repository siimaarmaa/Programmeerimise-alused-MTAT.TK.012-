import requests

def main():
    # Küsi kasutajalt kuunime ja päeva
    kuunimi = input("Sisesta kuu nimi (nt. jaanuar, veebruar, marts jne.): ")
    paev = int(input("Sisesta päeva järjekorranumber: "))
    
    # Koosta URL vastavalt kuunimele
    url = f"https://courses.cs.ut.ee/2024/eprogalused/Main/Kontroll-failistfaili2?action=download&upname={kuunimi}"
    
    try:
        # Laadi andmed URL-ilt
        response = requests.get(url)
        response.raise_for_status()  # Kontrolli, kas päring oli edukas
        
        # Loe nimepäevad ja koosta järjend
        nimepaevad = response.text.splitlines()
        
        # Väljastame sisestatud päevale vastavad nimepäevalised
        if 1 <= paev <= len(nimepaevad):
            print(f"{kuunimi} {paev}. nimepäevalised: {nimepaevad[paev - 1]}")
        else:
            print("Sisestatud päev ei ole kehtiv.")
    except requests.exceptions.RequestException:
        print("Andmete lugemine ebaõnnestus. Kontrolli URL-i või proovi hiljem uuesti.")

if __name__ == "__main__":
    main()
