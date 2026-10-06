hh = int(input("Hora de salida (HH, 0-23): "))
mm = int(input("Minutos de salida (MM, 0-59): "))
ss = int(input("Segundos de salida (SS, 0-59): "))
t = int(input("Tiempo de viaje en segundos (T): "))

segundos_iniciales = hh * 3600 + mm * 60 + ss

segundos_totales = segundos_iniciales + t

segundos_del_dia = segundos_totales % 86400


hora_llegada = segundos_del_dia // 3600
minuto_llegada = (segundos_del_dia % 3600) // 60
segundo_llegada = segundos_del_dia % 60

print(f"Hora de llegada: {hora_llegada:02d}:{minuto_llegada:02d}:{segundo_llegada:02d}")