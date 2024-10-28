# Küsi kasutajalt inimeste arvu ja ühe bussi kohtade arvu
inimeste_arv = int(input("Sisesta inimeste arv: "))
kohti_bussis = int(input("Sisesta ühe bussi kohtade arv: "))

# Arvuta vajalike busside arv ja inimeste arv viimases bussis
vajalikud_bussid = (inimeste_arv + kohti_bussis - 1) // kohti_bussis  # Ümardamine üles
viimases_bussis = inimeste_arv % kohti_bussis if inimeste_arv % kohti_bussis != 0 else kohti_bussis

# Väljasta tulemus
print(f"Vajalik busside arv: {vajalikud_bussid}")
print(f"Inimeste arv viimases bussis: {viimases_bussis}")
