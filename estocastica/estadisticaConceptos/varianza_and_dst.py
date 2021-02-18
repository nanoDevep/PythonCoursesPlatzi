import random
import math

def media(numeros):
    return sum(numeros) / len(numeros)

def varianza(numeros):
    media_n = media(numeros)
    sumatoria = 0
    for i in numeros:
        sumatoria += (i - media_n) ** 2
    
    return sumatoria / len(numeros)

def desviacionEst(numeros):
    return math.sqrt(varianza(numeros))
    


if __name__ == '__main__':
    # numeros = [random.randint(18, 21) for i in range(10)]
    numeros = [1, 1, 1, 1, 2]
    media_n = media(numeros)
    Var = varianza(numeros)
    dst = desviacionEst(numeros)

    print(numeros)
    print('La media es:', media_n)  
    print('La varianza es:', Var)
    print('La desviacion estandar es:', dst)

    valores = (68, 95, 99.7)
    for i in range(3):
        print(f'El  {valores[i]}% de los datos estan entre [{media_n-(i+1*dst)}, {media_n+(i+1*dst)}')

        