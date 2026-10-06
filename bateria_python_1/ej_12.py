print("\nIntroduce el Punto 1:")
x1 = float(input("Ingresa x1: "))
y1 = float(input("Ingresa y1: "))

print("\nIntroduce el Punto 2:")
x2 = float(input("Ingresa x2: "))
y2 = float(input("Ingresa y2: "))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"\nLa distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia:.4f}")