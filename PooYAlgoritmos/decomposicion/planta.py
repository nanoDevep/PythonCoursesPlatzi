import time
import timeit


class Planta:


    def __init__(self, tipo, scientistName, medicinalUse, Tamano, clima):
        self.tipo = tipo
        self.scientistName = scientistName
        
        if medicinalUse:
            self.medicinalUse = MedicinalProperties()
        else:
            self.medicinalUse = None
    
        
        self._tallo = Tallo(Tamano) 
        self._clima = clima
        self._cuotaAgua = 0
        self._vidaPuntos = 10

    def show_medicinalUse(self):

        if self.medicinalUse:
            self.medicinalUse.showProperties()
        

    def makePhotosinthesis(self):
        self._tomarAgua()
        self._tallo.buscarNutrientes()


    def _tomarAgua(self):
        self._cuotaAgua += 1

    def describeStatus(self):
        print('tamano: ' , self.get_tamano())
        print('cuotaAgua: ' , self.get_cuotaAgua())
        print('Clima: ' , self.get_clima())


    def get_tamano(self):
        return self._tallo.tamano

    def get_clima(self):
        return self._clima

    def get_cuotaAgua(self):
        return self._cuotaAgua
    
    def secarse(self):
        self._cuotaAgua -= 1
        self.marchitarse()


    def marchitarse(self):
        if self._cuotaAgua < 0:
            self.morir()
    

    def morir(self):
        print('He muerto')


    

class MedicinalProperties:

    def __init__(self):
        
        pair_of_properties = {
            '1': 'Antiinflamatorio',
            '2': 'Antinauseas',
            '3': 'Antiespamosdicos',
            '4': 'Antigripal', 
            '5': 'Relajante',
            '6': 'Previene enfermedades mentales'
        }

        a = input(''' 
        ¿Cuales son sus propiedades medicinales?
        _____________________________________________
        Si tiene mas de uno por favor separelos por comas
        
        [1]: Antiinflamatorio
        [2]: Antinauseas
        [3]: Antiespamosdicos
        [4]: Antigripal
        [5]: Relajante
        [6]: Previene enfermedades mentales
        
        [7] Agregar propiedades no incluidas

        ''')

        self.properties = []

        if len(a) > 1:

            for i in a.split(','):
                if i == '7':
                    self.properties.append(input(': '))
                else:
                
                   if int(i) < 7 and int(i) > 0:
                    self.properties.append(pair_of_properties[i])            


    def showProperties(self):
        print('My plant has this properties')
        print('--'*12)

        for i in self.properties:
            print(i)


class Tallo:

    def __init__(self, tamano):

        # Crear hojas
        self.tamano = tamano
        self.hojas = []

        for _ in range(tamano // 15):
            self.hojas.append(Hoja(5))
    

    def buscarNutrientes(self):
        
        for i in self.hojas:
            i.absorberLuz()
        
        self.crecer()

        print('Esperar! ')
        
        time.sleep(5)

    def crecer(self):
        if self.tamano < 5:
            self.tamano += 1

        




class Hoja:


    def __init__(self, longitud):
        self.cuotaDiaria = 0

        self.tamano = longitud 


    def absorberLuz(self):
        self.cuotaDiaria += 1


    def pararDeAbsorberLuz(self):
        self.cuotaDiaria = 0


if __name__ == '__main__':
    Cannabis = Planta('Medicinal', 'Cannabis', True, 150, 'templado')
    

    while True:
        Cannabis.describeStatus()
        Cannabis.makePhotosinthesis()
        Cannabis.show_medicinalUse()
        Cannabis.marchitarse()
        Cannabis.medicinalUse.showProperties()

        if input('Escribe s  para salir: ') == 's':
            break
