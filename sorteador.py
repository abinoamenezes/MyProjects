import tkinter as tk
from tkinter import Label, Scrollbar, ttk
import re
import random
from tkinter.messagebox import showinfo



class Jan(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sorteador')
        self.geometry('600x400+600+250')
        self.config(background='#ADD8E6')

        self.lbl_sort=Label(self,text='Sorteador de nomes',font='Arial 24',foreground='#FF4500',bg='#ADD8E6')
        self.lbl_sort.place(x=140,y=5)

        self.camp=tk.Text(self,width=50,height=10, pady=10,font='Arial 10')
        self.camp.focus()
        
        
        self.camp.place(x=110,y=59)


        self.btn=tk.Button(self,text='Sortear',width=15,height=2,font='Arial 11',command=self.sortear)
        self.btn.place(x=195,y=270)

    def sortear(self):
       x =self.camp.get('0.0','end')
       lis=re.split('\n',x)
       
       for y in lis:
            if y=='':
                lis.remove(y)
       
       nome_sorteador=random.choice(lis)
       print(nome_sorteador)
       showinfo(title='Resultado',message=f'O nome sorteado foi {nome_sorteador}')
            



app=Jan()
app.mainloop()