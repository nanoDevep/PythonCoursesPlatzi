import random
import math
from varianza_and_dst import desviacionEst, media
from bokeh.plotting import figure, output_file, show

def lanzar_dardos(numero_de_agujas, x_points, y_points, colors):
    agujas_en_circulo = 0

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([1, -1])
        y = random.random() * random.choice([1, -1])

        x_points.append(x)
        y_points.append(y)
        distancia_a_centro = math.sqrt(x**2 + y**2)

        if distancia_a_centro <= 1:
            agujas_en_circulo += 1
            colors.append('#fcba03')
        else:
            colors.append('#0044ff')
        
    
    return (4*agujas_en_circulo) / numero_de_agujas

def  simular(numero_de_agujas, numero_de_intentos, x, y, colors):

    resultados = []

    for _ in range(numero_de_intentos):
        resultado = lanzar_dardos(numero_de_agujas, x, y, colors)
        resultados.append(resultado)
    
    mean = media(resultados)
    dst = desviacionEst(resultados)

    print(f'la media es {mean} con una varacion {dst}')
    return mean, dst

def medir(precision, numero_de_intentos, numero_de_agujas):
    sigma = precision

    while sigma >= precision / 1.96:
        x = []
        y = []
        colors = []
        mean, sigma = simular(numero_de_agujas, numero_de_intentos, x, y, colors)
        numero_de_agujas *= 2
    
    print(len(x), len(y), numero_de_agujas)
    graficar(x, y, colors)

    return mean

def graficar(x, y, colors):
    output_file('hola.html')

    figura = figure(title='Medicion de pi', x_axis_label='x', y_axis_label='y')

    figura.circle(x, y, fill_color=colors)

    show(figura)


if __name__ == '__main__':
    medir(0.1, 1, 10000)

    
