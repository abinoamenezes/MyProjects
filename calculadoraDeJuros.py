import tkinter as tk
from tkinter import ttk

class RootMain (tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('450x350+650+200')
        self.title('Calculadora de juros')


class FrameMain(ttk.Frame):
    def __init__(self, conteiner):
        super().__init__(conteiner,width=450,height=270)

        #criando widgts

        lbl_titulo=ttk.Label(self,text='hello',font='Arial 20 bold')
        lbl_titulo.grid(row=0,column=0,columnspan=2)

        self.grid(row=0,column=0)


        lbl_capital=ttk.Label(self,text='Capital')
        lbl_capital.grid(row=1,column=0,pady=10)

        entry_capital=ttk.Entry(self)
        entry_capital.grid(row=1,column=1,pady=10)

        lbl_juros=ttk.Label(self, text='Juros')
        lbl_juros.grid(row=2,column=0,pady=10)

        entry_juros=ttk.Entry(self)
        entry_juros.grid(row=2,column=1)
        
        

root=RootMain()
frame=FrameMain(root)
root.mainloop()



