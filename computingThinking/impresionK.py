def run():
    maximo = int( input('De que tamaño quiere la K: ') )

    i = maximo


    counter = 0

    while i > 0:
        impresion = '*' * i 
        print(impresion + ' ' * counter + impresion)
        i -= 1
        counter += 2
    
    counter -= 2
    i = 1

    while i < maximo + 1:
        impresion = '*' * i 
        print(impresion + ' ' * counter + impresion)
        i += 1
        counter -= 2
    


if __name__ == "__main__":
    run()