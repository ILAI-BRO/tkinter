from tkinter import *

a = 128512

def change():
    global a
    a += 1
    metka['text'] = chr(a)
    text['text'] = f"&#{a}"


window = Tk()
window.geometry("350x350")
window.configure(bg="red")
metka = Label(text=chr(a), width=30, height=3, font=("Arial", 54))
text = Label(text=f"&#{a}", bg="red", font=("Arial", 24))
text.pack()
metka.pack()
window.wm_iconbitmap('logo_2.ico')
window.wm_title('Генератор смайликов')

knopka = Button(text='Следующий смайлик', command=change, width=30, height=3)
knopka.pack()
window.mainloop()
