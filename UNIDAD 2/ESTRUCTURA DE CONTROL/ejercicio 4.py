def mayor_de_edad(edad):
    bandera=False
    if edad>=17:
       bandera=True
    return bandera
while True:
    dato =int(input("Ingrese la edad: "))
    if mayor_de_edad(dato)==True:
        print("Es mayor de edad")
        break
    else:
        print("Es menor de edad")