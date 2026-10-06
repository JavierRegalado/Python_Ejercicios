num1 = float(input("Dame un numero "))
num2 = float(input("Dame un segundo numero "))

def suma(numero1, numero2):

    return numero1 + numero2

def resta(numero1, numero2):

    return numero1 - numero2

def multiplicacion(numero1, numero2):

    return numero1 * numero2

def division(numero1, numero2):

    return numero1 / numero2

print("La suma es " + str(suma(num1, num2)))
print("La resta es " + str(resta(num1, num2)))
print("La multiplicacion es " + str(multiplicacion(num1, num2)))
print("La division es " + str(division(num1,num2)))