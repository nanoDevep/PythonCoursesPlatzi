class Avion:

    def __init__(self, marca):
        self._marca = marca

    def obtener_marca(self):
        print('Dentro del metodo GETmarca')
        return self._marca 
    

    def asignar_marca(self, marca):
        print('Dentro del metodo SETmarca')
        self._marca = marca

    marca  = property(obtener_marca, asignar_marca)

if __name__ == '__main__':
    
    airbus = Avion('Airbus')
    
    print(airbus.marca)

    boeing = Avion('Boing')

    print(boeing.marca)