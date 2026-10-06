num = int(input("Ingrese un número de dos dígitos: "))


def invertir_numero(numero: int) -> int:

    decenas = numero // 10
    
    unidades = numero % 10
    
    numero_invertido = (unidades * 10) + decenas
    
    return numero_invertido

print(f"El número invertido es: {invertir_numero(num)}")