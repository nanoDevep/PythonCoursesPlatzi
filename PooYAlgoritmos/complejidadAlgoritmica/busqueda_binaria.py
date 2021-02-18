from busqueda_lineal import busqueda_lineal as bl
import random


def binary_search(lista, objetivo, final, comienzo):
    i = 0

    if comienzo > final:
        final, comienzo = comienzo, final
    final -= 1
    mitad = (final + comienzo) // 2

    while comienzo <= final:
        i += 1

        if lista[mitad] == objetivo:
            print('numero de iteraciones: ' , i,' encontrado en la posicion', mitad)
            return True

        elif lista[mitad] > objetivo:
            final = mitad - 1
        else:
            comienzo = mitad + 1

        mitad = (final + comienzo) // 2

    print('numero de iteraciones: ' , i)
    return False



if __name__ == '__main__':
    n = int(input('n: '))
    lista = sorted([random.randint(0,100) for i in range(n)])
    objetivo = int(input('objetivo: '))

    a = bl(lista, objetivo)
    b = binary_search(lista, objetivo, len(lista), 0)
    print(b)