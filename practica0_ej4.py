"""
4. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 5, 
comenzando con el intervalo [1,2], y el error epsilon = 0.5.
"""
import decimal

def funcion(x):
    
    return x**3 + x -5


def ciclo(limite_a, limite_b, epsilon):
    
    while((limite_b - limite_a) >= epsilon):
        promedio = (limite_b + limite_a) / 2
        valor = funcion(promedio)
        if(valor == 0):
            flag = True
            break
        if(valor * funcion(limite_a) < 0):
            limite_b = valor
        else:
            limite_a = valor
    return promedio


if __name__ == '__main__':
    
    epsilon = 0.5
    limite_a = 1
    limite_b = 2
    flag = False
    
    valorRaiz = ciclo(limite_a, limite_b, epsilon)

    if(flag):
        print(f"Se encontro una raiz de valor {valorRaiz}")
    else:
        print(f"Valor aprox de la raiz {valorRaiz}")