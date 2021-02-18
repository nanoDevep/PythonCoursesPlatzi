def busqueda_binaria():

    objetivo = int(input('Ingresa un numero que desees conocer su raiz: '))

    try:
        epsilon = float(input('''Cual es el margen de error? 
    Ingresa Control + C si quieres asignar el por defecto que es 0.01
    :'''))

    except KeyboardInterrupt:
        epsilon = 0.01

    maximo = max(1.0, objetivo)
    bajo = 0
    respuesta = (bajo + maximo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            maximo = respuesta
        
        respuesta = (bajo + maximo) / 2

    print('la raiz aproximada de {} es {}'.format(objetivo, respuesta))
