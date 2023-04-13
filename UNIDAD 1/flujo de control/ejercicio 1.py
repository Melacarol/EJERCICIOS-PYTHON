print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 30/03/2023\n")
x=input("ingresar el estado del semaforo: ")
if x=='verde':
    print("cruzar la calle")
elif x=='amarillo':
    print("no cruzar la calle")
elif x=='rojo':
    print("no cruzar la calle")
else:
    print(f"el color {x} no hay en el semaforo")