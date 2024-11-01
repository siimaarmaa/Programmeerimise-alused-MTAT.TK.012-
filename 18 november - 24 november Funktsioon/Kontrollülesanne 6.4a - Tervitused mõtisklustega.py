# Funktsioon tervitus, mis kuvab tervituse koos järjekorranumbriga
def tervitus(n):
    print('Võõrustaja: "Tere!"')
    print(f'Täna {n}. kord tervitada, mõtiskleb võõrustaja.')
    print('Külaline: "Tere, suur tänu kutse eest!"')

# Peaprogramm
# Küsime kasutajalt külaliste arvu
kylaliste_arv = int(input("Sisesta külaliste arv: "))

# Tsükkel, mis kutsub funktsiooni tervitus vastava järjekorranumbriga
for i in range(1, kylaliste_arv + 1):
    tervitus(i)
