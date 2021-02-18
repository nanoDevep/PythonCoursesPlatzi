import random

# Crearemos una clase padre borracho muy basica de la cual todos las clases borrachos o sea 
# los tipos de borrachos heredaran

# Cosas como Nombre, y eso xd.


class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre

# Creamos otra abstraccion del borracho 
class BorrachoPacifico(Borracho):

    # instanciamos el borracho
    def __init__(self, nombre):
        super().__init__(nombre)

    #como solo puede moverse de arriba hacia abajo por eso escojemos una de estas 4 opciones
    def camina(self):
        return random.choice(((0,1) , (1,0), (-1,0), (0, -1)))



