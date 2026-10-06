n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
    if n2 >= n3:
        medio, menor = n2, n3
    else:
        medio, menor = n3, n2
elif n2 >= n1 and n2 >= n3:
    mayor = n2
    if n1 >= n3:
        medio, menor = n1, n3
    else:
        medio, menor = n3, n1
else:
    mayor = n3
    if n1 >= n2:
        medio, menor = n1, n2
    else:
        medio, menor = n2, n1

print(f"Mayor a menor: {mayor}, {medio}, {menor}")