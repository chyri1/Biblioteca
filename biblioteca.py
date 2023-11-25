from datetime import date
from usuario import Usuario
from livro import Livro
from emprestimo import Emprestimo

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_emprestimos_ativos(self):
        emprestimos_ativos = [emprestimo for usuario in self.usuarios for emprestimo in usuario.emprestimos]
        return emprestimos_ativos

    def listar_livros_mais_emprestados(self, n):
        livros_mais_emprestados = sorted(self.livros, key=lambda livro: len(livro.emprestimos), reverse=True)
        return livros_mais_emprestados[:n]

    def listar_usuarios_inadimplentes(self):
        data_hoje = date.today()
        usuarios_inadimplentes = [usuario for usuario in self.usuarios if any(emprestimo.data_devolucao < data_hoje for emprestimo in usuario.emprestimos)]
        return usuarios_inadimplentes
