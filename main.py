class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f'O aluno {self.nome} está presente!'

class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} esta ministrando uma aula sobre {assunto}')

class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos if alunos is not None else []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        presenca_str = f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n"
        for aluno in self.alunos:
            presenca_str += aluno.presenca() + "\n"
        return presenca_str

# Demonstração
professor = Professor("Paulo")
aluno1 = Aluno("Lucas")
aluno2 = Aluno("Pedro")
aluno3 = Aluno("Maria")

aula = Aula(professor, "Artes")

aula.adicionar_aluno(aluno1)

aula.adicionar_aluno(aluno2)

aula.adicionar_aluno(aluno3)
print(aula.listar_presenca())
