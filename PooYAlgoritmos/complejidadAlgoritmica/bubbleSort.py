import random


def bubble_sort(lista):


    final = len(lista)
    counter = 0
    begin = 1
    print('tamaño de lista ', final)
    counter2 = 0

    while counter2 < len(lista):
        
        while begin < final:
            # print(lista[begin], end=' ')
            if lista[begin] < lista[begin-1]:
                lista[begin-1], lista[begin] = lista[begin], lista[begin-1]

            begin += 1 
            counter += 1
        
        final -= 1
        # print('')
        begin = 1
        counter2 += 1
    
    print('recorridos ', counter)

    print(f'porcentaje: {(counter / len(lista)) * 100}% ')
    




def ordenamiento_de_burbuja(lista):
    n = len(lista)
    counter = 0
    for i in range(n):
        counter += 1
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)
            counter += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(counter)
    return lista


if __name__ == '__main__':

    lista = [random.randint(0,100) for i in range(int(input(': ')))]

    hola = ordenamiento_de_burbuja(lista.copy())
    print(lista)
    bubble_sort(lista)
