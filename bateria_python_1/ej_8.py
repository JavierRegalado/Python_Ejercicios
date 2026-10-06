sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese el monto de la venta 1: "))
venta2 = float(input("Ingrese el monto de la venta 2: "))
venta3 = float(input("Ingrese el monto de la venta 3: "))

total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.10
total_mes = sueldo_base + comision

print("\n--- Desglose de Pagos ---")
print(f"Ganancia por comisiones (10%): ${comision:.2f}")
print(f"Total a recibir en el mes: ${total_mes:.2f}")