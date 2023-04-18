# coding: utf-8

from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre1 = Tk()

fenetre["bg"]="white"

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

Button(text='Action', command=callback).pack()

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=10, pady=20)

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")
        showwarning("title 5", "On s'amuse, hein ?!")

Button(text='Action', command=callback).pack()

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=10, pady=10)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=100)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=100)

l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
l.pack(fill="both", expand="no")

Label(l, text="A l'intérieure de la frame").pack()

def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

Button(text='Action', command=callback).pack()

def alert():
    showinfo("alerte", "Bravo!")
def info():
    showinfo("info", "Vas te faire mettre !!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=info)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_separator()
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=10, pady=10)
Button(fenetre, text ='Bonjour', command=alert).pack(side=LEFT, padx=5, pady=5)
Button(fenetre, text ='Au revoir').pack(side=RIGHT, padx=5, pady=5)

for ligne in range(3):
    for colonne in range(3):
        Button(fenetre1, text='L%s-C%s' % (ligne, colonne), borderwidth=3).grid(row=ligne, column=colonne)

# Button(text='Action', command=callback).pack(

# fenetre.mainloop()
fenetre1.mainloop()

