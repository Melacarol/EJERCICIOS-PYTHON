print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 31/03/2023\n")
valor_1=int(input("ingresar valor 1: "))
valor_2=int(input("ingresar valor 2: "))

operacion=0
print("Presione 1 para sumar")
print("Presione 2 para restar")
print("Presione 3 para multiplicar")

opción= input("Que opción desea:")
if opción=="1":
    operacion=valor_1 + valor_2
    print("La suma de los valores es", operacion)
elif opción=="2":
    operacion=valor_1 - valor_2
    print("La resta de los valores es", operacion )
elif opción=="3":
    operacion=valor_1 * valor_2
    print("La multiplicación es", operacion)
else:
    print("No es correcta la opcion")