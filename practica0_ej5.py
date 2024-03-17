#5. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 10 haciendo 4 pasos.

#La cantidad de pasos que de va a depender mucho de los limites que establezcamos. 

def f(x):
    return (x**3) + x - 10

limite_a = 1
limite_b = 3
epsilon = 0.1
i = 0

while((abs(limite_a - limite_b) > epsilon) and (i < 4)):
    print(f"Iteración {i}")
    promedio = (limite_a + limite_b) / 2
    valor = f(promedio)
    if(valor == 0):
        break
    if((f(limite_a) * valor) < 0):
        limite_b = promedio
    else:
        limite_a = promedio
    i+=1

print("")
print(f"Valor de la raiz {promedio} resuelta en la iteracion {i}")
    