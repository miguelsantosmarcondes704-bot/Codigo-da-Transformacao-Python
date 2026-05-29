import unittest

class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

class TestCalculadoraExcecoes(unittest.TestCase):
    def test_divisao_por_zero_deve_lancar_excecao(self):
        calc = Calculadora()
        
        # Verifica se o erro ValueError é disparado corretamente
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()