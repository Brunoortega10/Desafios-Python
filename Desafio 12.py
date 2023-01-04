preco = int(input("Qual é o preço do produto? R$ "))

desc = preco * 5 / 100

print ("O produto que custava R$ {:.2f}, na promoção de 5% está saindo por {:.2f}".format(preco, (preco-desc)))

