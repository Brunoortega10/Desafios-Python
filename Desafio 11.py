larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))

a = larg*alt
tinta = a/8

print ("Sua parece de {}X{} tem uma área de {}M².".format(larg, alt, a))
print ("Para pintar essa parede será necessário {:.2f}L de tinta.".format(tinta))