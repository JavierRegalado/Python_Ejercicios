f = float(input("Dame los grados en fahrenheit "))

def conversion(fahrenheit):

    return (f -32) * 5/9

print( str(f) + " grados fahrenheit son " + str(conversion(f)) + " grados celsius")