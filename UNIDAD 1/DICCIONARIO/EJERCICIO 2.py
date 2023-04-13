print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 09/04/2023\n")
#1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: "clave": valor
alumnos={}
#2.Dado el siguiente diccionario:
personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}
#a) Imprime la edad de Juan.
print("La edad de Juan es",personas["Juan"])
#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
personas["Luis"]="18"
print("Elemento agregado al diccionario",personas)
#c) Elimina el elemento con la clave "Pedro".
personas.pop("Pedro")
print("Elemento eliminado del diccionario",personas)
#3.Dado el siguiente diccionario:
ventas = {"manzanas": 10, "naranjas": 5, "peras": 8}
#a) Imprime la cantidad de manzanas vendidas.
print("La cantidad de manzanas vendidas es: ",ventas["manzanas"])
#b) Agrega 3 elementos más al diccionario: "limones": 12, "sandías": 3, "melones": 5.
ventas["limones"]="12"
ventas["sandias"]="3"
ventas["melones"]="5"
print("Elementos agregados al diccionario",ventas)
#c) Imprime las claves del diccionario.
print("Las claves del diccionario son: ",ventas.keys())
#4. Dado el siguiente diccionario:
alumnos = {"Juan": {"edad": 22, "promedio": 8.5}, "María": {"edad": 20, "promedio": 9.0}, "Pedro": {"edad": 25, "promedio": 7.5}}
#a) Imprime la edad de Juan.
print("La edad de Juan es: ",alumnos["Juan"]["edad"])
#b) Imprime el promedio de María.
print("El promedio de Maria es: ",alumnos["María"]["promedio"])
#c) Agrega un nuevo elemento al diccionario con la clave "Ana" y los valores "edad": 19 y "promedio": 8.0.
alumnos["Ana"]={"edad":19,"promedio":8.0}
print("Elemento agregado al diccionario",alumnos)
alumnos.items()
for c,v in alumnos.items():
    if v["edad"]>= 20 and  v["edad"]<= 22:
        print(c)
#5. Dado el siguiente diccionario:
empleados = {"Juan": {"departamento": "Ventas", "sueldo": 1500}, "María": {"departamento": "Contabilidad", "sueldo": 1800}, "Pedro": {"departamento": "Ventas", "sueldo": 1700}, "Ana": {"departamento": "Recursos Humanos", "sueldo": 1900}}
#a) Imprime el sueldo de Pedro.
print("El sueldo de Pedro es: ",empleados["Pedro"]["sueldo"])
#b) Cambia el sueldo de Ana a 2000.
empleados["Ana"]["sueldo"]=2000
print("El nuevo sueldo de ana es: ",empleados)
#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.
empelados_ventas={"Juan": {"departamento": "Ventas", "sueldo": 1500},"Pedro": {"departamento": "Ventas", "sueldo": 1700}}
print("Empleados del departamento de ventas: ",empelados_ventas)
#6.Dado el siguiente diccionario:
cursos = {
    "Pedro": ["Matemáticas", "Biología", "Historia"],
    "María": ["Física", "Química", "Literatura"]
}
#a) Imprime las materias en las que está inscrito Pedro.
print("Las materias que esta incrito Pedro son: ",cursos["Pedro"])
#b) Agrega una materia más a la lista de materias de María: "Programación".
cursos["Maria"]="Programacion"
print("Materia agregada a la lista de Maria",cursos)
#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
biologia = {}

for estudiante, cursos in cursos.items():
    if "Biología" in cursos:
        biologia[estudiante] = cursos

print("Los estudiantes que estan incritos en biologia son: ", biologia)
#7. Dado el siguiente diccionario:
productos = {'manzanas': 2.99, 'naranjas': 1.99, 'peras': 3.99, 'uvas': 4.99, 'kiwis': 0.99, 'duraznos': 2.49}
stock = {'manzanas': 100, 'naranjas': 50, 'peras': 25, 'uvas': 75, 'kiwis': 200, 'duraznos': 60}
#a) Imprime el precio de las naranjas.
print("El precio de las naranjas son: ",productos["naranjas"])
#b) Cambia el stock de peras a 12.
stock["peras"]="12"
print("El nuevo stock de las peras es: ",stock)
#c) Crea una función que calcule el valor total de los productos en el diccionario.
def calcularvalor (productos,stock):
    valortotal=0
    for productos,precio in productos.items():
        if productos in stock:
            cantidad= stock[productos]
            valortotal += precio* cantidad
    return valortotal
valortotal = calcularvalor(productos, stock)
print(valortotal)
