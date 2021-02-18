def aproximacionTodasCombinaciones():
    numero_objetivo = int( input('Introduce un numero para buscar su raiz cuadrada: ') )
    epsilon = float(input('Cual es el margen de error?: '))
    respuesta = 0
    paso = epsilon ** 2
    veces = 0

    while abs(respuesta**2 - numero_objetivo ) >= epsilon and respuesta <= numero_objetivo:
        respuesta += paso
        veces += 1
        print(respuesta)

    if abs(respuesta ** 2 - numero_objetivo) >= epsilon:
        print('NO se encontro la raiz')
    else: 
        print('La raiz aproximada es {} y se encontro en {}'.format(respuesta, veces)) 

