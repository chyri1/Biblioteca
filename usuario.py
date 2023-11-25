from datetime import date, timedelta

class Usuario:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.emprestimos = []

    def fazer_emprestimo(self, livro):
        emprestimo = livro.emprestar(self)
        if emprestimo:
            self.emprestimos.append(emprestimo)
            return emprestimo
        else:
            return None

    def fazer_devolucao(self, emprestimo):
        emprestimo.data_devolucao = date.today()
        self.emprestimos.remove(emprestimo)
