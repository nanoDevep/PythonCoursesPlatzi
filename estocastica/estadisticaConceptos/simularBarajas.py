import random
import collections

PALOS = ('ESPADA', 'DIAMANTE', 'TREBOL', 'CORAZONES')
VALORES = ('as','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey')

def crear_barajas():
    barajas = []

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas


def obtener_mano(barajas, tamano_mano):
    return random.sample(barajas, tamano_mano)

def corrida(manos, intentos):
    cantidad = 0
    last = 0

    corridas = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        
        counter = sorted({int(i) for i in valores if i.isdigit()})
         

        for valor in counter:
            if last == 0:
                last = valor
            else:
                if valor == last + 1:
                    last = valor
                    cantidad += 1

                    if cantidad == 4:
                        corridas += 1
                        break
                elif valor != last + 1:
                    last = valor
                    cantidad = 0
    
    return corridas / intentos
            

def main(intentos, tamano_mano):
    barajas = crear_barajas()
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
        
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break
    
    probabilidad_par = pares / intentos
    print(f'la probabilidad de obtener un par en una mano de {tamano_mano} es {probabilidad_par*100}%')
    # print(f'la probabilidad de obtener una corrida en una mano de {tamano_mano} es {corrida(manos, intentos)*100}%')

    
        

if __name__ == '__main__':
    intentos = int(input('Nº de intentos: '))
    tamano_mano = int(input('tamano manos: '))

    main(intentos, tamano_mano)

        