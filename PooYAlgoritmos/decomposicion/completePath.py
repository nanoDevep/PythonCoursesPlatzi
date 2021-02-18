import timeit

def completePath(string, maxLength):

    if len(string) == maxLength - 1:
        string += 'OK'
    else:
        string += '-'

    return string




past = timeit.timeit()
texto = ''

while True:

    cur = timeit.timeit()

    while input(': ') != '0':
        past = cur 
        texto = completePath(texto, 10)
        print(texto)
    
    if len(texto) >= 10:
        break