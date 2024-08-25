import string
import random

#Mostrar en pantalla los caracteres que seran tomados para generar la clave randomizada
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#Tambien podriamos indicar manualmente que caracteres pueden ser utilizados para la clave
# caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_-/"

#Funcion para generar nueva clave utilizando un for in
def generar_clave(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    clave = ""
    for i in range(longitud):
        clave += random.choice(caracteres)
    return clave

#Solicitamos al usuario indique de que tamaño desea la clave
longitud = int(input ("Indicar longitud de la clave deseada: "))

#Esta sera la variable que tomara el valor devuelto por la funcion
nueva_clave = generar_clave(longitud)

#mostramos resultado.
print("La nueva contraseña es: ", nueva_clave)
