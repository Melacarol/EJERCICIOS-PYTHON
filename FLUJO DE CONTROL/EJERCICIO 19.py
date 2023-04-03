print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 30/03/2023\n")
nombre=input("igresar su nombre: ")
edad=int(input("ingresar su edad "))
if edad>=18:
    print(nombre, "es mayor de edad")
elif edad<18:
    print(nombre, "es menor de edad")