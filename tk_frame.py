from tkinter import *

def read():
    name = e.get()
    print(name)
    e.delete(0, END)

def read2():
    city = e2.get()
    print(city)
    e2.delete(0, END)

window = Tk()

f1 = Frame()
f2 = Frame()
f1.pack()
f2.pack()


m = Label(f1, text="Введите имя:", fg="red", bg="white", font=("Courier", 20))
m.pack(side=LEFT)
e = Entry(f1, width=50, justify="right",fg="red", bg="white", font=("Courier", 20))
e.pack(side=LEFT)
b = Button(f1, text="Отправить", command=read, fg="red", bg="white", font=("Courier", 20))
b.pack(side=LEFT)



m2 = Label(f2, text="Введите имя:", fg="red", bg="white", font=("Courier", 20))
m2.pack(side=LEFT)
e2 = Entry(f2, width=50, justify="right", fg="red", bg="white", font=("Courier", 20))
e2.pack(side=LEFT)
b2 = Button(f2, text="Отправить", command=read2, fg="red", bg="white", font=("Courier", 20))
b2.pack(side=LEFT)
window.mainloop()








#
# window = Tk()
# frame_top = Frame(window)
# frame_bottom = Frame(window)
# frame_left = Frame(window)
# frame_right = Frame(window)
#
# frame_left.pack(side=LEFT)
# frame_right.pack(side=RIGHT)
# frame_bottom.pack(side=BOTTOM)
# frame_top.pack(side=TOP)
#
# window.geometry("350x350")
#
# window.title("Frame")
#
# metka1 = Label(frame_left, text='Метка 1', bg='red')
# metka1.pack(side=LEFT)
# metka2= Label(frame_right, text='Метка 2', bg='yellow')
# metka2.pack(side=RIGHT)
# metka3 = Label(frame_bottom, text='Метка 3', bg='green')
# metka3.pack(side=BOTTOM)
# metka4 = Label(frame_top, text='Метка 4', bg='blue')
# metka4.pack(side=TOP)
#
#
# window.mainloop()