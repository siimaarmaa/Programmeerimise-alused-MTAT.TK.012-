# Küsi kasutajalt aastatulu (mittenegatiivne ujukomaarv)
aastatulu = float(input("Sisesta oma aastatulu (mittenegatiivne ujukomaarv): "))

# Arvuta maksuvaba tulu vastavalt tingimustele
if aastatulu <= 6000:
    maksuvaba_tulu = aastatulu
elif aastatulu <= 14400:
    maksuvaba_tulu = 6000
elif aastatulu <= 25200:
    maksuvaba_tulu = 6000 - (6000 / 10800) * (aastatulu - 14400)
else:
    maksuvaba_tulu = 0

# Ümarda maksuvaba tulu kahe komakohani ja väljasta tulemus
maksuvaba_tulu = round(maksuvaba_tulu, 2)
print(f"Maksuvaba tulu on: {maksuvaba_tulu} eurot.")
