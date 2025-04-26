import tkinter as tk
import random

# Funktion zum Würfeln
def wuerfeln():
    zahl = random.randint(1, 6)
    punkte_label.config(text=str(zahl))
    if zahl == 1:
        nachricht_label.config(text="Miau")
    elif zahl == 2:
        nachricht_label.config(text="Hello")
    elif zahl == 3:
        nachricht_label.config(text="Okay")
    elif zahl == 4:
        nachricht_label.config(text="Gut")
    elif zahl == 5:
        nachricht_label.config(text="fast")
    elif zahl == 6:
        nachricht_label.config(text="Gewonnen")

# GUI einrichten
fenster = tk.Tk()
fenster.title("Würfel Spiel")

# Knopf zum Würfeln
wuerfeln_knopf = tk.Button(fenster, text="Würfel", command=wuerfeln)
wuerfeln_knopf.pack()

# Label für die Punkte
punkte_label = tk.Label(fenster, text="", font=("Helvetica", 48))
punkte_label.pack()

# Label für die Nachricht
nachricht_label = tk.Label(fenster, text="", font=("Helvetica", 24))
nachricht_label.pack()

# Hauptschleife der GUI
fenster.mainloop()

