from tkinter import *

def read():
    t = text.get(1.0, END)
    print(t)
    text.delete(1.0, END)

def read2():
    pushkin = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    "Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie c"
    info = text.insert(1.0, pushkin)


window = Tk()

window.title("Стихотворение")

text = Text(width=30, height=20, bg="black", fg="white", font=("Courier", 20))
text.pack(side=LEFT)

scrollbar = Scrollbar(command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text.configure(yscrollcommand=scrollbar.set)

b = Button(text="Ввод", command=read)
b.pack(side=LEFT)
b2 = Button(text="Вставка", command=read2)
b2.pack(side=LEFT)

window.mainloop()