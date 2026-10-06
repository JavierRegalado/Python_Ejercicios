base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
    print(f"El resultado de la potencia es: {resultado}")

elif exponente == 0:
    resultado = 1
    print("El resultado es: 1")

else:  # Exponente negativo
    resultado = 1 / (base ** abs(exponente))
    print(f"El resultado es: {resultado}")