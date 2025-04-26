#2.Escribe un programa que intente sumar un número y una cadena. Si se produce un errorde tipo, captura la excepción TypeError y muestra un 
##mensaje de error al usuario.#

num1 = 8
num2 = "gfrted"


try:
    resultado = num1 + num2
    print(resultado)
except TypeError:    
    print("se ha producido un error, no se puede sumar un entero y una cadena de texto")


