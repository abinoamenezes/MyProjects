import tkinter as tk
from tkinter import ttk

class RootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x350')
        ttk.Label(self,text='Calculadora de Juros Simples',font='Copperplate 10 bold').place(x=8,y=5)

        ttk.Label(self,text='Capital',font='arial 12').place(x=8,y=55)
        entry_capita=ttk.Entry(self,width=20).place(x=70,y=55)

        ttk.Label(self,text='Tempo(m)',font='arial 12').place(x=8,y=85)
        entry_tempo=ttk.Entry(self,width=18).place(x=86,y=85)




roo=RootMain()
roo.mainloop()


