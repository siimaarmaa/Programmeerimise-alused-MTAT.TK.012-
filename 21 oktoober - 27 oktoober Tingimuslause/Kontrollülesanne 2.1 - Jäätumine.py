# Küsi kasutajalt õhutemperatuuri
temperatuur = float(input("Sisesta õhutemperatuur: "))

# Kontrolli temperatuuri ja anna sobiv teade
if temperatuur <= 4.0:
    print("On jäätumise oht.")
else:
    print("Ei ole jäätumise ohtu.")
