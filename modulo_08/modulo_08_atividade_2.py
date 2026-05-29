class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo}")


# Herança aplicada aqui
class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"Carro Elétrico: {self.marca} {self.modelo} | Autonomia: {self.autonomia_bateria}km")


# --- Teste do Exercício 2 ---
if __name__ == "__main__":
    carro_ev = CarroEletrico("BYD", "Seal", 520)
    carro_ev.exibir_info()