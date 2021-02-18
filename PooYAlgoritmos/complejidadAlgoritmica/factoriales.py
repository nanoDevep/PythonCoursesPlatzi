import time
import sys
print('recursion Limit: ', sys.getrecursionlimit())

def factorial_b(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 200
    while True:
        try:
            a = time.time()
            factorial_r(n)
            b = time.time()
            print('time taken:' , b - a )

            n += 100
        except Exception:
            recursionLimit = sys.getrecursionlimit() + 110
            print(recursionLimit)
            sys.setrecursionlimit(recursionLimit)
            


    # n = 10000

    # comienzo = time.time()
    # factorial_r(n)
    # print(f'recursion: {final - comienzo}')
    # final = time.time()

    # begin = time.time()
    # factorial_b(n)
    # end = time.time()
    # print(f'bucles: {end - begin}')

    
    # # print('si')
