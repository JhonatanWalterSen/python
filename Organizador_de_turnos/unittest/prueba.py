import unittest
import cambia_texto
class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "Buen día goldita"
        resultado = cambia_texto.todo_mayusuclas(palabra)
        self.assertEqual(resultado, 'BUEN DÍA GOLDITA')

if __name__ == '__main__':
    unittest.main()