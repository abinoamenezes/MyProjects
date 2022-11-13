import tkinter as tk
from tkinter import ttk

def adicionar():
    
    jan=tk.Tk()
    jan.geometry('400x200+750+120')
    lbl=ttk.Label(jan,text='Digite aqui os registros(separados por virgulas)')
    lbl.place(x=0,y=5)
    strvar=tk.StringVar()
    entry_dados=ttk.Entry(jan,width=35,textvariable=strvar)
    entry_dados.place(x=0,y=25)
    def adicionar2():
        jan.destroy()
    btn_confirma=ttk.Button(jan,text='confirmar',command=adicionar2)
    btn_confirma.focus()
    btn_confirma.place(x=10,y=49)
    jan.mainloop()

   
        
    

root=tk.Tk()
root.geometry('1000x400+450+30')

root.title('tabelas')

frame=ttk.Frame(root,width=1000,height=400)
frame.grid(row=0,column=0)
tabela1=ttk.Treeview(
    frame,
    columns=['nome', 'idade','email','profissao'],
    height=15,

)
tabela1.heading('nome',text='Nome')
tabela1.heading('idade',text='Idade')
tabela1.heading('email',text='e-mail')
tabela1.heading('profissao',text='Profissão')

tabela1.grid(row=0,column=0)

btn_adicionar=tk.Button(text='adicionar na tabela',command=adicionar)
btn_adicionar.grid(row=1,column=0,pady=10)







root.mainloop()