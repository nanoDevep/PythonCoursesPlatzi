
class Personaje:

    def __init__(self, nombre, vida):
        self.nombre =  nombre
        self.vida =  vida

    def presentarse(self):
        print('Hola mi nombre es {} y tengo {} puntos de vida! Ahora podes matarme!'.format(self.nombre, self.vida))



class Enemigo(Personaje):

    def __init__(self, nombre, vida, dano):
        super().__init__(nombre, vida) 
        self._dano = dano

    
    def recibir_dano(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            return True
        
        return False
    
    def infligir_dano(self, Personaje):
        Personaje.vida -= self._dano
            

class Heroe(Personaje):

    def __init__(self, nombre, vida, dano, habilidad):
        super().__init__(nombre, vida)
        self._dano = dano
        self._habilidad = habilidad

    def presentarse(self):
        super().presentarse()
        print('Mi habilidad es: {}'.format(self._habilidad))

    
if __name__ == '__main__':

    print('Interfaz de personajes, Heroes y Enemigos \n')
    print(' + '*30)
    print('')
    
    PabloElMalo = Enemigo('Pablo', 100, 20)

    JoseElHeroe = Heroe('Jose', 70, 28, 'Daño Doble')

    PabloElMalo.presentarse()
    JoseElHeroe.presentarse()



    