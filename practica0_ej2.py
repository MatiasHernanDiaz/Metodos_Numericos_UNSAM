"""
2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones, una f y una g, 
y que la aplicación iterada sea una vez f, luego g, luego f, luego g, y así siguiendo, 
alternando una con otra, en total las veces que se especifique por el parámetro n, 
y finalmente devuelva el resultado obtenido tras la última aplicación.
"""

import math

def pedirDatos():
    valor = int(input('Ingrese el valor de X: '))
    cantidad = int(input('Ingrese la cantidad de aplicacion de funciones: '))
    return valor, cantidad

def ciclo(valor, cantidad):
    i = 0
    while(i < cantidad):
        if(i % 2 == 0):
            valor = math.pow(valor, 3)
        else:
            valor = math.sin(valor)
        i += 1
    return valor

if __name__ == "__main__":
    valor, cantidad = pedirDatos()

    print(f"Valor inicial de X = {valor}, valor final {ciclo(valor, cantidad)}")