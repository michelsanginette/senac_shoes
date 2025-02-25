# Pessoa, Professor, Aluno

# Criando a SuperClass Pessoa
class Pessoa:

    def __init__(self, nome,idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def exibir_dados(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Cpf: {self.cpf}'
    
# Criando a Subclass Aluno
class Aluno(Pessoa):

    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf) # Herda atributos da classe Pessoa.
        self.matricula = matricula
        self.notas = [] # Lista para armazenar notas do aluno.

    def adicionar_notas(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def exibir_dados(self):
        return f'{super().exibir_dados()} | Matrícula: {self.matricula}'
    
class Professor(Pessoa):

    # disciplina, salário -> atributos
    # exibir_dados -> Pessoa, + a disciplina e o salario.

    def __init__(self, nome, idade, cpf, disciplina, salario):
        super().__init__(nome, idade, cpf) # Herda atributos da classe Pessoa.
        self.disciplina = disciplina
        self.salario = salario

    def exibir_dados(self):
        return f'{super().exibir_dados()} | Disciplina: {self.disciplina} | Salário: R${self.salario:.2f}'
    
# Criando um aluno
aluno1 = Aluno("Maria Souza", 16, "123456", "2025001")


# Criando um professor
professor1 = Professor("Carlos Mendes", 48, "654321", "Matemática", 50000)


# Exibindo as informações
print(aluno1.exibir_dados())
print(professor1.exibir_dados())