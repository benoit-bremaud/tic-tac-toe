# coding: utf-8

from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=50)
entree.pack()

label = Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()

# bouton de sortie
bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# checkbutton
bouton = Checkbutton(fenetre, text="Benoit")
bouton.pack()

# radiobutton
value = StringVar()
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

# canvas
canvas = Canvas(fenetre, width=150, height=120, background="blue")
ligne1 = canvas.create_line(75, 0, 75, 120, fill="white")
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Benoit", font="Arial 16 italic", fill="red")
canvas.pack()

value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()

value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()


fenetre.mainloop()



