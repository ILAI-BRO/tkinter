from tkinter import *

#============================================================================
def change():
    metka['text'] = "Отлично ты ее нажал!"
    metka['bg'] = 'yellow'



window = Tk()
window.geometry("300x300")
window.configure(bg="black")

metka = Label(window, text="Всем привет", bg="black", fg="white", width=30, height=2)
metka.pack()
knopka = Button(window, text="Нажми меня", bg="red", fg="white", width=30, height=2)
knopka.config(command=change)
knopka.pack()

window.mainloop()