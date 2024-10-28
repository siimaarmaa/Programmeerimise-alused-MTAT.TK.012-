name = input("Sisesta oma nimi: ")
lubatud_kiirus = int(input("Sisesta lubatud kiirus (täisarv): "))
tegelik_kiirus = int(input("Sisesta tegelik kiirus (täisarv): "))
kiiruse_uletamine = tegelik_kiirus - lubatud_kiirus

if kiiruse_uletamine > 0:
    esialgne_trahv = kiiruse_uletamine * 5
    trahv = min(300, esialgne_trahv)
    print(f"{name}, kiiruse ületamise eest on teie trahv {trahv} eurot.")
else:
    print(f"{name}, te ei ületanud kiirust, trahvi ei määrata.")
