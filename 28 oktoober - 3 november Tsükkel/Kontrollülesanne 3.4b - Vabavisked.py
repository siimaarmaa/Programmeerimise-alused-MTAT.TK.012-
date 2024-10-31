import random

# Küsi kasutajalt visketabavuse protsentides (täisarv 0 kuni 100)
tabavuse_protsent = int(input("Palun sisesta visketabavuse protsentides (0 kuni 100): "))

# Algväärtustame muutujad
visete_arv = 1000
tabanud_visked = 0
praegune_vise = 0

# Simuleerime 1000 viset while-tsükli abil
while praegune_vise < visete_arv:
    if random.randint(1, 100) <= tabavuse_protsent:
        print("Vise tabas")
        tabanud_visked += 1
    else:
        print("Vise mööda")
    praegune_vise += 1

# Väljastame kokku tabanud visete arvu
print("Kokku tabas", tabanud_visked, "viset.")
