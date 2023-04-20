# coding:utf-8

# import tkinter
from tkinter import *
from tkinter.messagebox import *

# Variables globales


"""
nouvelle déclaration du tableau des cases
on commence par définir chaque case indépendemment
"""
case_1 = {
    "valeur" : "",
    "x_case" : 111*0.5,
    "y_case" : 111*0.5
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
signe = ["X", "O"]
a = True
window = Tk()
window.geometry("350x390")


label = Label(window, text="Tic Tac Toe GAME !!", font="Arial 20 bold")
label.pack()

# Canevas
canvas = Canvas(window, width=333, height=333, background="black")
canvas.create_line(0, 111, 333, 111, fill="white")
canvas.create_line(0, 222, 333, 222, fill="white")
canvas.create_line(111, 0, 111, 333, fill="white")
canvas.create_line(222, 0, 222, 333, fill="white")
canvas.pack()

def reset_canvas():
    canvas.delete("signe")
    case_1["valeur"] = case_2["valeur"] = case_3["valeur"] = case_4["valeur"] = case_5["valeur"] = case_6["valeur"] = \
    case_7["valeur"] = case_8["valeur"] = case_9["valeur"] = ""


def quelle_case(event):
    global n_case
    n_case = 0
    x = event.x
    y = event.y
    if x in range(0, 111):
        if y in range(0, 111):
            print("Case 1")
            n_case = "case1"
        elif y in range(111, 222):
            print("Case 4")
            n_case = "case4"
        elif y in range(222, 333):
            print("Case 7")
            n_case = "case7"
    elif x in range(111, 222):
        if y in range(0, 111):
            print("Case 2")
            n_case = "case2"
        elif y in range(111, 222):
            print("Case 5")
            n_case = "case5"
        elif y in range(222, 333):
            print("Case 8")
            n_case = "case8"
    elif x in range(222, 333):
        if y in range(0, 111):
            print("Case 3")
            n_case = "case3"
        elif y in range(111, 222):
            print("Case 6")
            n_case = "case6"
        elif y in range(222, 333):
            print("Case 9")
            n_case = "case9"


    if tableau_des_cases[n_case]["valeur"] == signe[0] or tableau_des_cases[n_case]["valeur"] == signe[1]:
        showerror("Tic Tac Toe", "Selection impossible, choisissez une case vide !")


    else:
        canvas.create_text(tableau_des_cases[n_case]["x_case"], tableau_des_cases[n_case]["y_case"], text=str(signe[0]), font="Arial 22 bold", fill="red", tags="signe")
        tableau_des_cases[n_case]["valeur"] = signe[0]

        a = False
        if tableau_des_cases["case1"]["valeur"] == tableau_des_cases["case2"]["valeur"] == tableau_des_cases["case3"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(0+5, 111-4, 333-2, 0+5, outline="yellow", width=5, tags="signe")
            a = True
        if tableau_des_cases["case4"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case6"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(0+5, 222-4, 333-2, 111+5, outline="yellow", width=5, tags="signe")
            a = True
        if tableau_des_cases["case7"]["valeur"] == tableau_des_cases["case8"]["valeur"] == tableau_des_cases["case9"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(0+5, 333-4, 333-2, 222+5, outline="yellow", width=5, tags="signe")
            a = True
        if tableau_des_cases["case1"]["valeur"] == tableau_des_cases["case4"]["valeur"] == tableau_des_cases["case7"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(0+5, 0+5, 111-4, 333-2, outline="yellow", width=5, tags="signe")
            a = True
        if tableau_des_cases["case2"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case8"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(111+3, 0+5, 222-4, 333-2, outline="yellow", width=5, tags="signe")
            a = True
        if tableau_des_cases["case3"]["valeur"] == tableau_des_cases["case6"]["valeur"] == tableau_des_cases["case9"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(222+4, 0+5, 333-2, 333-2, outline="yellow", width=5, tags="signe")
            a = True
        if tableau_des_cases["case1"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case9"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(0, 0+5, 333-2, 333-2, outline="yellow", width=5, tags="signe")
            a = True
        if tableau_des_cases["case3"]["valeur"] == tableau_des_cases["case5"]["valeur"] == tableau_des_cases["case7"]["valeur"] == str(signe[0]):
            canvas.create_rectangle(0, 0+5, 333-2, 333-2, outline="yellow", width=5, tags="signe")
            a = True
        if a == True:
            if askyesno("Tic Tac Toe Game", "Le joueur {} à gagné cette partie\nVoulez vous rejouer ?!".format(signe[0])):
                reset_canvas()
                #canvas.delete("signe")
                #case_1["valeur"] = case_2["valeur"] = case_3["valeur"] = case_4["valeur"] = case_5["valeur"] = case_6["valeur"] = case_7["valeur"] = case_8["valeur"] = case_9["valeur"] = ""

            else:
                window.quit()

        if case_1["valeur"] and case_2["valeur"] and case_3["valeur"] and case_4["valeur"] and case_5["valeur"] and case_6["valeur"] and case_7["valeur"] and case_8["valeur"] and case_9["valeur"] != "" :
            if askyesno("Tic Tac Toe Game", "Match nul, aucun gagant !!\nVoulez-vous rejouer ?"):
                reset_canvas()
                #canvas.delete("signe")
                #case_1["valeur"] = case_2["valeur"] = case_3["valeur"] = case_4["valeur"] = case_5["valeur"] = case_6["valeur"] = case_7["valeur"] = case_8["valeur"] = case_9["valeur"] = ""

            else:
                window.quit()

        signe.reverse()


window.bind('<Button-1>', quelle_case)


window.mainloop()