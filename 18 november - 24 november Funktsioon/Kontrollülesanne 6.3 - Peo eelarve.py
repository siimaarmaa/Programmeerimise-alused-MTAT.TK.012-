# Funktsioon eelarve, mis arvutab eelarve kogusumma antud osalejate arvuga
def eelarve(osalejate_arv):
    soogi_kulu = osalejate_arv * 10  # Söök maksab 10 eurot inimese kohta
    ruumi_rent = 55  # Ruumi rent on 55 eurot
    kogusumma = soogi_kulu + ruumi_rent  # Kogusumma on söögi kulu pluss ruumi rent
    return kogusumma  # Tagastame kogusumma

# Peaprogramm
# Küsime kasutajalt kutsutud inimeste arvu
kutsutud = int(input("Sisesta kutsutud inimeste arv: "))

# Küsime kasutajalt juba tulekut kinnitanud inimeste arvu
tulevad = int(input("Sisesta inimeste arv, kes on teatanud, et nad tulevad: "))

# Arvutame ja väljastame maksimaalse eelarve (kui kõik kutsutud tulevad kohale)
max_eelarve = eelarve(kutsutud)
print("Maksimaalne eelarve on:", max_eelarve, "eurot")

# Arvutame ja väljastame minimaalse eelarve (kui tulevad ainult need, kes on teatanud)
min_eelarve = eelarve(tulevad)
print("Minimaalne eelarve on:", min_eelarve, "eurot")
