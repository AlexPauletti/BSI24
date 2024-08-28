media = float(input("Informe a média do aluno: "))
freq = float(input("Informe a frequência do aluno: "))

if freq >= 75 and media >= 7.0:
    print("Aluno aprovado")

else:
    if freq >= 75 and media >= 3.0 and media < 7.0:
        print("Aluno em exame")

    else:
        print("Aluno reprovado")    
