# Küsi kasutajalt lause, mida ta soovib mantrana kasutada
mantra = input("Palun sisesta mantra: ")

# Küsi kasutajalt, mitu korda ta soovib mantrat korrata
korduste_arv = int(input("Mitu korda soovid mantrat korrata? "))

# Väljastab ekraanile mantrat sama arv kordi
for i in range(korduste_arv):
    print(mantra)
