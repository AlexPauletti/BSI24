#adquirindo os valores iniciais
deposito = (0)
deposito = float(input("Informe a quantidade depositada: "))
cheque1 = float(input("Informe o valor do primeiro cheque efetuado: "))
cheque2 = float(input("Informe o valor do segundo cheque efetuado: "))

#cálculo da retirada com imposto
cpmf = (0.38/100)
saldo = (deposito - cheque1 - cheque2 - ((cheque1+cheque2)*cpmf))

print(f"Seu saldo atual é: {saldo}")