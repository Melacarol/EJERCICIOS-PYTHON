print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 10/04/2023\n")
#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla de números enteros y calcular su suma y promedio.
numeros=(2,3,4,5,6,7,8,9)
suma=0
for e in numeros:
    suma += e
promedio=suma/len(numeros)
print("la suma es " , suma)
print("su promedio seria " , promedio)
#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
num1=(1,2,3,4,5)
num2=(1,2,3,4,5)
suma_tuplas = tuple(map(sum, zip(num1, num2)))
print("La suma de los elementos ",suma_tuplas)
#Crear una tupla de nombres y ordenarla alfabéticamente.
tupla=("maria","carolina","karla","paula")
print("El orden alfabeticamente es: ",sorted(tupla))
#Crear una tupla de números y encontrar el valor mínimo y máximo.
numeros3=[2,3,4,5,6,7,8,9,45,2,4]

print("Valor maximo es: ",max(numeros3))
print("Valor minimo es: ",min(numeros3))
#Crear una tupla de números y convertirla en una lista.
tupla=(1,2,3,4,5,67,8,9)
print("Convertida en lista : ",list(tupla))
#Crear una tupla con los días de la semana y mostrar el tercer elemento.
semana=("lunes","martes","miercoles","jueves","viernes")
print("el tercer elemento", semana[2])
#Crear una tupla con números enteros y mostrar aquellos que son pares.
numeros=(1,2,3,4,5)
for e in numeros:
    if e % 2 == 0: 
       print("numeros pares: ", e)
#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
for mes in meses:
    if len(mes) > 5:
       print("tiene mas de 5 letras es: ",mes)
#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
numeros=(15,34,56,7,8,98,45,23)
for e in numeros:
    if e > 18 :
        print("mayores de edad ", e)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
libros=(("La divina comedia","Dante Alighieri", ),
        ("La comedia humana", "Honoré de Balzac"),
        ("Drácula","Bram Stroker"))

print("Titulo del tercer libro : ", libros[2][0])