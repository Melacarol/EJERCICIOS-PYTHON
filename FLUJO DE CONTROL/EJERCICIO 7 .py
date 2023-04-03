print("Curso: FUNDAMENTOS DE PYTHON")
print("Estudiante: Melanie Torres")
print("Fecha: 31/03/2023\n")
print('\n\tPizzería Napolitana\n\n\tMenú de Pizzas\n1.Pizzas vegetarianas\n2.Pizzas no vegetarianas')
opción=int(input('Ingrese una opción del menú: '))
if opción==1:
    print('\tUsted eligio el tipo de pizzas vegetarianas\nLos ingredientes disponibles son:\n1.Pimiento\n2.tofu\n Solo puede elegir un ingrediente!!!')
    ingredientev=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientev==1:
        print('Su pizza consta de Pimiento,mozzarella y tomate!!')
    elif ingredientev==2:
        print('Su pizza consta de Tofu,mozzarella y tomate!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')
elif opción==2:
    print('\tUsted eligio el tipo de pizzas no vegetarianas\nLos ingredientes disponibles son:\n1.Peperoni\n2.Jamón\nSalmon\nSolo puede elegir un ingrediente!!!')
    ingredientesn=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientesn==1:
        print('Su pizza consta de Peperoni,mozzarella y tomate!!')
    elif ingredientesn==2:
        print('Su pizza consta de Jamón,mozzarella y tomate!!')
    elif ingredientesn==3:
        print('Su pizza consta de Salmon,mozzarella y tomate!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')