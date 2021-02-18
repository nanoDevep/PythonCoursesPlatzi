import math


class Algorithms:

    def __init__(self):
        pass

    
    def logarithm(self, n):
        return math.log10(n)
    
    def lineal(self, n):
        return n

    def n_logarithm(self, n):
        return n * math.log10(n)

    def constante(self, n):
        return 1

    def square(self, n):
        return n ** 2
    
    def exponential(self, n):
        return 2 ** n


if __name__ == '__main__':

    algoritmo = Algorithms()
    steps = [1, 10 , 100, 1000, 100000]

    for i in steps:
        print(algoritmo.constante(i))
        print(algoritmo.logarithm(i))
        print(algoritmo.lineal(i))
        print(algoritmo.n_logarithm(i))
        print(algoritmo.square(i))
        print(algoritmo.exponential(i))
        print('')


