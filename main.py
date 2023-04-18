# coding:utf-8

from tkinter import *

fenetre = Tk()

bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
# label
label = Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()

# bouton1.pack()

label.pack()

fenetre.mainloop()

# bouton de sortie

# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()

