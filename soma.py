print("Digite uma sequência de valores e finalize com um 0")
soma = 0
valor = 1
while valor != 0:
    valor = int(input("Digite um valor:"))
    soma = soma + valor
print("A soma dos valores é igual a", soma)