import tkinter as tk
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def calculer():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        
        pgcd_val = gcd(a, b)
        ppcm_val = lcm(a, b)
        
        pair_a = "pair" if a % 2 == 0 else "impair"
        pair_b = "pair" if b % 2 == 0 else "impair"
        somme = a + b
        liste_nombres = list(range(1, somme + 1))
        
        label_resultat.config(text=f"PGCD: {pgcd_val}\nPPCM: {ppcm_val}\n"
                                  f"{a} est {pair_a}\n{b} est {pair_b}\n"
                                  f"Entiers entre 1 et {somme}: {liste_nombres}")
    except ValueError:
        label_resultat.config(text="Veuillez entrer des entiers valides.")
        
fenetre = tk.Tk()
fenetre.title("Calcul PGCD, PPCM et vérification des entiers")

label_a = tk.Label(fenetre, text="Entier A:")
label_a.pack()

entry_a = tk.Entry(fenetre)
entry_a.pack()

label_b = tk.Label(fenetre, text="Entier B:")
label_b.pack()

entry_b = tk.Entry(fenetre)
entry_b.pack()

btn_calculer = tk.Button(fenetre, text="Calculer", command=calculer)
btn_calculer.pack()

label_resultat = tk.Label(fenetre, text="", justify="left")
label_resultat.pack()

fenetre.mainloop()
