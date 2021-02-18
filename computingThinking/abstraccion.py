import aproximacion
import busquedaBinaria
import compararEdades
import enumeracion
import os 

class Abstrayendo:

    def __init__(self):
        print('¡Hemos entrado al mundo de la abstracción!')

    def aproximacionPrecisa(self):
        aproximacion.aproximacionTodasCombinaciones()

    def busquedaBinaria(self):
        busquedaBinaria.busqueda_binaria()

    def compararEdades(self):
        compararEdades.comparando()

    def aproximacionMenosPrecisa(self):
        enumeracion.enumeracionMenosPrecisa()



if __name__ == '__main__':
    
    abstraedor = Abstrayendo()

    while True:
        menuOptions = input('''Bienvenidos a tu abstraedor personal
        
        En el siguiente menú puedes escoger uno de los siguientes platillos:
        
        [1]Aproximacion mas precisa pero honestamente muy inefectiva en rendimiento
        [2]Aproximacion por busqueda binara muchísimo más efectiva
        [3]Compara Edades de 2 personas 
        [4]Aproximacion menos precisa pero un poco mas rapida que la 1
        [5] Con este salimos del bucle! 

        Por favor escoge el numero que corresponde a la opcion: ''')

        if menuOptions == '1':
            abstraedor.aproximacionPrecisa()
        elif menuOptions == '2':
            abstraedor.busquedaBinaria()
        elif menuOptions == '3':
            abstraedor.compararEdades()
        elif menuOptions == '4':
            abstraedor.aproximacionMenosPrecisa()
        elif menuOptions == '5':
            break
        else:
            print('Por favor escoge una opcion disponible!')
            continue
        
        os.system('cls')

    
    