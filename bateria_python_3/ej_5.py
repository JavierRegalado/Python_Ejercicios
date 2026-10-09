caracter = input("Ingrese un caracter: ")
while caracter != " ":
    if caracter.lower() in "aeiou":
        print(f"{caracter} es una vocal.")
    else:
        print(f"{caracter} no es una vocal.")
    caracter = input("Ingrese un caracter vacio para acabar: ")

