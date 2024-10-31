import random

# Küsi kasutajalt vajalike täringute arvu
taringute_arv = int(input("Palun sisesta vajalike täringute arv: "))

# Viskame vastava arvu täringuid ja väljastame tulemused
for i in range(taringute_arv):
    tulemus = random.randint(1, 6)
    print("Täringu viske tulemus:", tulemus)
