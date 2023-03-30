num1 = int ( input ( "ingresar primer numero: " ))
num2 = int ( input ( "ingresar el segundo numero: " ))

x = num1  ==  num2
#opción 1
print ( "los numeros: "  +  str ( num1 ) +  " y "  +  str ( num2 ) +  " son iguales: "  +  str ( x ))
#opción 2
print ( "los numeros:" , ( num1 ), "y" , ( num2 ), "son iguales:" ,( x ))
#opción 3
print ( f"los numeros: { num1 } y { num2 } son iguales: { x } " )
#opción 4
print ( "los numeros: {} y {} son iguales: {} \n " . format ( num1 , num2 , x ))

y = num1  !=  num2
#opción 1
print ( "los numeros: "  +  str ( num1 ) +  " y "  +  str ( num2 ) +  " son diferentes: "  +  str ( y ))
#opción 2
print ( "los numeros:" , ( num1 ), "y" , ( num2 ), "son diferentes:" ,( y ))
#opción 3
print ( f"los numeros: { num1 } y { num2 } son diferentes: { y } " )
#opción 4
print ( "los numeros: {} y {} son diferentes: {} \n " . format ( num1 , num2 , y ))

z = num1 > num2
#opción 1
print ( "entre los numeros: "  +  str ( num1 ) +  " y "  +  str ( num2 ) +  " el primer numero es mayor: "  +  str ( z ))
#opción 2
print ( "entre los numeros:" , ( num1 ), "y" , ( num2 ), "el primer numero es mayor:" ,( z ))
#opción 3
print ( f"entre los numeros: { num1 } y { num2 } el primer numero es mayor: { z } " )
#opción 4
print ( "entre los numeros: {} y {} el primer numero es mayor: {} \n " . format ( num1 , num2 , z ))

a = num1 <= num2
#opción 1
print ( "entre los numeros: "  +  str ( num1 ) +  " y "  +  str ( num2 ) +  " el segundo es mayor o igual que el primero: "  +  str ( a ))
#opción 2
print ( "entre los numeros:" , ( num1 ), "y" , ( num2 ), "el segundo es mayor o igual que el primero:" ,( a ))
#opción 3
print ( f"entre los numeros: { num1 } y { num2 } el segundo es mayor o igual que el primero: { a } " )
#opción 4
print ( "entre los numeros: {} y {} el segundo es mayor o igual que el primero: {}" . format ( num1 , num2 , a ))