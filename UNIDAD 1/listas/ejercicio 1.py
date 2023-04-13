print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 09/04/2023\n")
#1. Crear una lista de numeros del 1 al 5
lista=[1,2,3,4,5]
print(lista)
#2. Accede al elemto 3 de la lista:
print(lista[3])
#3. Modifica un elemento de la lista:
lista[3]=100
print(lista)
#4. Agrega el elemento 9 al final de la lista
lista.append(9)
print(lista)
#5. Eliminar el elemento 2 de la lista:
lista.remove(2)
print(lista)
#6. Recorrer una lista con un bucle for:
for e in lista:
    print(e)
#7. Ordenar una lista:
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
#8. Obtener la longitud de una lista:
print(len(lista))
#9. Comprobar si un elemento está en la lista:
a=int(input("ingresar un numero: "))
if a in lista:
    print("El numero se encuentra en la lista")
else:
    print("El numero no se encuentra en la lista")
    