from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.tix import NoteBook

def calculo_água(event):
    peso=strva.get()
    qtd= eval(f'{peso}*0.035')
    showinfo(
        title='Aviso',
        #message=f'Sua quantidade de aguá diaria tem que ser de {qtd:.1f} Litros. Ingira {} copos de 200ml'
    )
    


root=Tk()

root.geometry('400x250+450+200')
root.title('Controle de água')

image=PhotoImage(file='Meus/copo-de-agua.png')
root.wm_iconphoto(False,image)

note=ttk.Notebook(root)
note.grid(row=0,column=0)

fra=Frame(
    note,
    width=600,
    height=450,
    background='#00BFFF'
)
fra.grid(row=0,column=0)

note.add(fra,text='Calculo ')

strva=StringVar()

entry_peso=ttk.Entry(
    fra,
    width=20,
    textvariable=strva
)
entry_peso.bind('<Return>',calculo_água)
entry_peso.place(x=5,y=20)


lbl_peso=Label(fra,text='Digite aqui seu peso(kg)',bg='#00BFFF',foreground='black')
lbl_peso.place(x=170,y=20)

root.mainloop()