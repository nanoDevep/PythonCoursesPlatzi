import random

def insertion(lista):

    # for i in range(len(lista)):

    #     for j in range(len(lista)- 1):
    #         if lista[i-j] < lista[j]:
    #             lista[i] , lista[j] = lista[j] , lista[i]
    
    # return lista

    for i in range(0, len(lista)):
    
        for j in range(0, len(lista)-1):
            if lista[i]  < lista[j] and i != j: # si ponen mayor que, se ordenan de manera descendente
                # y si se pone < se ordenan ascendente
                print(f"i: {i} j:{j}")
                lista[i] , lista[j] = lista[j], lista[i]



if __name__ == '__main__':
    lista = [random.randint(0,100) for i in range(20)]

    insertion(lista)

    print(lista)