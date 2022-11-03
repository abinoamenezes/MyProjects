from cProfile import label
from textwrap import fill
from tkinter import *
from tkinter import ttk,Tk
from tkinter.messagebox import showinfo, showwarning


#função que verifica senha e usuário
dados=['abino69', 'abino8986']


def verificar_login():
    if dados[0]==entry_nome.get() and dados[1]==entr_senha.get():
        showinfo(title='Aviso',message=f'Bem-Vindo {dados[0]}')
    
    else:
        showwarning(title='Aviso', message='Senha ou usuário incorreto')
        entry_nome.focus()
        entry_nome.select_range(0,END)


#criando janela
root=Tk()
root.geometry('350x340+600+200')
root.title('Login')
root.resizable(width=False, height=False)
root.config(background='white')

#dividindo a janela
frame_cima=Frame(
    root,
    background='white',
    width=350,
    height=80,
    relief='flat'
    
)
frame_cima.grid(row=0,column=0,sticky=NSEW)

frame_baixo=Frame(
    root,
    background='white',
    width=350,
    height=200,
    relief='flat'
    
)
frame_baixo.grid(row=1,column=0,sticky=NSEW)

#configuraFrameCIma

lbl_cima=Label(
    frame_cima,
    font='Arial 30 bold',
    anchor='w',
    text='LOGIN',
    background='white',
    foreground='green'
)
lbl_cima.place(x=5,y=5)

lbl_traco=Label(
    frame_cima,
    background='red',
    width=330,
    text='',
    font='Arial 1'
    
)
lbl_traco.place(y=50,x=5)

#configurando frame em Baixo

lbl2= Label(
    frame_baixo,
    text='Usuário *',
    font='Arial 12',
    background='white'
)
lbl2.grid(row=0,column=0,sticky='w',pady=10,padx=5)

entry_nome=Entry(
    frame_baixo,
    width=40
)
entry_nome.focus()
entry_nome.grid(column=0,row=1,padx=5)

lbl3= Label(
    frame_baixo,
    text='Senha *',
    font='Arial 12',
    background='white'
)
lbl3.grid(row=3,column=0,sticky='w',pady=10,padx=5)

entr_senha=Entry(
    frame_baixo,
    width=40,
    show='*'

)
entr_senha.grid(column=0,row=4,padx=5,sticky='w')


#Botão de logar
buto_entra=Button(
    root,
    font='Arial 20',
    background='orange',
    foreground='black',
    text='Entrar',
    command=verificar_login

)
buto_entra.place(x=5,y=250,width=340)



root.mainloop()

