import random
import string
import pyperclip  #pip install pyperclip

keys=''
while keys !='q':

    print("\nGenerador de contraseñas")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation
    chars = lowercase + uppercase + nums + symbols
    
    keys = input("Longitud contraseña (25 por defecto)?")
    if keys.isdigit():longitud=int(keys)
    else: longitud=25
    if longitud>94: longitud=94

    temp = random.sample(chars, longitud)
    temp="".join(temp)
    print(temp)
    pyperclip.copy(temp)

    keys = input("Contraseña copiada al portapapeles\nPulsa 'q' para salir: ")
