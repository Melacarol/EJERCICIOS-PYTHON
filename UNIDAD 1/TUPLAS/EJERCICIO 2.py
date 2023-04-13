print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 09/04/2023\n")
#Crear una tupla de números enteros y calcular su suma y promedio.
numeros=(1,2,3,4,5)
suma=0
for e in numeros:
    suma+=e
promedio=suma/len(numeros)
print("La suma es: ",suma)
print("El promedio es: ",promedio)
#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
a=(2,4,6,8,10)
b=(2,4,6,8,10)
c=tuple(map(sum,zip(a,b)))
print("La suma de las tuplas es: ",c)
#Crear una tupla de nombres y ordenarla alfabéticamente.
nombres=("Paula","Carolina","Karla","Ana")
print("Nombres ordenados alfabeticamente: ",sorted(nombres))
#Crear una tupla de números y encontrar el valor mínimo y máximo.
numeros=(32,3,4,8,10,24,50)
print("El valor minimos es: ",min(numeros))
print("El valor maximo es: ",max(numeros))
#Crear una tupla de números y convertirla en una lista.
tupla=(6,5,3,7,8,3,2)
print("Tupla convertida en lista: ",list(tupla))
#Crear una tupla con los días de la semana y mostrar el tercer elemento.
dias=("Lunes","Martes","Miercoles","Juves","Viernes")
print("El tercer elemento es: ",dias[2])
#Crear una tupla con números enteros y mostrar aquellos que son pares.
numeros_enteros=(1,2,3,4,5,6,7,8,9,10)
for e in numeros_enteros:
    if e % 2 == 0:
        print("Numeros pares: ",e)
#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Nomviembre","Diciembre")
for mes in meses:
    if len(mes) > 5:
        print("El mes que tiene mas de 5 letras es: ",mes)
#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
edad=(15,17,18,18,20,22,23,14,11)
for e in edad:
    if e > 18:
        print("La cantidad de personas mayores a 18 es: ",e)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
libros=(("Las almas muertas","Nicolai Gogol"),
        ("Drácula","Bram Stroker"),
        ("La divina comedia","Dante Alighieri"))

print("El titulo del tercer libro es: ",libros[2][0])


