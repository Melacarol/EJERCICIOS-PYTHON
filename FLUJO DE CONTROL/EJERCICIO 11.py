print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 31/03/2023\n")
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el terser numero: "))

if a>b and a >c :
    print ("el numero ",a ," es mayor al segundo y terser numero")
elif b>a and b >c :
    print ("el numero ",b ," es mayor al primer y terser numero")
elif c>b and c >a :
    print ("el numero ",c ," es mayor al primer y segundo numero")
else :
    print ("Ninguno es mayor ")