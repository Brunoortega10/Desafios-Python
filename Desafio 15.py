km = float(input("Digite quantos KMs foram percorridos com o carro: "))
dias = float(input("Digite quantos dias o carro foi alugado: "))
tot = (km * 0.15) + (dias * 60)

print ("O valor total do aluguel de carro foi: R$ {}".format(tot))