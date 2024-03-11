"""
1. Implementar en Python el proceso anterior, que use una función 
(externa implementada, o bien pasada como parámetro), que lea el x como 
parámetro y un n natural, y luego sobre el ex inicial aplique la f n veces, 
finalmente devolviendo el resultado obtenido tras la última aplicación.

"""
import math

def aplicarFuncionCos(numero: int, cantidad: int):
    i = 0
    while( i < cantidad):
        numero = math.cos(numero)
        i += 1
    return numero

if __name__ == '__main__':
    print("""
            Utilizando la libreria math se aplicara Cos a un X ingresado una cierta cantidad de veces
          """)
    numero = int(input("Ingrese el valor de X: "))
    cantidad = int(input("Ingrese la cantidad: "))
    print(f"Valor inicial de X = {numero}, valor aplicando Cos {cantidad} veces = {aplicarFuncionCos(numero, cantidad)}")