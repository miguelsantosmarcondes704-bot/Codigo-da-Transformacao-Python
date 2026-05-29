class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo}")


# --- Teste do Exercício 1 ---
if __name__ == "__main__":
    meu_carro = Carro("Toyota", "Corolla")
    meu_carro.exibir_info()