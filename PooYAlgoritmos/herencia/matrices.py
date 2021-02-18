

class Matrices:


    def __init__(self, lista):
        self.lista = tuple(lista)

    def __add__(self, matriz):
        return Matrices([i + m for i, m in zip(self.lista, matriz.lista)])
   
    

if __name__ == '__main__':
    primera = Matrices([1,2,3])
    segunda = Matrices([2,3,4])
    tercera = Matrices([1,1,1])


    a = primera + segunda + tercera
    print(a.lista)

