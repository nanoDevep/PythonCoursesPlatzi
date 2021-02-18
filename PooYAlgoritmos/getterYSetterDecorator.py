class Avion:

    def __init__(self, marca):
        self._marca = marca

    @property
    def marca(self):
        print('Dentro del metodo GETmarca')
        return self._marca 
    
    @marca.setter
    def marca(self, marca):
        print('Dentro del metodo SETmarca')
        self._marca = marca

    # marca  = property(obtener_marca, asignar_marca)

if __name__ == '__main__':
    
    airbus = Avion('Airbus')
    
    airbus.marca = 'adios'

    boeing = Avion('Boing')

    # boeing.obtener_marca = 'avianca'
    print(airbus.marca)

# class Millas:
# 	def __init__(self):
# 		self._distancia = 0

# 	# Función para obtener el valor de _distancia
# 	# Usando el decorador property
# 	@property
# 	def obtener_distancia(self):
# 		print("Llamada al método getter")
# 		return self._distancia

# 	# Función para definir el valor de _distancia
# 	@obtener_distancia.setter
# 	def definir_distancia(self, valor):
# 		if valor < 0:
# 			raise ValueError("No es posible convertir distancias menores a 0.")
# 		print("Llamada al método setter")
# 		self._distancia = valor

# # Creamos un nuevo objeto 
# avion = Millas()

# # Indicamos la distancia
# avion.distancias = 200

# # Obtenemos su atributo distancia
# print(avion.distancias)