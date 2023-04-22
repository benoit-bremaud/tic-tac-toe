# coding:utf-8

# import tkinter
from tkinter import *
from tkinter.messagebox import *
import random



"""
nouvelle déclaration du tableau des cases
on commence par définir chaque case indépendemment
"""
case_1 = {
    "valeur" : "",
    "x_case" : 111*0.5,
    "y_case" : 111*0.5,
}
case_2 = {
    "valeur" : "",
    "x_case" : 111*1.5,
    "y_case" : 111*0.5
}
case_3 = {
    "valeur" : "",
    "x_case" : 111*2.5,
    "y_case" : 111*0.5
}
case_4 = {
    "valeur" : "",
    "x_case" : 111*0.5,
    "y_case" : 111*1.5
}
case_5 = {
    "valeur" : "",
    "x_case" : 111*1.5,
    "y_case" : 111*1.5
}
case_6 = {
    "valeur" : "",
    "x_case" : 111*2.5,
    "y_case" : 111*1.5
}
case_7 = {
    "valeur" : "",
    "x_case" : 111*0.5,
    "y_case" : 111*2.5
}
case_8 = {
    "valeur" : "",
    "x_case" : 111*1.5,
    "y_case" : 111*2.5
}
case_9 = {
    "valeur" : "",
    "x_case" : 111*2.5,
    "y_case" : 111*2.5
}

tableau_des_cases = {
    "case1" : case_1,
    "case2" : case_2,
    "case3" : case_3,
    "case4" : case_4,
    "case5" : case_5,
    "case6" : case_6,
    "case7" : case_7,
    "case8" : case_8,
    "case9" : case_9
}

# Définition des variables globales
signe = ["X", "O"]
l_canvas = 333
h_canvas = 333

l_window = l_canvas + 7
h_window = h_canvas + 50

ia_participe = True

def ia_joue():
    ia_niveau_difficulte()

def ia_niveau_difficulte():
    n = 1
    cases_vides(n)

def cases_vides(x):
    match x:
        case 1:
            ia_choix_case_difficulte_1()
        case 2:
            ia_choix_case_difficulte_2()
        case 3:
            ia_choix_case_difficulte_3()

def ia_choix_case_difficulte_1():
    n = ""
    for i in range(len(tableau_des_cases)):
        if tableau_des_cases["case" + str(i+1)]["valeur"] == "":
            n += str(i+1)
    ai_case_choisie(n)

def ia_choix_case_difficulte_2():
    n = ""
    ai_case_choisie(n)
    pass

def ia_choix_case_difficulte_3():
    ai_case_choisie(n)
    pass

def ai_case_choisie(X):
    case_choisie_par_ia = "case"
    case_choisie_par_ia += str(random.choice(str(X))) # Choisi une case au hazard parmis les cases libres restantes
    cocher_la_case(case_choisie_par_ia)

def quelle_case(event):
    x = event.x
    y = event.y
    n_case = ""
    if x in range(0, 111):
        if y in range(0, 111):
            n_case = "case1"
        elif y in range(111, 222):
            n_case = "case4"
        elif y in range(222, 333):
            n_case = "case7"
    if x in range(111, 222):
        if y in range(0, 111):
            n_case = "case2"
        elif y in range(111, 222):
            n_case = "case5"
        elif y in range(222, 333):
            n_case = "case8"
    if x in range(222, 333):
        if y in range(0, 111):
            n_case = "case3"
        elif y in range(111, 222):
            n_case = "case6"
        elif y in range(222, 333):
            n_case = "case9"
    cocher_la_case(n_case)

def cocher_la_case(n_case):
    if tableau_des_cases[n_case]["valeur"] == signe[0] or tableau_des_cases[n_case]["valeur"] == signe[1]:
        showerror("Tic Tac Toe Game", "Choix impossible\nChoisissez une case vide !!")
    else:
        canvas.create_text(tableau_des_cases[n_case]["x_case"], tableau_des_cases[n_case]["y_case"], text=str(signe[0]), font="Arial 22 bold", fill="red", tags="signe")
        tableau_des_cases[n_case]["valeur"] = signe[0]
        match_nul()

def match_nul():
    if case_1["valeur"] and case_2["valeur"] and case_3["valeur"] and case_4["valeur"] and case_5["valeur"] and case_6["valeur"] and case_7["valeur"] and case_8["valeur"] and case_9["valeur"] != "":
        if askyesno("Tic Tac Toe Game", "Match nul, aucun gagant !!\nVoulez-vous rejouer ?"):
            reset_canvas()
            reset_tableau_des_cases()
        else:
            window.quit()
    else:
        check_gagnant()

def reset_canvas():
    canvas.delete("signe")

def reset_tableau_des_cases():
    for i in range(len(tableau_des_cases)):
        tableau_des_cases["case" + str(i+1)]["valeur"] = ""

def check_gagnant():
    if tableau_des_cases["case1"]["valeur"] == tableau_des_cases["case2"]["valeur"] == tableau_des_cases["case3"]["valeur"] == signe[0]:
        no = 1
    elif tableau_des_cases["case4"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case6"]["valeur"] == signe[0]:
        no = 2
    elif tableau_des_cases["case7"]["valeur"] == tableau_des_cases["case8"]["valeur"] == tableau_des_cases["case9"]["valeur"] == signe[0]:
        no = 3
    elif tableau_des_cases["case1"]["valeur"] == tableau_des_cases["case4"]["valeur"] == tableau_des_cases["case7"]["valeur"] == signe[0]:
        no = 4
    elif tableau_des_cases["case2"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case8"]["valeur"] == signe[0]:
        no = 5
    elif tableau_des_cases["case3"]["valeur"] == tableau_des_cases["case6"]["valeur"] == tableau_des_cases["case9"]["valeur"] == signe[0]:
        no = 6
    elif tableau_des_cases["case1"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case9"]["valeur"] == signe[0]:
        no = 7
    elif tableau_des_cases["case3"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case7"]["valeur"] == signe[0]:
        no = 8
    else:
        no = 0
    encadre_cases_gagnantes(canvas, no)

def encadre_cases_gagnantes(canvas, cas_no):
    n = False
    match cas_no:
        case 0:
            pass
        case 1:
            canvas.create_rectangle(0 + 5, 111 - 4, 333 - 2, 0 + 5, outline="yellow", width=5, tags="signe")
            n = True
        case 2:
            canvas.create_rectangle(0 + 5, 222 - 4, 333 - 2, 111 + 5, outline="yellow", width=5, tags="signe")
            n = True
        case 3:
            canvas.create_rectangle(0 + 5, 333 - 4, 333 - 2, 222 + 5, outline="yellow", width=5, tags="signe")
            n = True
        case 4:
            canvas.create_rectangle(0 + 5, 0 + 5, 111 - 4, 333 - 2, outline="yellow", width=5, tags="signe")
            n = True
        case 5:
            canvas.create_rectangle(111 + 3, 0 + 5, 222 - 4, 333 - 2, outline="yellow", width=5, tags="signe")
            n = True
        case 6:
            canvas.create_rectangle(222 + 4, 0 + 5, 333 - 2, 333 - 2, outline="yellow", width=5, tags="signe")
            n = True
        case 7:
            canvas.create_rectangle(0 + 5, 0 + 5, 111 - 4, 111 - 4, outline="yellow", width=5, tags="signe")
            canvas.create_rectangle(111 + 4, 111 + 4, 222 - 4, 222 - 4, outline="yellow", width=5, tags="signe")
            canvas.create_rectangle(222 + 4, 222 + 4, 333 - 4, 333 - 4, outline="yellow", width=5, tags="signe")
            n = True
        case 8:
            canvas.create_rectangle(222 + 4, 0 + 4, 333 - 4, 111 - 4, outline="yellow", width=5, tags="signe")
            canvas.create_rectangle(111 + 4, 111 + 4, 222 - 4, 222 - 4, outline="yellow", width=5, tags="signe")
            canvas.create_rectangle(0 + 4, 222 + 4, 111 + 4, 333 - 4, outline="yellow", width=5, tags="signe")
            n = True
    if n:
        le_gagnant_est()
    else:
        changer_joueur()
        if ia_participe and signe[0] == "O": # Et maintenant faire jouer l'IA
            ia_joue()
        else:
            pass


def le_gagnant_est():
    if askyesno("Tic Tac Toe Game", "Le joueur {} à gagné cette partie\nVoulez vous rejouer ?!".format(signe[0])):
        reset_canvas()
        reset_tableau_des_cases()
    else:
        window.quit()

def changer_joueur():
    signe.reverse()

taille_window = str(l_window) + "x" + str(h_window)

window = Tk()

window.geometry(str(taille_window))

label = Label(window, text="Tic Tac Toe GAME !!", font="Arial 20 bold")
label.pack()

case_select = window.bind('<Button-1>', quelle_case)

# Canevas
canvas = Canvas(window, width=l_canvas, height=h_canvas, background="black")
canvas.create_line(0, h_canvas/3, l_canvas, h_canvas/3, fill="white")
canvas.create_line(0, 2*(h_canvas/3), l_canvas, 2*(h_canvas/3), fill="white")
canvas.create_line(l_canvas/3, 0, l_canvas/3, h_canvas, fill="white")
canvas.create_line(2*(l_canvas/3), 0, 2*(l_canvas/3), h_canvas, fill="white")
print(l_canvas, h_canvas)
canvas.pack()


window.mainloop()




