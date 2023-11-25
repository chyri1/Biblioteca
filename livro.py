from datetime import date, timedelta
from emprestimo import Emprestimo 

class Livro:
    def __init__(self, titulo, autor, editora, ano_publicacao, quantidade_copias):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.quantidade_copias = quantidade_copias
        self.emprestimos = []

    def emprestar(self, usuario):
        if self.quantidade_copias > 0:
            self.quantidade_copias -= 1
            data_emprestimo = date.today()
            data_devolucao = date.today() + timedelta(days=14)  # Exemplo: 14 dias de empréstimo
            emprestimo = Emprestimo(usuario, self, data_emprestimo, data_devolucao)
            self.emprestimos.append(emprestimo)
            return emprestimo
        else:
            return None

    def devolver(self, emprestimo):
        if emprestimo in self.emprestimos:
            self.quantidade_copias += 1
            self.emprestimos.remove(emprestimo)
