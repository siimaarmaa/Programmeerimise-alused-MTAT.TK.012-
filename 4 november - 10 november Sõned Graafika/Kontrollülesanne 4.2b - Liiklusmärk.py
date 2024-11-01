import tkinter as tk

# Funktsioon, mis joonistab "Anna teed" liiklusmärgi
def joonista_anna_teed_mark(canvas):
    laius = 300
    korgus = 300
    
    # Joonistame kolmnurga
    kolmnurga_korgus = 200
    kolmnurga_laius = 250
    x0 = (laius - kolmnurga_laius) / 2
    y0 = (korgus - kolmnurga_korgus) / 2
    x1 = x0 + kolmnurga_laius
    y1 = y0
    x2 = laius / 2
    y2 = y0 + kolmnurga_korgus
    
    # Kolmnurk punane täis
    canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill='red', outline='black')
    
    # Sisemine valge kolmnurk
    valge_marginaal = 20
    x0 += valge_marginaal
    y0 += valge_marginaal
    x1 -= valge_marginaal
    y1 += valge_marginaal
    y2 -= valge_marginaal
    
    canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill='white', outline='black')

# Loo tkinter aken
aken = tk.Tk()
aken.title("Liiklusmärk")

# Loo lõuend ja määra taustavalgeks
canvas = tk.Canvas(aken, width=300, height=300, bg='white')
canvas.pack()

# Joonista liiklusmärk
joonista_anna_teed_mark(canvas)

# Käivita tkinter peamine tsükkel
aken.mainloop()
