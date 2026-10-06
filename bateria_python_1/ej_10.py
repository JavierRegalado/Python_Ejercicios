p1 = float(input("La nota del primer parcial "))
p2 = float(input("La nota del segundo parcial "))
p3 = float(input("La nota del tercer parcial "))
examen_final = float(input("La nota del examen final "))
trabajo_final = float(input("La nota del trabajo final "))

mediaParcial = (p1+p2+p3) / 3

##calcular porcentajes
porcentaje_media = mediaParcial * 0.55
porcentaje_examen = examen_final * 0.3
porcentaje_trabajo_final = trabajo_final * 0.15

#calificacion final

calificacion_final = porcentaje_media + porcentaje_examen + porcentaje_trabajo_final

print(f"Tu nota final es {calificacion_final}")
