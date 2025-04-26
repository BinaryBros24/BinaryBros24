import tkinter as tk 
import random

# Funktion zum Würfeln
def wuerfeln():
    zahl = random.randint(1, 6)
    punkte_label.config(text=str(zahl))
    if zahl == 1:
        nachricht_label.config(text="Try again")
    elif zahl == 2:
        nachricht_label.config(text="You need more luck")
    elif zahl == 3:
        nachricht_label.config(text="Okay")
    elif zahl == 4:
        nachricht_label.config(text="Good")
    elif zahl == 5:
        nachricht_label.config(text="Almost done")
    elif zahl == 6:
        nachricht_label.config(text="Winner")

# GUI einrichten
fenster = tk.Tk()
fenster.title("cube (no one asked for)")

# Knopf zum Würfeln
wuerfeln_knopf = tk.Button(fenster, text="the cube is not cubing", command=wuerfeln)
wuerfeln_knopf.pack()

# Label für die Punkte
punkte_label = tk.Label(fenster, text="", font=("Helvetica", 48))
punkte_label.pack()

# Label für die Nachricht
nachricht_label = tk.Label(fenster, text="", font=("Helvetica", 24))
nachricht_label.pack()

# Hauptschleife der GUI
fenster.mainloop()


