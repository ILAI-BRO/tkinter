from tkinter import *


lst_name = []
lst_surname = []
lst_lastname = []

def get_name():
    global name
    name = inp_name.get()
    lst_name.append(name)
    inp_name.delete(0, END)
    print(lst_name)



def get_surname():
    global surname
    surname = inp_surname.get()
    lst_surname.append(surname)
    inp_surname.delete(0, END)
    print(lst_surname)

def get_lastname():
    global lastname
    lastname = inp_lastname.get()
    lst_lastname.append(lastname)
    inp_lastname.delete(0, END)
    print(lst_lastname)

window = Tk()

window.title("Фреймы!")

fr_name = Frame()
fr_surname = Frame()
fr_lastname = Frame()

fr_name.pack()
fr_surname.pack()
fr_lastname.pack()

metka_name = Label(fr_name, text="    Введите имя:", fg="black", bg="white", font=("Courier", 15))
metka_name.pack(side=LEFT)
inp_name = Entry(fr_name, width=50, fg="black", bg="white", font=("Courier", 15))
inp_name.pack(side=LEFT)
b_name = Button(fr_name, text="Отправить", command=get_name, fg="black", bg="white",
                                                        font=("Courier",
                                                                                       15))
b_name.pack(side=LEFT)

metka_surname = Label(fr_surname, text="Введите фамилию:", fg="black", bg="white", font=("Courier",
                                                                                      15))
metka_surname.pack(side=LEFT)
inp_surname = Entry(fr_surname, width=50, fg="black", bg="white", font=("Courier", 15))
inp_surname.pack(side=LEFT)
b_surname = Button(fr_surname, text="Отправить", command=get_surname, fg="black", bg="white",
                                                        font=("Courier",
                                                                                       15))
b_surname.pack(side=LEFT)

metka_lastname = Label(fr_lastname, text="Введите отчество:", fg="black", bg="white",
                       font=("Courier",
                                                                                      15))
metka_lastname.pack(side=LEFT)
inp_lastname = Entry(fr_lastname, width=50, fg="black", bg="white", font=("Courier", 15))
inp_lastname.pack(side=LEFT)
b_lastname = Button(fr_lastname, text="Отправить", command=get_lastname, fg="black", bg="white",
                                                        font=("Courier",
                                                                                       15))
b_lastname.pack(side=LEFT)

window.mainloop()