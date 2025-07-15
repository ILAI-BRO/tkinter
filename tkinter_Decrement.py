from tkinter import *

a = 100

def change():
    global a
    a -= 1
    metka['text'] = a

window = Tk()
window.geometry("300x300")
window.configure(bg="#000000")
metka = Label(text='100', width=30, height=3)
metka.pack()
window.wm_iconbitmap('logo_2.ico')
window.wm_title('Моя первая программа на Python')
knopka = Button(text='Декремент', command=change, width=30, height=3)
knopka.pack()
window.mainloop()



