#Escribir un programa que pida al usuario dos numeros enteros e imprima todos los
#numeros enteros entre los dos.
ingreso1= int(input('ingrese el número 1:'))
ingreso2= int(input('ingrese el número 2:'))
if(ingreso1<ingreso2):
    while ingreso1 < ingreso2:
        ingreso2-=1
        print(ingreso2)
else:
    while ingreso2 < ingreso1:
       ingreso1-=1
       print(ingreso1)       