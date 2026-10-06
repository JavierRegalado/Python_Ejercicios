d = float(input("Ingrese la distancia entre los dos vehículos (km): "))
v1 = float(input("Ingrese la velocidad del vehículo que va detrás / más rápido (km/h): "))
v2 = float(input("Ingrese la velocidad del vehículo que va adelante / más lento (km/h): "))

tiempo_minutos = (d / (v1 - v2)) * 60

print(f"El vehículo más rápido alcanzará al otro en {tiempo_minutos:.2f} minutos.")