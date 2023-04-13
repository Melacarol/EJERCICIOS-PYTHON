print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 31/03/2023\n")
calificacion= float (input( "ingrese la calificacion del examen con punto: "))
print(calificacion )
if calificacion>=9.50 and calificacion <=10:
    print("La calificacion es: Exelente")
elif calificacion>=8.50 and calificacion <9.50:
    print("La calificacion es: Muy bueno")
elif calificacion>=7.00 and calificacion <8.50:
    print("La calificacion es: Bueno")
elif calificacion>=4.00 and calificacion <7.00:
    print("La calificacion es: Regular")
else :
    print("La calificacion es: Deficiente")