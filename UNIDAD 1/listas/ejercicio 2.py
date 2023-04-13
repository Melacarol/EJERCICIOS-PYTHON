print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 09/04/2023\n")
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
numeros=[]
numeros=[1,2,3,4,5]
print(numeros)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
amigos=["Estefania","Jennifer","Nayeli","Evelyn"]
print(amigos[0])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
lista=[1,2,3,4,5,6,7,8,9,10]
for e in lista:
    if e % 2==0:
        print(e)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
amigos=["Estefania","Jennifer","Nayeli","Evelyn"]
print(amigos[-1])
#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista[-1])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
lista=[1,2,3,4,5,6,7,8,9,10]
for e in lista:
    if e % 7 and not e % 2 == 0:
        print(e)
#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
amigos=["Estefania","Jennifer","Nayeli","Evelyn"]
amigos.insert(2,"Melanie")
print(amigos)
#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista[-1],lista[0])
#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
amigos=["Estefania","Jennifer","Nayeli","Evelyn"]
print(len(amigos))
#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
lista=[1,2,3,4,5,6,7,8,9,10]
print(sum(lista))