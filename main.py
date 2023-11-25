from datetime import date, timedelta
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

def menu_principal(biblioteca):
    while True:
        print("\n** Biblioteca Municipal - Sistema de Gerenciamento **")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Listar Empréstimos Ativos")
        print("6. Listar Livros Mais Emprestados")
        print("7. Listar Usuários Inadimplentes")
        print("8. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_livro(biblioteca)
        elif escolha == "2":
            cadastrar_usuario(biblioteca)
        elif escolha == "3":
            realizar_emprestimo(biblioteca)
        elif escolha == "4":
            realizar_devolucao(biblioteca)
        elif escolha == "5":
            listar_emprestimos_ativos(biblioteca)
        elif escolha == "6":
            listar_livros_mais_emprestados(biblioteca)
        elif escolha == "7":
            listar_usuarios_inadimplentes(biblioteca)
        elif escolha == "8":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_livro(biblioteca):
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    editora = input("Editora do livro: ")
    ano_publicacao = input("Ano de publicação do livro: ")
    quantidade_copias = int(input("Quantidade de cópias disponíveis: "))

    livro = Livro(titulo, autor, editora, ano_publicacao, quantidade_copias)
    biblioteca.cadastrar_livro(livro)
    print(f"Livro '{titulo}' cadastrado com sucesso.")

def cadastrar_usuario(biblioteca):
    nome = input("Nome do usuário: ")
    endereco = input("Endereço do usuário: ")
    telefone = input("Telefone do usuário: ")

    usuario = Usuario(nome, endereco, telefone)
    biblioteca.cadastrar_usuario(usuario)
    print(f"Usuário '{nome}' cadastrado com sucesso.")

def realizar_emprestimo(biblioteca):
    nome_usuario = input("Nome do usuário: ")
    titulo_livro = input("Título do livro: ")

    usuario = next((u for u in biblioteca.usuarios if u.nome == nome_usuario), None)
    livro = next((l for l in biblioteca.livros if l.titulo == titulo_livro), None)

    if usuario and livro:
        emprestimo = usuario.fazer_emprestimo(livro)
        if emprestimo:
            print(f"Empréstimo realizado com sucesso. Data de devolução: {emprestimo.data_devolucao}")
        else:
            print("Não foi possível realizar o empréstimo. Livro não disponível.")
    else:
        print("Usuário ou livro não encontrado.")

def realizar_devolucao(biblioteca):
    nome_usuario = input("Nome do usuário: ")
    titulo_livro = input("Título do livro: ")

    usuario = next((u for u in biblioteca.usuarios if u.nome == nome_usuario), None)
    livro = next((l for l in biblioteca.livros if l.titulo == titulo_livro), None)

    if usuario and livro:
        emprestimo = next((e for e in usuario.emprestimos if e.livro == livro), None)
        if emprestimo:
            usuario.fazer_devolucao(emprestimo)
            livro.devolver(emprestimo)
            print("Devolução realizada com sucesso.")
        else:
            print("Não foi possível encontrar o empréstimo correspondente.")
    else:
        print("Usuário ou livro não encontrado.")

def listar_emprestimos_ativos(biblioteca):
    emprestimos_ativos = biblioteca.listar_emprestimos_ativos()
    if emprestimos_ativos:
        print("\nEmpréstimos Ativos:")
        for emprestimo in emprestimos_ativos:
            print(f"Usuário: {emprestimo.usuario.nome}, Livro: {emprestimo.livro.titulo}, Data de Devolução: {emprestimo.data_devolucao}")
    else:
        print("Não há empréstimos ativos.")

def listar_livros_mais_emprestados(biblioteca):
    n = int(input("Quantos livros deseja listar? "))
    livros_mais_emprestados = biblioteca.listar_livros_mais_emprestados(n)
    if livros_mais_emprestados:
        print("\nLivros Mais Emprestados:")
        for livro in livros_mais_emprestados:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Empréstimos: {len(livro.emprestimos)}")
    else:
        print("Ainda não há livros emprestados.")

def listar_usuarios_inadimplentes(biblioteca):
    usuarios_inadimplentes = biblioteca.listar_usuarios_inadimplentes()
    if usuarios_inadimplentes:
        print("\nUsuários Inadimplentes:")
        for usuario in usuarios_inadimplentes:
            print(f"Nome: {usuario.nome}, Telefone: {usuario.telefone}")
    else:
        print("Não há usuários inadimplentes.")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    menu_principal(biblioteca)
