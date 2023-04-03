print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 31/03/2023\n")
numero = input("Ingrese un numero: ")

if len(numero) != 1:
    print(f"No se puede procesar el {numero}. Debe ingresar un solo numero.")
elif numero in "1,2,3,4,5,6,7,8,9":
    print(f"{numero} pertenece a la secuencia")
else:
    print(f"{numero} no pertenece a la secuencia")