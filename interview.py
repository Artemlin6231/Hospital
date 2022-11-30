import tkinter as tk
import re
import numpy as np
from tkinter import scrolledtext
from tkinter import *
from tkinter import ttk

def convert_question():
    file = open("опрос.txt", "r", encoding="utf8")
    Text = file.read()
    Text = Text.split(sep='\n')

    # отделяем вопросы
    pattern = r'^\d{1,3}\.' # строка начинается с 1 или 3 цифр, а затем идёт точка (ограничение на 999 вопросов!!!)
    Text_q = [i for i in Text if len(re.findall(pattern, i)) != 0]
    print('Всего вопросов:', len(Text_q))

    # отделяем ответы
    pattern = r'^.\)' # строка начинается с одного любого символа, а затем идёт скобка
    Text_a = [i for i in Text if len(re.findall(pattern, i)) != 0]
    print('Всего ответов:', len(Text_a))

    Text_dict = {}
    for i,q in enumerate(Text_q):
        Text_dict[q] = []
        for j in range(4*i,4*i+4):
            Text_dict[q].append(Text_a[j])
    return Text_q,Text_dict
def open_window(Text_q,Text_dict,name):
    global qc, probability,c
    window = tk.Tk()
    window.title('Опросник пациента '+name)
    window.resizable(width=False, height=False)
    window.geometry('720x480+400+100')
    window.config(bg = '#DEFDFF')
    qc = 0
    probability = 0
    quest = scrolledtext.ScrolledText(window, width=75, height=5)
    quest.insert(tk.INSERT, Text_q[qc] + ',' + name+'?')
    quest.pack()
    mark = tk.Label(window, text='Выберите ответы: ', font=('Arial Bold', 18), fg = '#99004C', bg='#DEFDFF')
    mark.pack()
    entry = tk.Entry(window)
    entry.pack()
    variants = scrolledtext.ScrolledText(window, width=75, height=5)
    variants.insert(tk.INSERT, Text_dict[Text_q[qc]][0]+'\n')
    variants.insert(tk.INSERT,  Text_dict[Text_q[qc]][1]+'\n')
    variants.insert(tk.INSERT,  Text_dict[Text_q[qc]][2]+'\n')
    variants.insert(tk.INSERT, Text_dict[Text_q[qc]][3]+'\n')
    variants.pack()


    #a = max([CheckVar1.get(), CheckVar2.get(), CheckVar3.get(), CheckVar4.get()]) / 4
    #probability += a
    qc += 1
    def question():
        global qc, probability,c
        if qc >= len(Text_dict):
            c = probability/20
            if c<0.5 and c>0:
                root = tk.Tk()
                root.geometry('720x480+400+100')
                root.config(bg='#DEFDFF')
                name = tk.Label(root, text="Вам в стационар",
                                bg='#DEFDFF',
                                fg='#99004C',
                                font=('Arial', 28, 'bold'),
                                pady = 200
                                )
                name.pack()
            elif c>0.5:
                root = tk.Tk()
                root.geometry('720x480+400+100')
                root.config(bg='#DEFDFF')
                name = tk.Label(root, text="Вам в поликлинику",
                                bg='#DEFDFF',
                                fg='#99004C',
                                font=('Arial', 28, 'bold'),
                                pady = 200
                                )
                name.pack()
            else:
                root = tk.Tk()
                root.geometry('720x480+400+100')
                root.config(bg='#DEFDFF')
                name = tk.Label(root, text="Оу... Кажется, вы нуждаетесь в госпитализации!",
                                bg='#DEFDFF',
                                fg='#99004C',
                                font=('Arial', 28, 'bold'),
                                pady = 200
                                )
                name.pack()
            return c
        quest.delete('1.0', 'end')
        variants.delete('1.0', 'end')
        quest.insert(tk.INSERT, Text_q[qc])
        quest.pack()
        variants.insert(tk.INSERT, Text_dict[Text_q[qc]][0]+'\n')
        variants.insert(tk.INSERT, Text_dict[Text_q[qc]][1]+'\n')
        variants.insert(tk.INSERT, Text_dict[Text_q[qc]][2]+'\n')
        variants.insert(tk.INSERT, Text_dict[Text_q[qc]][3]+'\n')
        variants.pack()
        a = entry.get()
        if a not in ['1','2','3','4']:
           a = 0
        probability += int(a)
        qc += 1
        entry.delete(0, END)


    ButNext = tk.Button(text='Следующий',
                        font=('Arial Bold', 18),
                        command=question,
                        bg='#DEFDFF',
                        fg='#99004C',
                        activebackground='green'
                        )
    ButNext.pack()
    #first_block = Block(window, Text_dict, Text_q)

    window.mainloop()
    return c
