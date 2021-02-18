import random

def busqueda_lineal(lista, objetivo):
    match = False
    i = 0
    for i in lista:
        i += 1
        if objetivo == i:
            match = True
            break
    
    print('Numero de iteraciones en busqueda lineal: ', i)
    return match



if __name__ == '__main__':
    n = int(input('list length: '))

    lista = [random.randint(0, 100) for i in range(n)]

    objetivo = int(input('Num to search: '))
    print(lista)
    founded = busqueda_lineal(lista, objetivo)

    print(f'el numero {objetivo} {"esta" if founded else "no esta"} en la lista')