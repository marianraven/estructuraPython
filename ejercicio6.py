#Escribir un programa pida al usuario dos numeros enteros e informe por pantalla cual
#es menor de los dos, si son iguales, indicarlo por separado.
ingreso1= int(input("ingrese el primer número: "))
ingreso2= int(input("ingrese el segundo número: "))

if(ingreso1>ingreso2):
    print('El número menor es el segundo ingresado:', ingreso2)

elif(ingreso2> ingreso1):
    print('El número menor es el primero ingresado:', ingreso1)

else:
  print('Los números son iguales')
