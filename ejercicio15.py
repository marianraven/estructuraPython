#Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo, de altura igual al número introducido.
numero=int(input('Ingrese un número entero:'))

print('El triángulo rectangulo que le corresponde a su número es el siguiente:')
nulo=0
while nulo<=(numero-1):
    nulo+=1
    print('*'*nulo)