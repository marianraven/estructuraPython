#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al género y
#el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su inicial y género, y muestre por pantalla el grupo
#que le corresponde.
generoM='M'
generoF='F'
genero=str(input('Ingrese la inicial de su género en mayúsculas, "F" para femenino, "M" para masculino:'))


if(genero==generoM):
    print('usted es genero masculino')
elif(genero== generoF):
    print('usted es de género femenino')    
else:
     print('ha ingresado una opción inválida') 

nombre=str(input('Ingrese la inicial de su nombre en mayúsculas:'))

if((genero==generoF) & (nombre<'M') | (genero==generoM)&(nombre>'N')):
    print('usted pertenece al grupo A')
else:
    print('Usted pertenece al grupo B')    


