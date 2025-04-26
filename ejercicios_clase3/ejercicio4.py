
#Ejercicio 4. Calcular el promedio de una lista de números usando args y un operador ternario

def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else "La lista está vacía"
    return promedio

entrada = input("Ingresa números separados por comas: ").split(",")
numeros = [float(num) for num in entrada]  # Convertir los valores a flotantes

resultado = calcular_promedio(*numeros)

print(f"El promedio es: {resultado}" if isinstance(resultado, float) else resultado)