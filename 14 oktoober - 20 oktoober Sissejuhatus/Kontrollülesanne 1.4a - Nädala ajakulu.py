ainepunktid = int(input("Sisesta ainepunktide arv (täisarv): "))
nadalate_arv = int(input("Sisesta nädalate arv (täisarv): "))
ajakulu_kokku = ainepunktid * 26
nadalane_ajakulu = ajakulu_kokku / nadalate_arv
nadalane_ajakulu_umberdatud = round(nadalane_ajakulu)

print("Ühe nädala eeldatav ajakulu on:", nadalane_ajakulu_umberdatud, "tundi")