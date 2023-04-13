print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 31/03/2023\n")
letra = input("Ingrese una letra: ")

if len(letra) != 1:
    print("No se puede procesar el dato. Debe ingresar una sola letra.")
elif letra in "aeiouAEIOU":
    print("Es vocal")
else:
    print("No es vocal")