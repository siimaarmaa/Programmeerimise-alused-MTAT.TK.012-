# Funktsioon banner, mis võtab argumendiks reklaamlause ja tagastab selle suurtähtedega
def banner(reklaamlause):
    return reklaamlause.upper()

# Peaprogramm
# Küsime kasutajalt, mitu korda soovitakse reklaamlauset kuvada
kordade_arv = int(input("Mitu korda soovid reklaamlauset kuvada? "))

# Küsime kasutajalt, millist reklaamlauset ta soovib kasutada
reklaamlause = input("Sisesta reklaamlause: ")

# Kuvame reklaamlause kasutaja soovitud arv kordi, kutsudes iga kord välja banner-funktsiooni
for i in range(kordade_arv):
    print(banner(reklaamlause))
