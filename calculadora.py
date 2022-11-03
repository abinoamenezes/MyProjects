from tkinter import *
from tkinter import ttk

#cores
#f2faf2'  #branca
##8dade0 #azul
valor=''
#adicionando valores na tela
def adicionar_valor(event):
    global valor
    valor= valor + event
    strva.set(valor)
 

 #calculando as expressões 
def calcular():
   strva.set(eval(strva.get())) 
   global valor
   valor=''

#apagando
def clean():
   strva.set('')
   global valor
   valor=''

    




root=Tk()
root.title('Calculadora')
root.geometry('239x288')
root.config(background='#181c18')
root.resizable(False, False)

#frame cima
frame_visor=Frame(
    root,
    width=239,
    height=50,
    background='#526152'
)
frame_visor.grid(row=0,column=0)


#frame baixo
frame_button=Frame(
    root,
    width=239,
    height=290,
    background='#1a1c1a'
)
frame_button.grid(row=1,column=0)

strva=StringVar()

#Label visor
visor=Label(
    frame_visor,
    width=16,
    height=2,
    font='Arial 20',
    relief='flat',
    background='white',
    textvariable=strva,
    )
visor.place(x=1,y=1)

#butão apagar
button_apagar=Button(
    frame_button,
    text='Limpar',
    width=10,
    height=2,
    background='red',
    foreground='white',
    cursor="pirate",
    command=clean

    
)
#botoẽs
button_apagar.place(x=0,y=2)

button_porcent=Button(
    frame_button,
    text='%',
    font='Arial 20',
    background='#f2faf2',
    foreground='Black',
    height=1,
    width=2,
    pady=5.5,
    cursor='hand1',
    command=lambda: adicionar_valor('%')
)
button_porcent.place(x=110,y=2)

button_dividir=Button(
    frame_button,
    text='/',
    font='Arial 20',
    background='#8dade0',
    foreground= 'white',
    height=1,
    width=2,
    padx=15,
    pady=5.5,
    cursor='hand1',
   command=lambda:adicionar_valor('/')


)
button_dividir.place(x=170,y=2)

button_num7=Button(
    frame_button,
    text='7',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=16,
    cursor='hand1',
    command=lambda: adicionar_valor('7')

)
button_num7.place(x=0,y=52)

button_num8=Button(
    frame_button,
    text='8',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=16,
    cursor='hand1',
    command=lambda: adicionar_valor('8')
    

)
button_num8.place(x=55,y=52)


button_num9=Button(
    frame_button,
    text='9',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=18,
    cursor='hand1',
    command=lambda: adicionar_valor('9')

)
button_num9.place(x=110,y=52)

button_Multiplicar=Button(
    frame_button,
    text='*',
    font='Arial 20',
    background='#8dade0',
    foreground= 'white',
    height=1,
    width=2,
    padx=15,
    pady=4,
    cursor='hand1',
    command=lambda: adicionar_valor('*')


)
button_Multiplicar.place(x=170,y=52)

button_num4=Button(
    frame_button,
    text='4',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=16,
    cursor='hand1',
    command=lambda: adicionar_valor('4')
    
    

)
button_num4.place(x=0,y=98)


button_num5=Button(
    frame_button,
    text='5',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=16, 
    cursor='hand1',
    command=lambda: adicionar_valor('5')   

)
button_num5.place(x=55,y=98)

button_num6=Button(
    frame_button,
    text='6',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=18, 
    cursor='hand1',
    command=lambda: adicionar_valor('6')   

)
button_num6.place(x=110,y=98)

button_menos=Button(
    frame_button,
    text='-',
    font='Arial 20',
    background='#8dade0',
    foreground= 'white',
    height=1,
    width=2,
    padx=15,
    pady=4,
    command=lambda: adicionar_valor('-')


)
button_menos.place(x=170,y=98)

button_num1=Button(
    frame_button,
    text='1',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=16,
    cursor='hand1',
    command=lambda: adicionar_valor('1')
    
)
button_num1.place(x=0,y=144)

button_num2=Button(
    frame_button,
    text='2',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=16,
    cursor='hand1',
    command=lambda: adicionar_valor('2')

)
button_num2.place(x=55,y=144)


button_num3=Button(
    frame_button,
    text='3',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=18,
    cursor='hand1',
    command=lambda: adicionar_valor('3')

)
button_num3.place(x=110,y=144)

button_mais=Button(
    frame_button,
    text='+',
    font='Arial 20',
    background='#8dade0',
    foreground= 'white',
    height=1,
    width=2,
    padx=15,
    pady=4,
    cursor='plus',
    command=lambda: adicionar_valor('+')


)
button_mais.place(x=170,y=144)

button_num0=Button(
    frame_button,
    text='0',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=4,
    padx=21,
    cursor='hand1',
     command=lambda: adicionar_valor('0')
    

)
button_num0.place(x=0, y=190)

button_ponto=Button(
    frame_button,
    text='.',
    font='Arial 20',
    background='#f2faf2',
    foreground= 'black',
    height=1,
    width=1,
    padx=18,
    cursor='hand1',
    command=lambda: adicionar_valor('.')
   
    

)
button_ponto.place(x=110, y=190)

button_igual=Button(
    frame_button,
    text='=',
    font='Arial 20',
    background='green',
    foreground= 'white',
    height=1,
    width=2,
    padx=15,
    pady=4,
    cursor='hand2',
    command=calcular
  

)
button_igual.place(x=170,y=190)


root.mainloop()