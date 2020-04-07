#Escribir un programa que recibe como entrada desde el usuario dos números enteros
#e informa por pantalla todos los números pares entre ellos.
ingreso1= int(input('ingrese el número 1:'))
ingreso2= int(input('ingrese el número 2:'))
if(ingreso1<ingreso2):
    while ingreso1 < ingreso2:
      ingreso2-=1
      if(ingreso2%2==0):
          print(ingreso2)
              
else:
    while ingreso2 < ingreso1:
       ingreso1-=1
       if(ingreso1%2==0):
         print(ingreso1)   