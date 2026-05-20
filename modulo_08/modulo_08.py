class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Carro: {self.marca} {self.modelo}")

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"Carro Elétrico: {self.marca} {self.modelo} | Autonomia: {self.autonomia_bateria}km")

    def __str__(self):
        return f"{self.marca} {self.modelo} (Elétrico) - Bateria: {self.autonomia_bateria}km"


class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"


class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.catalogo = []

    def adicionar_livro(self, livro: Livro):
        self.catalogo.append(livro)

    def listar_livros(self):
        for livro in self.catalogo:
            print(livro)

    def emprestar_livro(self, titulo_livro: str):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo_livro.lower() and livro.disponivel:
                livro.disponivel = False
                return True
        return False

    def devolver_livro(self, titulo_livro: str):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo_livro.lower() and not livro.disponivel:
                livro.disponivel = True
                return True
        return False


if __name__ == "__main__":
    # Teste Carros
    c = Carro("Toyota", "Corolla")