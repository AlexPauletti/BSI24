salarioL = []
filhosL = []
pobreL = []

censo = int(input("A pesquisa da prefeitura foi de quantas pessoas? "))

#contando o censo
if censo <= 1:
    print("para de palhaçada")

else:
    for a in range(0, censo, 1):
        salario = float(input("Informe seu salário: "))
        salarioL.append(salario)

        filhos = int(input("Informe a quantidade de filhos que você tem: "))
        filhosL.append(filhos)

    #media basica dos dois valores
    mediaSalario = sum(salarioL)/censo
    mediaFilhos = sum(filhosL)/censo

    #definindo o maior salário
    maior = 2
    for b in salarioL:
        if b > maior:
            maior = b

    #em busca da porcentagem
    for c in salarioL:
        if c <= 1500:
            pobreL.append(c)

    quantPobre = len(pobreL)
    porcemPobre = (quantPobre/censo)*100

    print(f"A prefeitura fez uma pesquisa com {censo} pessoas. \n\n A média salarial é {mediaSalario}. \n A média de filhos é {mediaFilhos}. \n O maior salário é R${maior}. \n {porcemPobre}% dos participantes recebem até R$1500,00.")

