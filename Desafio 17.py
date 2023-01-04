catOpost = float(input("Digite o cateto oposto: "))
catAdja = float(input("Digite o cateto adjacente: "))

hip = ((catOpost**2)+(catAdja**2))**(1/2)

print ("A hipotenusa é: {:.2f}".format(hip))