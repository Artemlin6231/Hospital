import tkinter as tk
import re
import numpy as np
from tkinter import scrolledtext
from tkinter import *
from tkinter import ttk
import interview
import survave
import maze

def main_interview():

    class Patient:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def quiz(self):
            Text_q, Text_dict = interview.convert_question()
            diagnoz = interview.open_window(Text_q, Text_dict, self.name)
            return diagnoz
    class Patient_by_hospital(Patient):
        def game(self):
            survave.run()
            return
    class Patient_by_polyclinic(Patient):
        def game(self):
            maze.founding()
            return

    name = 'LEXA'
    age = 18
    lexa = Patient(name,age)

    mainwindow = tk.Tk()
    mainwindow.title('Вы')
    mainwindow.resizable(width=False, height=False)
    mainwindow.geometry('720x480+400+100')
    photo = tk.PhotoImage(file = 'hospital.png')
    mainwindow.iconphoto(False, photo)
    mainwindow.config(bg = '#DEFDFF')
    label = tk.Label(mainwindow,text = "Ваше имя:",
                     bg = '#DEFDFF',
                     fg = '#99004C',
                     font = ('Arial', 18, 'bold'),
                     pady = 20
                     )
    label .pack()
    entry = tk.Entry(mainwindow)
    entry.pack()
    label1 = tk.Label(mainwindow,text = "Ваш возраст:",
                      bg = '#DEFDFF',
                      fg = '#99004C',
                      font = ('Arial', 18, 'bold'),
                      pady = 20
                      )
    label1.pack()
    entry1 = tk.Entry(mainwindow)
    entry1.pack()
    def out():
        global name, age
        name = entry.get()
        age = entry1.get()

        label2 = tk.Label(mainwindow, text="Закройте вкладку",
                          bg='#DEFDFF',
                          fg='#99004C',
                          font=('Arial', 18, 'bold'),
                          pady=20
                          )
        label2.pack()
        return
    button = tk.Button(mainwindow,text = "Отправить",
                       command = out,
                       bg='#DEFDFF',
                       fg='#99004C',
                       font=('Arial', 18, 'bold'),
                       activebackground='green',
                       pady=20
                       )
    button.pack()
    mainwindow.mainloop()

    lexa = Patient(name,age)
    status = lexa.quiz()
    if status<0.5:
        lexa_stay = Patient_by_hospital(name,age)
    else:
        lexa_stay = Patient_by_polyclinic(name,age)

    lexa_stay.game()


