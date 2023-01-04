sal = float(input("Qual é o salário do funcionario? R$ "))
aum = (sal * 15)/100

print("Um funcionário que ganha R$ {:.2f}, receberá R$ {:.2f} após o aumento de 15%.".format(sal, (sal+aum)))

