
#Ejercicio 1. Calcular el mayor de dos números ingresados por teclado usando un operador
#ternario.#

def calcular_mayor(*args, **kwargs):
    num1 = args[0]  
    num2 = kwargs.get('num2')  
    mayor = num1 if num1 > num2 else num2
    return mayor

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

resultado = calcular_mayor(numero1, num2=numero2)

print(f"El mayor número es: {resultado}")










