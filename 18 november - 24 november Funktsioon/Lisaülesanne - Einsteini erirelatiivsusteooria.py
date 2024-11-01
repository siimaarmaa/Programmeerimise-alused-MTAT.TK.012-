# Valguse kiirus konstantina
c = 299792.458  # km/s

# Funktsioon summa, mis arvutab kiiruste summa Einsteini erirelatiivsusteooria järgi
def summa(u, v):
    return (u + v) / (1 + (u * v) / c**2)

# Peaprogramm
# Küsime kasutajalt nelja keha kiirused
kiirus1 = float(input("Sisesta esimese keha kiirus (km/s): "))
kiirus2 = float(input("Sisesta teise keha kiirus (km/s): "))
kiirus3 = float(input("Sisesta kolmanda keha kiirus (km/s): "))
kiirus4 = float(input("Sisesta neljanda keha kiirus (km/s): "))

# Arvutame kiiruste summa, rakendades funktsiooni järjestikuliselt
summa_12 = summa(kiirus1, kiirus2)
summa_123 = summa(summa_12, kiirus3)
kogusumma = summa(summa_123, kiirus4)

# Väljastame lõpliku kiiruste summa
print("Kiiruste summa Einsteini erirelatiivsusteooria järgi on:", kogusumma, "km/s")
