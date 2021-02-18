
class Campo:


    def __init__(self):
        self.coordenadas_de_borracho = {}


    def agregar_borracho(self, borracho, coordenada):
        self.coordenadas_de_borracho[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borracho[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        
        self.coordenadas_de_borracho[borracho] = nueva_coordenada


    def obtener_borracho(self, borracho):
        try:
            return self.coordenadas_de_borracho[borracho]
        except KeyError:
            print('No esta este borrachin por favor añadelo')