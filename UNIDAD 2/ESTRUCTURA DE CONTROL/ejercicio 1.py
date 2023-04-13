def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def saludo():
    print("Hola Melanie")
def formateo(nombre,apellido):
    print(nombre,apellido)
bandera=True
while bandera:
    print("Menu de opciones")
    print("Presione 1 para sumar")
    print("Presione 2 para restar")
    print("Presione 3 para multiplicar")
    print("Presione 4 para dividir")
    print("Presione 5 para saludar")
    print("Presione 6 para formatear")
    print("Presione 7 para salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion != 7:
        num1=int(input("ingrese el valor 1: "))
        num2=int(input("ingrese el valor 2: "))
        if opcion == 1:
            print("La suma es: ",suma(num1,num2))
        elif opcion == 2:
            print("La resta es: ",resta(num1,num2))
        elif opcion == 3:
            print("La multiplicacion es: ",multiplicacion(num1,num2))
        elif opcion == 4:
            print("La division es: ",division(num1,num2))
        elif opcion == 5:
            saludo()
        else:
            formateo("Melanie","Torres")
    else:
        bandera=False
        print("Fin del ciclo")
print("Nueva linea")

