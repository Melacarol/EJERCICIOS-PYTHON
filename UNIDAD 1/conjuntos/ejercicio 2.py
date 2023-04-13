print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 10/04/2023\n")
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
a=set()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.add(9)
a.add(10)
print("conjunto de numeros del 1 al 10: ",a)
#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ellos.
pares = set()
for i in range(2, 11, 2):
    pares.add(i)
impares = set()
for i in range(1, 11, 2):
    impares.add(i)

print("Conjunto de números pares del 1 al 10:", pares)
print("Conjunto de números impares del 1 al 10:", impares)

interseccion = pares.intersection(impares)
print("Intersección entre los conjuntos:", interseccion)
#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas={"manzana","banana","naranja"}
elemento=input("Ingresar un elemento: ")
if elemento in frutas:
    print("El elemento se encuentra en el conjunto")
else:
    print("El elemento no se encuentra en el conjunto")
#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
num1={1,2,3,4,5}
num2={4,5,6,7,8}
union_conjuntos=num1.union(num2)
print("La union de los dos conjuntos es: ",union_conjuntos)
#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.
elementos={"leche","pan","huevos","azucar"}
print("El conjunto es: ",elementos)
elementos.discard("azucar")
print("El conjunto eliminado un elemento: ",elementos)
elementos.add("harina")
print("El conjunto agregado un elemento: ",elementos)
#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.
nombres={"Juan","Maria","Pedro","Luisa"}
print("El numero de elemntos es: ",len(nombres))
#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.
num1={1,2,3,4,5}
num2={4,5,6,7,8}
print("El conjunto 1 es: ",num1)
print("El conjunto 2 es: ",num2)
diferencia_simetrica=num1.symmetric_difference(num2) 
print("La diferencia simetrica es: ",diferencia_simetrica)
#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.
conjunto1={1,2,3,4,5,6,7,8,9,10}
conjunto2={5,6,7,8,9,10,11,12,13,14,15}
print("El conjunto 1 es: ",conjunto1)
print("El conjunto 2 es: ",conjunto2)
union=conjunto1.union(conjunto2)
print("La union de los conjuntos es: ",union)
#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.
frutas1={"manzana","banana","naranja","pera"}
print("Elementos ordenados alfabeticamente: ",sorted(frutas1))
#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.
x={1,2,3,4,5,6,7,8,9,10}
b={6,7,8,9,10,11,12,13,14,15}
print("El primer conjunto es: ",x)
print("El segundo conjunto es: ",b)
print("La interseccion de los dos conjuntos es: ",x.intersection(b))