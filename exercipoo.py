class alunos:
    def __init__(self,nome,anoNacsimento,cpf,matricula):
        self.nome=nome
        self.anoNascimento=anoNacsimento
        self.cpf=cpf
        self.matricula=matricula

    def mostrar_dados(self):
        print ('DADOS')
        print(f'''nome: {self.nome}\n 
        ano de nascimento: {self.anoNascimento}\n 
        idade: {2022-self.anoNascimento}
        CPF: {self.cpf}\n
        Matrícula: {self.matricula}''')
    
aluno1=alunos('Abinoã Menezes de Paula',2002,70493109480, 202467)
aluno1.mostrar_dados()
        