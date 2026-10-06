num1 = float(input("Dame un numero "))
num2 = float(input("Dame un segundo numero "))
num3 = float(input("Dame un tercer numero "))

def cal_media(numero1, numero2, numero3):

    return (numero1 + numero2 + numero3) / 3

print("La media es " + str(cal_media(num1, num2, num3)))