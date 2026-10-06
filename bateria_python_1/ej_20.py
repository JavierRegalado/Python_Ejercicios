m2 = int(input("Monedas de 2€: "))
m1 = int(input("Monedas de 1€: "))
m50 = int(input("Monedas de 50 céntimos: "))
m20 = int(input("Monedas de 20 céntimos: "))
m10 = int(input("Monedas de 10 céntimos: "))

total_centimos = (m2 * 200) + (m1 * 100) + (m50 * 50) + (m20 * 20) + (m10 * 10)

euros = total_centimos // 100
centimos = total_centimos % 100

print(f"\nTienes {euros} euros y {centimos} céntimos.")