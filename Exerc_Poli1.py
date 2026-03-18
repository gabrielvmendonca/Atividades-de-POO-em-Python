from abc import ABC, abstractmethod

class Midia(ABC):
    @abstractmethod
    def exibir_info(self):
        pass

class Livro(Midia):
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def exibir_info(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Páginas: {self.numero_paginas}"

class Filmes(Midia):
    def __init__(self, titulo, diretor, duracao):
        self.titulo = titulo
        self.diretor = diretor
        self.duracao = duracao
    
    def exibir_info(self):
        return f"Filme: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao}min"

class Musica(Midia):
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
    
    def exibir_info(self):
        return f"Música: {self.titulo}, Artista: {self.artista}, Segundos: {self.duracao}"

def main():
    # Criando uma lista de mídias (Polimorfismo em ação!)
    biblioteca = [
        Livro("A Bíblia", "Adonai", 1185),
        Filmes("O protetor", "Antoine Fuqua", 132),
        Musica("Sobre as Águas", "Rapha Gonçalves feat Isaias Saad", 458)
    ]

    print("--- MINHA BIBLIOTECA ---")
    for item in biblioteca:
        # Aqui o print funciona porque o método retorna a string
        print(item.exibir_info())

if __name__ == "__main__":
    main()