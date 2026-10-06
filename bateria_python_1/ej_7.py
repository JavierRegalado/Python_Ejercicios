minutos_totales = int(input("Ingresa la cantidad de minutos: "))

horas = minutos_totales // 60
minutos = minutos_totales % 60

print(f"{minutos_totales} minutos equivalen a {horas} hora(s) y {minutos} minuto(s).")