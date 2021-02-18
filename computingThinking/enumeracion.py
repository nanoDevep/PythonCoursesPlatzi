import time
def enumeracionMenosPrecisa():
    objetivo = int(input('Ingresa un numero para mirar si tiene una raiz cuadrada: '))
    respuesta = 0
    tiempo_inicial = time.time()

    while respuesta ** 2 < objetivo:
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f'El numero {objetivo} tiene de raiz y es {respuesta}')
    else:
        print(f'El numero {objetivo} no tiene de raiz cuadrada exacta ')

    ahora = time.time()
    print(f'Tiempo transcuerrido: {ahora-tiempo_inicial}')

