class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def __str__(self):
        return f"{self.marca} {self.modelo} (Elétrico) - Bateria: {self.autonomia_bateria}km"


# --- Teste do Exercício 3 ---
if __name__ == "__main__":
    carro1 = Carro("Honda", "Civic")
    carro2 = CarroEletrico("Tesla", "Model 3", 491)
    
    # O print chama automaticamente o método __str__
    print(carro1)
    print(carro2)