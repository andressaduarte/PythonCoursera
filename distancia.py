import math

x1 = int(input("Coordenada x1: "))
y1 = int(input("Coordenada y1: "))
x2 = int(input("Coordenada x2: "))
y2 = int(input("Coordenada y2: "))


if math.sqrt(((x1-x2)**2)+((y1-y2)**2)) >= 10:
    print("longe")
else:
    print("perto")