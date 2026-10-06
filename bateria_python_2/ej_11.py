a = float(input("Ingrese el lado A: "))
b = float(input("Ingrese el lado B: "))
c = float(input("Ingrese el lado C: "))

lados = sorted([a, b, c])
cat1, cat2, hip = lados[0], lados[1], lados[2]

if cat1 + cat2 <= hip or a <= 0 or b <= 0 or c <= 0:
    print("Error: Las dimensiones ingresadas no forman un triángulo válido.")
else:
    es_rectangulo = round(cat1**2 + cat2**2, 5) == round(hip**2, 5)

    if a == b == c:
        print("El triángulo es Equilátero.")
    elif es_rectangulo:
        if cat1 == cat2:
            print("El triángulo es Rectángulo e Isósceles.")
        else:
            print("El triángulo es Rectángulo.")
    elif a == b or b == c or a == c:
        print("El triángulo es Isósceles.")
    else:
        print("El triángulo es Escaleno.")