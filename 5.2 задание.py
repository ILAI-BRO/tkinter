from tkinter import *
from tkinter import messagebox as mb




def summ():
    s1 = e_1.get()
    if not s1.lstrip("-").isdigit():
        mb.showerror("Ошибка!", "Введите целое число в первое поле!")
        return
    s2 = e_2.get()
    if not s2.lstrip("-").isdigit():
        mb.showerror("Ошибка!", "Введите целое число во второе поле!")
        return
    s3 = e_3.get()
    if not s3.lstrip("-").isdigit():
        mb.showerror("Ошибка!", "Введите целое число во второе поле!")
        return
    slag_1 = int(s1)
    slag_2 = int(s2)
    slag_3 = int(s3)


    summa = slag_1 + slag_2 + slag_3
    m_1['text'] = f"{s1} + {s2} + {s3} = {summa}"


    answer = mb.askretrycancel(title="Вопрос", message="Сложить еще 3 числа?")
    if answer:
        e_1.delete(0, END)
        e_2.delete(0, END)
        e_3.delete(0, END)
        m_1['text'] = ""
    else:
        window.destroy()

def summ_2():
    s1 = e_1.get()
    if not s1.lstrip("-").isdigit():
        mb.showerror("Ошибка!", "Введите целое число в первое поле!")
        return
    s2 = e_2.get()
    if not s2.lstrip("-").isdigit():
        mb.showerror("Ошибка!", "Введите целое число во второе поле!")
        return
    s3 = e_3.get()
    if not s3.lstrip("-").isdigit():
        mb.showerror("Ошибка!", "Введите целое число в третье поле!")
        return
    slag_1 = int(s1)
    slag_2 = int(s2)
    slag_3 = int(s3)


    summa = slag_1 * slag_2 * slag_3
    m_1['text'] = f"{s1} * {s2} * {s3} = {summa}"


    answer = mb.askretrycancel(title="Вопрос", message="Умножить еще 3 числа?")
    if answer:
        e_1.delete(0, END)
        e_2.delete(0, END)
        e_3.delete(0, END)
        m_1['text'] = ""
    else:
        window.destroy()



window = Tk()
f = Frame(height=50)
f.pack()
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = int(w / 2)
h2 = int(h / 2)
window.geometry(f'{w2}x{h2}')
window.title("Калькулятор")


#logo = PhotoImage(file="calc-logo.png")
#logo_label = Label(window, image=logo)
#logo_label.pack()


m = Label(text="Введите три целых числа и нажмите на кнопку!", height=3, font="Arial 14")
m.pack()
e_1 = Entry()
e_1.pack()
e_2 = Entry()
e_2.pack()
e_3 = Entry()
e_3.pack()
b = Button(text="Сложить три числа", command=summ)
b.pack()
b2 = Button(text="Умножить три числа", command=summ_2)
b2.pack()
m_1 = Label(height=3)
m_1.pack()

window.mainloop()