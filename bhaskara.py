import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b ** 2 - 4 * (a * c)

if delta == 0:
    print("a raiz desta equação é", (-b + math.sqrt(delta)) / (2 * a))
elif delta < 0:
    print("esta equação não possui raízes reais")
else:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    if r1 <= r2:
        print("as raízes da equação são", r1, "e", r2)
    else:
        print("as raízes da equação são", r2, "e", r1)
