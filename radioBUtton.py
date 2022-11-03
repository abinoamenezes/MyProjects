import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()

str=tk.StringVar()

root.geometry('600x500+120+100')

tk.Label(
    root,
    text='Qual seu candiato',  
).pack()


opcao1=ttk.Radiobutton(
    root,
    text='bolsonaro',
    value='bolsonaro',
    variable=str
)
opcao1.pack()

opcao2=ttk.Radiobutton(
    root,
    text='Lula',
    value='Lula',
    variable=str
)
opcao2.pack()

buto=ttk.Button(
    root,
    text='Clique aqui para confirma seu voto',
    command=lambda: showinfo(
        title='voto',
        message=f'Seu candidato é {str.get()}'
    )
)
buto.pack()




root.mainloop()