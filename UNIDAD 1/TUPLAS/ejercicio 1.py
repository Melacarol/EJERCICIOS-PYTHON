print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 09/04/2023\n")
#Crear una tupla vacía:
x=()
print("La nueva tupla es: ",x)
#Crear una tupla con algunos elementos:
a=("azul","verde","morado")
print("Elementos de la tupla: ",a)
#Acceder a un elemento de la tupla:
print("Acceder a un elemento: ",a[2])
#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):
print("No se puede modificar un elemnto de la tupla")
#Concatenar dos tuplas:
num1=(2,4,6,8)
num2=(1,3,5,7)
num3=num1+num2
print("Concatar dos tuplas: ",num3)
#Obtener la longitud de una tupla:
print("La longitud de la tupla es: ",len(a))
#Convertir una tupla en una lista:
tupla=(1,2,3,4,5)
print("Convertido en lista: ",list(tupla))
#Convertir una lista en una tupla:
lista=(6,7,8,9,10)
print("Convertido en tupla: ",tuple(lista))