import time


num = int(input("Digite um numero: "))
ant = num - 1
suc = num + 1


print("Analisando o valor informado...")
time.sleep(2)
print("O valor informado tem como antecessor o numero {} e como sucessor, o nomero {}".format(ant,suc))