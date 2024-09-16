#AUTOR: Alexis Uriarte
#CALCULADORA

#Creación de funciones
def cabecera():
    print("="*22)
    print("|     CALCULADORA    |")
    print("="*22)
    print()
    print("[S] = Suma")
    print("[R] = Resta")
    print("[M] = Multiplicación")
    print("[D] = División")
    print()
    global opcion
    opcion = input("Elija una opción:")
    print()
    return opcion

#función suma
def suma(n1,n2):
    suma = n1 + n2
    return suma

#función resta
def resta(n1,n2):
    resta = n1 - n2
    return resta

#función multiplicación
def multiplicacion(n1,n2):
    mult = n1 * n2
    return mult

#función división
def division(n1,n2):
    if(n1 > 0) and (n2 > 0):
        division = n1 / n2
        return division
    else:
        return ("No es divisible por cero")

#Proceso
continuar = "SI"

while continuar == "SI":
    cabecera()
    #Entrada
    n1=int(input("Digita el primer número:"))
    n2=int(input("Digita el segundo número:"))
    #Ejecución
    if opcion == "S":
        print("La suma es:", suma(n1,n2))
    elif opcion == "R":
        print("La resta es:", resta(n1,n2))
    elif opcion == "M":
        print("La multiplicación es:", multiplicacion(n1,n2))
    elif opcion == "D":
        print("La división es:", division(n1,n2))
    else:
        print("Opcion inválida")
    print()
    continuar = input("¿Desea continuar? SI/NO:")

