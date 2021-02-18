try:
    import sys
except ImportError as e:
    print('Error de importacion' + e)

sys.path.append(r'C:\Users\Alcum\Onedrive\documents\pythonPro\estocastica')

from borracho import BorrachoPacifico
from coordenada import Coordenada
from campo import Campo
from bokeh.plotting import figure, show 

def graficar(points, pasos):
    # figura = figure(title='Camino de Borracho con ' + str(pasos) + ' pasos', x_axis_label='pasos', y_axis_label='distancia')

    # a , b = [points[i][0] for i in range(len(points))], [points[i][1] for i in range(len(points))]

    # figura.line(a, b , legend='distancia media')
    # print('Si!')
    # show(figura)
    print('Me llamaron' , pasos)
    pass

def caminata(campo, borracho, pasos):
    puntos = []
    inicio = campo.obtener_borracho(borracho)
    puntos.append((inicio.x, inicio.y))   
    print('Pasos son ', pasos)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
        pos_boracho = campo.obtener_borracho(borracho)

        puntos.append((pos_boracho.x, pos_boracho.y))   

    graficar(puntos, pasos)
    
    return inicio.distancia(campo.obtener_borracho(borracho))


def simular_caminata(pasos, numero_intentos, tipo_borracho):
    mi_borracho = tipo_borracho(nombre='David')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.agregar_borracho(mi_borracho, origen)
        simulacion_caminata = caminata(campo, mi_borracho, pasos)
        distancias.append(simulacion_caminata)
    
    return distancias

def main(distancia_caminata, numero_intentos, tipo_borracho):

    for pasos in distancia_caminata:

        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)

        distancia_media = round(sum(distancias) / len(distancias), 4)
        
        distancia_maxima = round(max(distancias), 2)
        
        distancia_minima = round(min(distancias), 2)

        print(f'la distancia promedio fue {distancia_media} la maxima fue {distancia_maxima} y la minima fue {distancia_minima}' )



if __name__ == '__main__':
    distancia_caminata = [10, 100, 1000, 10000]
    
    numero_intentos = 1 

    main(distancia_caminata, numero_intentos, BorrachoPacifico)