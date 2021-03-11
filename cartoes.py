meuCartao = int(input("Digite o número do seu cartão: "))

cartaoLido = 1
encontreiMeuCartao = False

while cartaoLido != 0 and not encontreiMeuCartao:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartao = True
    meuCartao = cartaoLido # tentativa de fazer com que o código encontre qualquer cartão inserido no input e não só o primeiro
if encontreiMeuCartao:
    print("Seu cartão está na lista!")
else:
    print("Seu cartão não está na lista...")