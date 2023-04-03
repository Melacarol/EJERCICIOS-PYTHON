print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 30/03/2023\n")
salario=float(input("ingrese su sueldo: "))
porcentaje=0
if salario < 10000:
    print("el impuesto es del: 5%")
    porcentaje =5/100
elif salario >= 10000 and salario <= 20000:
    print("el impuesto es del: 15%")
    porcentaje =15/100
elif salario >= 20000 and salario <= 35000:
    print("el impuesto es del: 20%")
    porcentaje =20/100
elif salario >= 35000 and salario <= 60000:
    print("el impuesto es del: 30%")
    porcentaje =30/100
elif salario >= 60000:
    print("el impuesto es del: 45%")
    porcentaje =45/100
else:
    print("el salario ingresado es incorrecto")

total=salario*porcentaje
print("el valor del impuesto a pagar es: ", total)
print("el salario a recibir es: ", salario-total)