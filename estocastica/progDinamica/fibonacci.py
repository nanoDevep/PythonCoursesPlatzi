import sys

sys.setrecursionlimit(10000)    

def fibonnaci(n):
    if n <= 1:
        return 1
    
    return fibonnaci(n-1) + fibonnaci(n-2)

def fibonnaci_dinamico(n, memo):
    if n <= 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonnaci_dinamico(n-1, memo) + fibonnaci_dinamico(n-2, memo)
        memo[n] = resultado
        return resultado

if __name__ == '__main__':
    n = int(input('Numero: '))
    memo = {}

    resultado = fibonnaci_dinamico(n, memo)    
    # print(memo)
    print(resultado)
