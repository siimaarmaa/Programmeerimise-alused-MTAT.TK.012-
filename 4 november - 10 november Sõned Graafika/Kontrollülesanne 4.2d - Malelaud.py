import tkinter as tk

# Funktsioon, mis joonistab malelaua
def joonista_malelaud(canvas, ruudu_suurus=50):
    for rida in range(8):
        for veerg in range(8):
            x1 = veerg * ruudu_suurus
            y1 = rida * ruudu_suurus
            x2 = x1 + ruudu_suurus
            y2 = y1 + ruudu_suurus
            värv = 'white' if (rida + veerg) % 2 == 0 else 'black'
            canvas.create_rectangle(x1, y1, x2, y2, fill=värv, outline='black')
    
    # Joonistame ratsu valgele ruudule (e4)
    ratsu_keskpunkt_x = 4 * ruudu_suurus + ruudu_suurus / 2
    ratsu_keskpunkt_y = 3 * ruudu_suurus + ruudu_suurus / 2
    canvas.create_text(ratsu_keskpunkt_x, ratsu_keskpunkt_y, text="♞", font=("Arial", 32), fill="black")

# Loo tkinter aken
aken = tk.Tk()
aken.title("Malelaud")

# Loo lõuend ja määra taustavalgeks
canvas = tk.Canvas(aken, width=400, height=400, bg='white')
canvas.pack()

# Joonista malelaud
joonista_malelaud(canvas)

# Käivita tkinter peamine tsükkel
aken.mainloop()
