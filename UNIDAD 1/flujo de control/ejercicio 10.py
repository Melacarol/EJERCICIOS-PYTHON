print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 02/04/2023\n")
año = int(input("Introduce un año: "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")