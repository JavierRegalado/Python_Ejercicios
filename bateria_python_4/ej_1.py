import random

# Dimensions of the table
FILAS = 10
COLUMNAS = 10

# Borde horizontal divisor (+----+----+...)
borde_horizontal = "+" + "+".join(["----"] * COLUMNAS) + "+"

# Generación e impresión de la tabla
for _ in range(FILAS):
    print(borde_horizontal)
    
    # Generar números aleatorios entre 1 y 99
    numeros = [random.randint(1, 99) for _ in range(COLUMNAS)]
    
    # Formatear números a 2 dígitos con relleno de cero y centrarlos en un ancho de 4 caracteres
    celdas = [f"{num:02d}".center(4) for num in numeros]
    
    # Unir las celdas con bordes verticales (| 74 | 43 | ...)
    print("|" + "|".join(celdas) + "|")

# Borde inferior final
print(borde_horizontal)