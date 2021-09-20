import math
  

class Mais_velha:

    def maior_idade(self):
        print("Dados da primeira pessoa")
        nome1 = input("Nome: ")
        idade1 = int(input("Idade: "))
        print("Dados da segunda pessoa")
        nome2 = input("Nome: ")
        idade2 = int(input("Idade: "))

        if idade1 > idade2:
            print(f"Pessoa mais velha {nome1}")
        else:
            print(f"Pessoa mais velha {nome2}")


class Salario:
    
    def salario_medio(self):
        print("Dados do primeiro funcionário")
        nome1 = input("Nome: ")
        salario1 = int(input("Salario: "))
        print("Dados do segundo funcionário")
        nome2 = input("Nome: ")
        salario2 = int(input("Salario"))

        media = (salario1+salario2)/2
        
        print(f'Salário médio {media}')
    

class Retangulo:
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcula_area(self):
        area = self.largura * self.altura / 2
        print(f'AREA: {area}')
    
    def calcula_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        print(f'PERIMETRO: {perimetro}')
        
    def calcula_diagonal(self):
        diagonal = math.sqrt((self.altura * self.altura) + (self.largura * self.largura))
        print(f'DIAGONAL: {diagonal}')


class Funcionario:
    def __init__(self, nome, salario, imposto):
        self.nome = nome
        self.salario = salario
        self.imposto = imposto
        
    def salario_liquido(self):
        salario_liquido = self.salario - self.imposto
        print(f'Funcionário {self.nome}, R${salario_liquido}')
        return salario_liquido
    
    def aumentar_salario(self,porcentagem):
        self.salario = self.salario + (((self.salario * porcentagem) / 100))
        print(f'Dados Atualizados {self.funcionario}, R${self.salario}')

class Aluno:
    
    def notas_aluno(self):
        nome = input("Nome Do Aluno")        
        print(f'Nome Do Aluno {nome}')
        
        print("Digite as três notas do Aluno: ")
        nota1 = int(input())
        if nota1 > 30 :
            nota1 = int(input("nota invalida, digite novamente: "))
            
        nota2 = int(input())
        if nota2 > 35 :
            nota2 = int(input("nota invalida, digite novamente: "))
            
        nota3 = int(input())
        if nota3 > 35 :
            nota3 = int(input("nota invalida, digite novamente: "))
        
        
        media = (nota1+nota2+nota3)/3
        
        if media < 60:
            print(f'Nota final {media}')
            print('Reprovado')
            falta = 60 - media
            print(f'Faltaram {falta} pontos')
        else:
            print(f'Nota final {media}')
            print('Aprovado')


class Menu:
    def menu(self):
        print("Digite o número da questão(de 1 a 5) ou 0 para sair: ")
        numero = int(input())
        l = True
        while l:
            if numero == 1:
                questao = Mais_velha()
                questao.maior_idade()
                l = False
            if numero == 2:
                questao = Salario()
                questao.salario_medio()
                l = False
            if numero == 3:
                largura = int(input("Digite a largura do triangulo"))
                altura = int(input("Digite a altura do triangulo"))
                questao = Retangulo(largura, altura)

                questao.calcula_area()
                questao.calcula_diagonal()
                questao.calcula_perimetro()
                l = False
            if numero == 4 :
                nome = int(input("Nome: "))
                salario = int(input("Salario: "))
                imposto = int(input("Imposto: "))

                questao = Funcionario(nome,salario,imposto)
                questao.salario_liquido()
                porcentagem = int(input("Digite a porcentagem para aumentar o sálario"))
                questao.aumentar_salario(porcentagem)
            if numero == 5 :
                questao = Aluno()
                questao.notas_aluno()
            if numero == 0:
                l = False
            if numero > 5:
                print("Opção incorreta")
            l = False
                
                
start = Menu()
start.menu()