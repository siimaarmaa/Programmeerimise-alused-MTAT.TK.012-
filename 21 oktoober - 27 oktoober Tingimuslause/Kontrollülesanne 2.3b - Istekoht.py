import random

# Küsi kasutajalt, kas ta soovib istekohta ise valida või lasta loosida
valik = input("Kas soovid istekoha ise valida või lasta loosida? (sisesta 'ise' või 'loos'): ").strip().lower()

if valik == "ise":
    # Kasutaja valib ise istekoha
    istekoht = input("Kas soovid istuda akna ääres või mitte? (sisesta 'aken' või 'muu'): ").strip().lower()

    if istekoht == "aken":
        print("Valisite ise.")
        print("Aknakoht.")
    elif istekoht == "muu":
        print("Valisite ise.")
        print("Vahekäigukoht.")
    else:
        print("Vigane sisestus.")
elif valik == "loos":
    # Kasutaja valis loosi
    loosi_tulemus = random.randint(1, 3)  # Loositakse number 1 kuni 3
    if loosi_tulemus == 1:
        print("Istekoht loositi.")
        print("Aknakoht.")
    else:
        print("Istekoht loositi.")
        print("Vahekäigukoht.")
else:
    print("Vigane sisestus.")
