import tkinter as tk

# Funktsioon, mis joonistab Tartu linna lipu
def joonista_tartu_lipp(canvas):
    laius = 300
    korgus = 200
    triibu_korgus = korgus // 3

    # Ülemine punane triip
    canvas.create_rectangle(0, 0, laius, triibu_korgus, fill='red', outline='')

    # Keskmine valge triip
    canvas.create_rectangle(0, triibu_korgus, laius, 2 * triibu_korgus, fill='white', outline='')

    # Alumine punane triip
    canvas.create_rectangle(0, 2 * triibu_korgus, laius, korgus, fill='red', outline='')

# Loo tkinter aken
aken = tk.Tk()
aken.title("Lipp")

# Loo lõuend ja määra taustavalgeks
canvas = tk.Canvas(aken, width=300, height=200, bg='white')
canvas.pack()

# Joonista lipp
joonista_tartu_lipp(canvas)

# Käivita tkinter peamine tsükkel
aken.mainloop()
