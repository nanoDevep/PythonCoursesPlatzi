

class Persona():

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.seCepillo = False

    # Este es el metodo privado
    def __seCepilloLosDientes(self, seCepillo):
        self.seCepillo = seCepillo


    def cepillarse(self):
        self.__seCepilloLosDientes(True)


    def saludarPersona(self, mensaje, otraPersona):
    
        if self.seCepillo:
            print(mensaje, otraPersona.nombre)
        else:
            print('Recuerda cepillarte los dientes! 💚')    


if __name__ == '__main__':

    juan = Persona('Juan', 19, 'H')
    andrea = Persona('Andrea', 21, 'M')
    

    juan.saludarPersona('Hola', andrea)
    juan.cepillarse()
    juan.saludarPersona('Ahora si, Hola', andrea)

    

