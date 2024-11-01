# Programm: Vikerkaare värvi generaator
# See programm genereerib juhuslikult vikerkaare värvi ja näitab kasutajale selle nime.
# Kirjutasin selle programmi, sest mind on alati huvitanud värvid ja tahtsin midagi lihtsat ning lõbusat teha.

import random
import tkinter as tk

# Funktsioon juhusliku vikerkaare värvi valimiseks
def juhuslik_varv():
    varvid = ["Punane", "Oranž", "Kollane", "Roheline", "Sinine", "Indigosinine", "Violetne"]
    return random.choice(varvid)

# Funktsioon, mis kuvab akna juhusliku värviga
def kuva_varv():
    valitud_varv = juhuslik_varv()
    tulemus_label.config(text=f"Vikerkaare värv: {valitud_varv}")

# Graafilise liidese loomine Tkinteri abil
aken = tk.Tk()
aken.title("Vikerkaare Värvi Generaator")
aken.geometry("300x200")

# Nupp värvi genereerimiseks ja tulemus kuvamiseks
genereeri_nupp = tk.Button(aken, text="Genereeri vikerkaare värv", command=kuva_varv)
genereeri_nupp.pack(pady=20)

# Silt tulemuse kuvamiseks
tulemus_label = tk.Label(aken, text="")
tulemus_label.pack()

# Käivita liides
aken.mainloop()
