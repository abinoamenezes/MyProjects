from tkinter import *
from tkinter import ttk
from turtle import width
import tkcalendar as tc
root=Tk()

root.geometry('400x400+650+150')
root.title('Calculadora de idade')


#criando frames
frame_cima=Frame(
    root,
    width=400,
    height=150,
    background='#4F4F4F'
)
frame_cima.grid(row=0,column=0)

frame_baixo=Frame(
    root,
    width=400,
    height=250,
    background='#1C1C1C'
)
frame_baixo.grid(row=1,column=0)

#criando labels cima
lbl_cima1=Label(
    frame_cima,
    text='CALCULADORA',
    font='Cambria 15',
    background='#4F4F4F',
    foreground='#FFD700'
)
lbl_cima1.place(x=120,y=24)

lbl_cima2=Label(
    frame_cima,
    text='DE IDADE',
    font='Cambria 35',
    background='#4F4F4F',
    foreground='#7FFFD4'
)
lbl_cima2.place(x=80,y=64)

#Criando Labels e buttons no frame_baixo

lbl_baixo1=Label(
    frame_baixo,
    text='Data inicial',
    font='Arial 15',
    background='#1C1C1C',
    foreground='white'
)
lbl_baixo1.place(x=20,y=20)

entry_baixo1=tc.DateEntry(
    frame_baixo,
    width=13,
    date='dd/mm/y',
    y=2022,
    bg='blue'
)
entry_baixo1.pla(x=40,y=47)

lbl_baixo2=Label(
    frame_baixo,
    text='Data de nascimento',
    font='Arial 15',
    background='#1C1C1C',
    foreground='white'

)
lbl_baixo2.place(x=20,y=47)

root.mainloop()

