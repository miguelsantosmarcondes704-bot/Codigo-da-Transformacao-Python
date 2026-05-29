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
        print(f"\n--- Catálogo da Biblioteca {self.nome} ---")
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


# --- Teste do Desafio Extra ---
if __name__ == "__main__":
    # Criando a biblioteca e os livros
    minha_biblioteca = Biblioteca("Central")
    livro1 = Livro("O Alquimista", "Paulo Coelho")
    livro2 = Livro("1984", "George Orwell")
    
    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)
    
    # Mostrando estado inicial
    minha_biblioteca.listar_livros()
    
    # Simulando empréstimo
    print("\n> Emprestando '1984'...")
    minha_biblioteca.emprestar_livro("1984")
    
    # Mostrando estado atualizado
    minha_biblioteca.listar_livros()