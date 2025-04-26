
#Ejercicio 5. Imprimir un mensaje de error si no se pasan suficientes argumentos.

def verificar_argumentos(*args, **kwargs):
    
    if len(args) < 2 or len(kwargs) < 1:
        return "Error: No se pasaron suficientes argumentos."
    else:
        return "¡Se pasaron suficientes argumentos!"

print(verificar_argumentos(1))  
print(verificar_argumentos(1, 2, nombre="Python"))  
print(verificar_argumentos(nombre="Python"))  