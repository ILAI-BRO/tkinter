from tkinter import *
import time
from tkinter import messagebox
import pygame as pg


#pip install auto-py-to-exe


pg.init()
pg.mixer.music.load('Music.mp3')

alarm_time = ''


root = Tk()


root.geometry("800x600")
root.title('Часы')
root.config(background="black")
f = Frame(root, height=200, bg="black")
f.pack()
tab = Label(root, text="00:00:00")

tab.config(bg="black", font=("Arial", 50, "bold"), fg="lime")
tab.pack(pady=10)
alarm = Entry(root, bg="black", fg="white")

alarm.config(bg="white", fg="black", font=("Arial", 20, "bold"), justify="center", width=10)
alarm.pack()
on_btn = Button(root)

on_btn.config(text="Включить будильник", font=("Arial", 10))
on_btn.pack(pady=10)
off_btn = Button(root)

off_btn.config(text="Выключить", font=("Arial", 10))
off_btn.pack(pady=10)



def tick():
    global alarm_time
    time_show = time.strftime('%X')
    if (alarm_time == time_show or alarm_time == time.strftime('%H:%M') or alarm_time ==
            time.strftime('%H')):
        alarm_time = ''
        pg.mixer.music.play()
    tab.config(text=time_show)
    tab.after(1000, tick)



def on_alarm(event):
    global alarm_time
    alarm_time = alarm.get().strip()
    messagebox.showinfo("Информация", f"Будильник установлен на {alarm_time}!")

def off_alarm(event):
    alarm_time = ''
    alarm.delete(0, END)
    pg.mixer.music.stop()
    messagebox.showinfo("Сообщение", f"Будильник выключен {alarm_time}!")


on_btn.bind("<Button-1>", on_alarm)
off_btn.bind("<Button-1>", off_alarm)
tick()
root.mainloop()