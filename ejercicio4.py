#4. Escribe un programa que intente abrir un archivo que no existe. 
# Si se produce una excepción FileNotFoundError,  captura  la  excepción  y  muestra  un  mensaje  de  error  al  usuario.  
# Sin embargo, también intenta crear el archivo si no existe.


try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe")

