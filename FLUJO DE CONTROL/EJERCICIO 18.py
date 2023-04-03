print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 02/04/2023\n")
frase = input("Introduce una frase: ")

frase = frase.replace(" ", "").lower()

if frase == frase[::-1]:
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")