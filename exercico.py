from ast import Str
from cgitb import text
import tkinter as tk
from tkinter import Button, ttk
from tkinter.messagebox import showinfo
from turtle import width

def info_candidatos(event):
   if strvar.get()=='bolsonaro':
    infors=tk.Text(root,width=100,foreground='yellow',background='blue')
    infors.insert('0.1',"""Número: 22\nidade:67\nnome completo:Jair Messias Bolsonaro
Cargo atual: Presidente da república
Partido: Partido Liberal(Pl)
""")
    infors.config(state='disabled')
    infors.grid(column=0,row=3)
   elif strvar.get()=='lula':
        infors=tk.Text(root,width=100,foreground='white',background='red')
        infors.insert('0.1',"""Número: 13\nidade:76\nnome completo:Luiz Inácio Lula da Silva
Cargo atual: nenhum
Partido: Partido dos Trabalhadores(PT)
""")
        infors.config(state='disabled')
        infors.grid(column=0, row=3)
   else:
        showinfo(
            title='Erro',
            message='Cadidato(a) não está concorrendo a presidente da república',
        )
       
root=tk.Tk()

root.title('treino')
root.geometry('600x400+650+100')

lbl1=ttk.Label(
    root,
    text='Em qual candidato a  presidente voçê irá votar?'
    
)
lbl1.grid(column=0,row=0,sticky='w')

strvar=tk.StringVar()
strvar.set('Digite aqui o nome do candidato...')

nome_presidente=ttk.Entry(
    root,
    textvariable=strvar,
    width=30, 
    font='Arial 10'
)
nome_presidente.select_range(0,tk.END)
nome_presidente.focus()
nome_presidente.bind('<Return>',info_candidatos)
nome_presidente.grid(column=1,row=0,sticky='W')


Butto=tk.Button(
    root,
    text='Clique aqui',
    foreground='green',
    command=lambda:info_candidatos(None)

)
Butto.grid(column=0,row=2,sticky='w')

root.mainloop()