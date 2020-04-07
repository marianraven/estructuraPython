#Escribir un programa que pregunte el nombre del usuario en la consola y un número
#entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
#como el número introducido.
nombre= str(input('Ingrese su nombre: '))
entero= int(input('Ingrese un número entero: '))
for i in range(entero):
    entero-=1
    print(nombre,'número de vuelta:',i)