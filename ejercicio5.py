#Escribe  un  programa  que  intente  dividir  dos  números.  Si  el  segundo  número  es  cero,captura  la  excepción  ZeroDivisionError.  
#Si  el  primer  número  es  un  número  no  válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

try:
    num1 = 15  
    num2 = 0   
    
    print(f"El resultado de la división es: {num1 / num2}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: ingrese un número válido.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")