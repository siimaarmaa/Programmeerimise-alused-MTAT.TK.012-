import tkinter as tk

# Funktsioon, mis joonistab maja
def joonista_maja(canvas):
    laius = 400
    korgus = 300
    
    # Maja keha
    canvas.create_rectangle(100, 150, 300, 300, fill='lightblue', outline='black')
    
    # Katus
    canvas.create_polygon(90, 150, 200, 70, 310, 150, fill='brown', outline='black')
    
    # Uks
    canvas.create_rectangle(170, 220, 230, 300, fill='saddlebrown', outline='black')
    
    # Aknad
    canvas.create_rectangle(120, 180, 160, 220, fill='white', outline='black')
    canvas.create_rectangle(240, 180, 280, 220, fill='white', outline='black')

# Loo tkinter aken
aken = tk.Tk()
aken.title("Maja")

# Loo lõuend ja määra taustavalgeks
canvas = tk.Canvas(aken, width=400, height=300, bg='white')
canvas.pack()

# Joonista maja
joonista_maja(canvas)

# Käivita tkinter peamine tsükkel
aken.mainloop()
