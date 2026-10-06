correctas = int(input("Ingrese el número de respuestas correctas: "))
incorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
en_blanco = int(input("Ingrese el número de respuestas en blanco: "))

puntaje_final = (correctas * 5) + (incorrectas * -1) + (en_blanco * 0)

print(f"El puntaje final obtenido es: {puntaje_final} puntos.")