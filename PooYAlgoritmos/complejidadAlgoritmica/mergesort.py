import random
from bubbleSort import bubble_sort
# import math

def mergeSort(lista, i):
    
    length = len(lista)

    if length > 1:
        
        izquierda = lista[:length//2]
        derecha = lista[length//2:]
        #  i += 1
        
        # print(izquierda, '*'*5 , derecha)

        _, i = mergeSort(izquierda, i)
        _, i = mergeSort(derecha, i )

        iz = 0
        d = 0

        o = 0

        while iz < len(izquierda) and d < len(derecha):

            if izquierda[iz] <= derecha[d]:
                lista[o] =  izquierda[iz]
                iz += 1
            else:
                lista[o] = derecha[d]
                d += 1
            
            o += 1
            i += 1


        while iz < len(izquierda):
            lista[o] = izquierda[iz]
            iz += 1
            o += 1
            i += 1

        while d < len(derecha):
            lista[o] = derecha[d]
            d += 1
            o += 1
            i += 1

        # print(f'izquieda {izquierda}  derecha {derecha}')
        # print(lista)
        # print('-'*15)        
        
    return lista, i

        




if __name__ == '__main__':

    lista = [random.randint(0, 100) for i in range(int(input(': ')))]
    # print(lista)

    a, i = mergeSort(lista, 0)    

    print(f'merge sort recorridos: {i}')
    # bubble_sort(lista)