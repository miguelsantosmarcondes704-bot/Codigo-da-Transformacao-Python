import unittest

def soma(a, b):
    return a + b

class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

class TestFuncaoSoma(unittest.TestCase):
    def test_soma_numeros_positivos(self):
        self.assertEqual(soma(2, 3), 5)

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)
        self.assertEqual(self.calc.somar(-1, 1), 0)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()