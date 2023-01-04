import math     

ang = float(input("Digite um angulo: "))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print("O valor do seno é: {:.2f}".format(sen))
print("O valor do Cosseno é: {:.2f}".format(cos))
print("O valor da tangente é: {:.2f}".format(tang))

