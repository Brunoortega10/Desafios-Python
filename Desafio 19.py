import random

n1 = str(input("Primeiro aluno: "))
n2 = str(input("segundo aluno: "))
n3 = str(input("terceiro aluno: "))
n4 = str(input("quarto aluno: "))

x = [n1,n2,n3,n4]

sorteado = random.choice(x)

print("O aluno sorteado foi: {}".format(sorteado))