import unittest

# Classe a ser testada
class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        return a / b

# Classe de teste
class TestCalculadora(unittest.TestCase):
    def test_operacao_soma(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(10, 5), 15)

    def test_operacao_divisao(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(10, 2), 5)

if __name__ == "__main__":
    unittest.main()