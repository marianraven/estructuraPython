#Escribir un programa que pida al usuario un número entero e indique si dicho número
#es par o impar.
numero= int(input('Ingrese un número:'))

if(numero%2==0):
    print('El número ingresado :',numero,'es par')

else:
    print('El número ingresado: ',numero,' es impar')