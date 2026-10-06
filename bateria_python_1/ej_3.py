c1 = float(input("Dame la medida de un cateto "))
c2 = float(input("Dame la medida del otro cateto "))

def calcular_hipotenusa(cateto1, cateto2):
    return (cateto1**2 + cateto2**2) ** 0.5

h = calcular_hipotenusa(c1, c2)

print("La hipotenusa es " + str(h))