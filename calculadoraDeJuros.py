import tkinter as tk
from tkinter import ttk

class calculos:
    @staticmethod
    def calculo_simples():
        frame.lbl_respostas.config(text=eval(f'{frame.strvar_capital.get()}* 1+ {frame.strvar_taxa.get()}* {frame.strvar_tempo.get()}'))
        
    
    def calculo_composto():
        montate=eval(f'{frame.strvar_capital.get()}*(1 + {frame.strvar_taxa.get()})**{frame.strvar_tempo.get}')
        return f'Montante: {montate}'
 

class RootMain (tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('450x250+650+200')
        self.title('Calculadora de juros')


class FrameMain(ttk.Frame):
    def __init__(self, conteiner):
        super().__init__(conteiner,width=450,height=170)

        #criando widgts

        self.lbl_titulo=ttk.Label(self,text='hello',font='Arial 20 bold')
        self.lbl_titulo.place(x=150,y=5)

        


        self.lbl_capital=ttk.Label(self,text='Capital')
        self.lbl_capital.place(x=5,y=45)

        self.strvar_capital=tk.StringVar()

        self.entry_capital=ttk.Entry(self,width=15,textvariable=self.strvar_capital)
        self.entry_capital.place(x=57,y=45)
        

        self.lbl_juros=ttk.Label(self, text='Juros')
        self.lbl_juros.place(x=5,y=80)
        
        self.strvar_juros=tk.StringVar()

        self.entry_juros=ttk.Entry(self,width=15,textvariable=self.strvar_juros)
        self.entry_juros.place(x=57,y=80)
       
        self.lbl_taxa_juros=ttk.Label(self,text='Taxa de juros')
        self.lbl_taxa_juros.place(y=45,x=220)


        self.strvar_taxa=tk.StringVar()

        self.entry_taxa_juros=ttk.Entry(self,width=15,textvariable=self.strvar_taxa)
        self.entry_taxa_juros.place(x=320,y=45)

        self.lbl_tempo=ttk.Label(self,text='tempo(meses)')
        self.lbl_tempo.place(x=215, y=85)

        self.strvar_tempo=tk.StringVar()

        self.entry_tempo=ttk.Entry(self,width=15,textvariable=self.strvar_tempo)
        self.entry_tempo.place(x=320,y=85)

        self.btn_calcular=ttk.Button(self,text='Calcular',width=12)
        self.btn_calcular.place(x=180,y=125)
        

        self.lbl_respostas=ttk.Label(self)
        self.lbl_respostas.place(x=100,y=125)

        self.grid(row=0,column=0)

class labelFrame(ttk.Labelframe):
    def __init__(self,container):
        super().__init__(container,text='options')

        #radioButton
        self.strSimples=tk.StringVar()
        self.radioBUtton_simples=ttk.Radiobutton(
            self,
            text='Juros simples'
            ,value='0'
            ,variable=self.strSimples,
            command=self.chamar
            )
        self.radioBUtton_simples.grid(row=0,column=0)


        self.radioBUtton_composto=ttk.Radiobutton(self,text='Juros Composto',value='1',variable=self.strSimples,command=self.chamar)
        self.radioBUtton_composto.grid(row=0,column=1)


        self.grid(column=0,row=1)



    def chamar(self):
        if self.strSimples.get()=='0':
            frame.btn_calcular.config(command=calculos.calculo_simples)
            
            
        else:
            frame.btn_calcular.config(command=calculos.calculo_composto)


    
        

root=RootMain()
frame=FrameMain(root)
label=labelFrame(root)
root.mainloop()



