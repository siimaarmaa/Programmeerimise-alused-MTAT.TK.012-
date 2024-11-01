#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))

def main():
    # Ava fail ja loe sünnikuupäevad
    try:
        with open("sunnikuupaevad.txt", encoding="utf-8") as fail:
            sunnikuupaevad = fail.read().splitlines()
    except FileNotFoundError:
        print("Faili 'sunnikuupaevad.txt' ei leitud.")
        return

    # Loo 9 failinime vastavalt elutee numbritele
    failid = [open(f"eluteenumber{i}.txt", "w", encoding="utf-8") for i in range(1, 10)]

    # Jaota sünnikuupäevad vastavalt elutee numbrile
    for kuupaev in sunnikuupaevad:
        number = elutee(kuupaev)
        failid[number - 1].write(kuupaev + "\n")

    # Sulge kõik loodud failid
    for fail in failid:
        fail.close()

if __name__ == "__main__":
    main()