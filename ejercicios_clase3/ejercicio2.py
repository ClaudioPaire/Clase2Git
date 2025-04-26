
#Ejercicio 2. Buscar una palabra en una lista ingresada por teclado usando args y un operador
#ternario

def buscar_palabra(*args):
    lista = args[0]  
    palabra = args[1]  
    
    resultado = "La palabra está en la lista" if palabra in lista else "La palabra no está en la lista"
    return resultado

entrada_lista = input("Ingresa palabras separadas por comas: ").split(",") 
palabra_buscada = input("Ingresa la palabra que deseas buscar: ")


mensaje = buscar_palabra(entrada_lista, palabra_buscada)

print(mensaje)