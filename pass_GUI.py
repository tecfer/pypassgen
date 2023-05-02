import random
import string
import pyperclip 
from tkinter import Tk, LabelFrame,Label, Entry, IntVar, Button, Checkbutton, W, mainloop


root = Tk()
root.title("Calculadora contraseñas")
root.iconbitmap("img/loock.ico")
root.geometry("238x248")
root.resizable(False, False)


def generar():
    
    lower = string.ascii_lowercase         
    upper = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation

    chars = ""
    if lowercase_int.get():
        chars = chars + lower
    if uppercase_int.get():
        chars = chars + upper
    if nums_int.get():
        chars = chars + nums
    if symbols_int.get():
        chars = chars + symbols
        
    try:
        largo =int(longitud.get())
    except: 
        largo=25
    if largo<4:
        largo=4 
    if largo > len(chars):
        largo = len(chars)       

    temp = random.sample(chars, largo)
    temp="".join(temp)
    try:
        pyperclip.copy(temp)
    except:
        labelPass = Label(root, text="Error al copiar al portapapeles").grid(row=3, column=0)
    else: 
        labelPass = Label(root, text="Clave copiada al portapapeles").grid(row=3, column=0)

    resultado.delete(0, "end")
    resultado.insert(0, temp)


opciones = LabelFrame(root, text="Opciones", padx=50)
opciones.grid(row=0, column=0, padx=3, pady=3)

longitud = Entry(opciones)
longitud.pack()
longitud.insert(0, "20")

lowercase_int = IntVar()
lowercase = Checkbutton(opciones, text="Minusculas", variable=lowercase_int, padx=10, pady=3)
lowercase.pack(anchor=W)
lowercase.select()

uppercase_int = IntVar()
uppercase = Checkbutton(opciones, text="Mayusculas", variable=uppercase_int, padx=10, pady=3)
uppercase.pack(anchor=W)
uppercase.select()

nums_int = IntVar()
nums = Checkbutton(opciones, text="Números", variable=nums_int, padx=10, pady=3)
nums.pack(anchor=W)
nums.select()

symbols_int = IntVar()
symbols = Checkbutton(opciones, text="Symbolos", variable=symbols_int, padx=10, pady=3)
symbols.pack(anchor=W)
symbols.select()

buton1 = Button(root, text="Generar", bg="orange", padx=50, 
                pady=5, command=generar ).grid(row=1, column=0)

resultado = Entry(root, width=30)
resultado.grid(row=2, column=0, padx=3, pady=3)
resultado.insert(0, "")


mainloop()