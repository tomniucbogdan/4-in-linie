from tkinter import *
from PIL import ImageTk
from joc_prorpiuzis import run


def ajutor():
    top = Toplevel()
    top.title("Instructiuni joc")
    top.configure(bg="#020C53")
    my_label = Label(top, text='''"4 in linie" este un joc in care jucatorii aleg una din cele 2 culori:
        Jucator 1: rosu
        Jucator 2: galben
                            
        Dupa ce fiecare jucator si-a ales culoarea, 
        piesele corespunzatoare culorii alese sunt puse intr-o tabla de joc, formata din 7 coloane si 6 randuri.
        
        Piesele cad drept in jos, ocupand un spatiu de pe tabla.
        
        Obiectivul jocului este de a fi primul care formeaza o linie orizontala, 
        verticala sau pe digonala secundara(din stanga jos spre dreapta sus) cu 4 dintre prorpiile piese.''',
                     font=("TimesNewRoman", 20), fg='white')
    my_label.configure(bg="#020C53")
    my_label.pack(anchor=CENTER)
    buton_iesire = Button(top, text="Inchide", command=top.destroy)
    buton_iesire.pack()
    top.state('zoomed')


window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width}x{height}')
window.title("4 in linie")
window.configure(bg="#020C53")
logo = ImageTk.PhotoImage(file="E:\\Programare_Python\\Proiect\\logo.png")
lg = Label(window, image=logo, bd=0)
lg.pack()
frame = LabelFrame(window, padx=5, pady=5, bd=0)
frame.configure(bg="#020C53")
frame.pack(pady=20)

# Butoane principale
buton_start = Button(frame, text="Start joc", bd="10", padx=139, pady=10, font=("TimesNewRoman", 20), bg="#FFCA3D",
                     command=lambda: [window.destroy(), run()])
buton_start.pack(pady=20)
buton_ajutor = Button(frame, text="Descriere joc", bd="10", padx=110, pady=10, font=("TimesNewRoman", 20), bg="#FFCA3D",
                      command=ajutor)
buton_ajutor.pack(pady=20)
buton_exit = Button(frame, text="Inchide jocul", bd="10", padx=115, pady=10, font=("TimesNewRoman", 20), bg="#FFCA3D",
                    command=window.destroy)
buton_exit.pack(pady=20)

window.state('zoomed')

window.mainloop()
