dia = int(input("Informe o dia da data desejada: "))
mes = int(input("Informe o mês da data: "))
ano = int(input("Informe o ano da data: "))

dias = int(input("Informe quantos dias deseja adicionar à data: "))

# lista, o primeiro dígito é referido como 0
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# função, parâmetro é ano, checando se o ano é divisível por 4 pra ver se é bissexto
def bissexto(ano):
    if ano%4 == 0:
        True
    else:
        False

if bissexto(ano) == True:
        dias_mes[1] = 29

# enquanto os dias somados existirem
while dias > 0:

    if bissexto(ano) == True:
        dias_mes[1] = 29
    else:
        dias_mes[1] = 28

    # += faz ele somar e já deixar adicionado à variável
    dia += 1

    # mes-1 pq a lista começa em zero
    if dias > int(dias_mes[mes-1]):
        mes += 1
        if mes > 12:
            ano += 1
            mes = 1
        dia = 1
    
    dia -= 1


print(f"A data virou: {dia}/{mes}/{ano}")