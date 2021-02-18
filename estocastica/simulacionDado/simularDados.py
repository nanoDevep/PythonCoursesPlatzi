import random

def tirar(numero_de_tiros):
    resultados = []
    for _ in range(numero_de_tiros):
        resultados.append(random.choice((1,2,3,4,5,6)))
    
    return resultados


def tirar_dado(numero_de_tiros, numero_de_repeticiones):
    resultados_tiros = []

    for _ in range(numero_de_repeticiones):
        resultado = tirar(numero_de_tiros)
        resultados_tiros.append(resultado)

    veces_1 = 0
    
    for i in resultados_tiros:
        if  1 in i:
            veces_1 += 1    
        
    print(f'La probabilidad de que nos salga uno es {veces_1 / numero_de_repeticiones}')
    


if __name__ == '__main__':
    numero_de_repeticiones  = int(input('Repetir cuantas veces?: '))
    numero_de_tiros = int(input('Cuantas veces tiramos el dado por repeticion: '))


    tirar_dado(numero_de_tiros, numero_de_repeticiones)


