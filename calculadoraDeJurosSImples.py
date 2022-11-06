import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


class RootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x200')
        ttk.Label(self,text='Calculadora de Juros Simples',font='Copperplate 10 bold').place(x=8,y=5)

        self.config(bg='#A9A9A9')

        self.strvar_capita=tk.StringVar()
        ttk.Label(self,text='Capital',font='arial 12').place(x=8,y=55)
        self.entry_capita=ttk.Entry(self,width=20,textvariable=self.strvar_capita).place(x=70,y=55)

        self.strvar_tempo=tk.StringVar()
        ttk.Label(self,text='Tempo(m)',font='arial 12').place(x=8,y=85)
        self.entry_tempo=ttk.Entry(self,width=18,textvariable=self.strvar_tempo).place(x=86,y=85)


        self.strvar_taxa=tk.StringVar()
        ttk.Label(self,text='Taxa',font='arial 12').place(x=8,y=115)
        self.entry_taxa=ttk.Entry(self,width=20,textvariable=self.strvar_taxa).place(x=70,y=115)

        self.btn_calcular=ttk.Button(self,text='calcular',width=20,command=self.calcular).place(x=40,y=150)

    
    def  calcular(self):
        result=eval(f'{self.strvar_capita.get()} * {self.strvar_tempo.get()} * ({self.strvar_taxa.get()}/100)')
        montante=result + float(self.strvar_capita.get())
        showinfo(title='informação',message=f'O valor do juros será de {result} e o montante será de {montante} reais')
        




roo=RootMain()
roo.mainloop()


