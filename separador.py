import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.geometry('600x400+150+200')

lbl1=ttk.Label(
    root,
    text='Label1',
)
lbl1.pack()

separador= ttk.Separator(
    root,
    orient='horizontal',

)
separador.pack(fill='x')

lbl2=ttk.Label(
    root,
    text='label2'

)
lbl2.pack()

root.mainloop()