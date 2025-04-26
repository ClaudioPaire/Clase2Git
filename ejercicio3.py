#Escribe  un  programa  que  intente  acceder  a  una  clave  que  no  existe  en  undiccionario. Si se produce una excepción KeyError, 
# captura la excepción y muestraun mensaje de error al usuario.


try:
    diccionario = {"apellido": "funes", "edad": 40}
    print(diccionario["nombre"])

except KeyError:    
    print("se ha producido un error, no se encuentra esa clave en el diccionario")