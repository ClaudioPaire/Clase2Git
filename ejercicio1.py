#1.Escribe un programa que intente dividir dos números. Si el segundo número es cero,captura la excepción ZeroDivisionError y muestra un mensaje 
# de error al usuario.#

num1= 25
num2= 0

try:
    resultado = num1 / num2
    print(resultado)
except ZeroDivisionError:    
    print("se ha producido un error, no se puede dividir por cero")