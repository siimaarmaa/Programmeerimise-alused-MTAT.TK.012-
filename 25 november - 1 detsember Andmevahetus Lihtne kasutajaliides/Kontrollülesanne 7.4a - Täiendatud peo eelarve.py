def eelarve(kulaliste_arv):
    # Eelarve arvutamine: iga külaline 10€ ja ruumi rent 55€
    return kulaliste_arv * 10 + 55

def loe_failist_kulalised(failinimi):
    kutsutud = 0
    tulevad = 0
    try:
        with open(failinimi, encoding='utf-8') as fail:
            for rida in fail:
                rida = rida.strip()
                if rida.startswith('+'):
                    tulevad += 1
                if rida.startswith('+') or rida.startswith('?'):
                    kutsutud += 1
    except FileNotFoundError:
        print(f"Faili '{failinimi}' ei leitud.")
        return None, None
    return kutsutud, tulevad

def main():
    failinimi = input("Sisesta külaliste failinimi: ")
    kutsutud, tulevad = loe_failist_kulalised(failinimi)
    
    if kutsutud is not None and tulevad is not None:
        print(f"Kutsutud inimesi kokku: {kutsutud}")
        print(f"Tulemisest on teatanud: {tulevad}")
        
        maksimaalne_eelarve = eelarve(kutsutud)
        minimaalne_eelarve = eelarve(tulevad)
        
        print(f"Maksimaalne eelarve: {maksimaalne_eelarve} eurot")
        print(f"Minimaalne eelarve: {minimaalne_eelarve} eurot")

if __name__ == "__main__":
    main()