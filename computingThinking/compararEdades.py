import os
def comparando():
    nombre1 = input('¿Cual es tu nombre?')
    nombre2 = input('¿Cual es tu nombre?')


    edad1 = input(f'Cual es la edad de {nombre1}? ')
    edad2 = input(f'Cual es la edad de {nombre2}? ')

    os.system('cls')
    if edad1 > edad2:
        print(f'{nombre1} es mayor que {nombre2}')
    elif edad2 > edad1:
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print(f'{nombre1} y {nombre2} tienen la misma edad que es {edad1}')

