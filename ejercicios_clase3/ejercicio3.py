
#Ejercicio 3. Determinar si un número es par o impar.

def determinar_paridad(numero):
    
    resultado = "El número es par" if numero % 2 == 0 else "El número es impar"
    return resultado

numero = int(input("Ingresa un número: "))

mensaje = determinar_paridad(numero)
print(mensaje)