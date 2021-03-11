dec = True
anterior = int(input("Digite o primeiro valor da sequência: "))
valor = 1
while valor != 0 and dec:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        dec = False
    anterior = valor

if dec:
    print("A sequência é decrescente :)")
else:
    print("A sequência não é decrescente :(")