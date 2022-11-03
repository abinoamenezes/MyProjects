import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.scrolledtext import ScrolledText
from turtle import width

root= tk.Tk()
root.title('python tkinter')

st= ScrolledText(
    root,
    width=100,
    height=10,
    font='Arial 25'
)
st.pack(expand=True, fill='both')

root.mainloop()