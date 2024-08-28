ano_nasc = int(input("Informe o ano em que nasceu: "))

idade = 2024 - ano_nasc

if idade >= 18:
    print("Você já tem idade para votar e tirar sua carteira de habilitação")

else:
    if idade >= 16:
        print("Você já tem idade para votar")
        