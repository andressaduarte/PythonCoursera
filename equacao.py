import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b ** 2 - 4 * (a * c)

if delta < 0:
  print("Essa equação não possui raízes reais.")
elif delta == 0:
    print("A raíz da equação é", (-b + math.sqrt(delta)) / (2 * a))
else:
    print("As raízes da equação são:", (-b + math.sqrt(delta)) / (2 * a), "e", (-b + math.sqrt(delta)) / (2 * a))
