import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title('Gerador de senhas')
root.geometry('570x350+950+200')
root.config(bg='#ADD8E6')

label_text=ttk.Label(root,text='Crie sua senha', font='Arial 20',background='#ADD8E6')
label_text.place(x=200, y=10)

label_tamanho=ttk.Label(root,text='Qual tamanho da sua senha?',font='Arial 12',background='#ADD8E6')
label_tamanho.place(x=5,y=70)


entry_tamanho=ttk.Entry(root, width=10)
entry_tamanho.place(x=230,y=70)


label_numero=ttk.Label(root,text='Sua senha possuirá números?',font='Arial 12',background='#ADD8E6')
label_numero.place(x=5, y=110)

btn_numero_sim=ttk.Button(root,text='yes')
btn_numero_nao=ttk.Button(root,text='no')
btn_numero_sim.place(x=250,y=110)
btn_numero_nao.place(x=343,y=110)

label_nome=ttk.Label(root,text='Sua senha possuirá letras? (yes/no)',font='Arial 12',background='#ADD8E6')
label_nome.place(x=5,y=150)

btn_nome_sim=ttk.Button(root,text='yes')
btn_nome_nao=ttk.Button(root,text='no')
btn_nome_sim.place(x=270,y=150)
btn_nome_nao.place(x=363,y=150)



label_carcter=ttk.Label(root,text='Sua senha possuirá caracteres especiais?',font='Arial 12',background='#ADD8E6')
label_carcter.place(x=5,y=190)

btn_cara_sim=ttk.Button(root,text='yes')
btn_cara_nao=ttk.Button(root,text='no')
btn_cara_sim.place(x=320,y=190)
btn_cara_nao.place(x=413,y=190)

btn_gerar=ttk.Button(root,text='Gerar senha')
btn_gerar.place(x=200,y=260,width=200)

root.mainloop()
