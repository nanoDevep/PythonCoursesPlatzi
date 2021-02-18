# importamos el modulo unittest para poder hacer pruebas de debugging
import unittest


def suma(num_1, num_2):
    resultado =  num_1 + num_2
    return resultado


class CajaNegraPruebas(unittest.TestCase):

    def test_sumaDosNumeros(self):
        num_1  = 0
        num_2 = 15

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15)
    
    
    def test_sumarNumeros(self):
        num_1  = 0
        num_2 = -15

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -15)


if __name__ == '__main__':
    unittest.main()