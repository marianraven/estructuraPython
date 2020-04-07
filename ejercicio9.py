#Escribir un programa que pida al usuario un número entero del 1 al 7 y muestre por
#pantalla el día de la semana correspondiente. Controlar que el número se encuentre
#en el rango correcto, si no es así, informar un error. Si el número es 2 el dia es
#martes.
ingreso= int(input('ingrese un número de 1 al 7:'))
if(ingreso==1):
    print('El día de la semana correspondiente al 1 es lunes')
elif(ingreso==2):
    print('El día de la semana correspondiente al 2 es martes')   
elif(ingreso==3):
    print('El día de la semana correspondiente al 3 es miércoles')   
elif(ingreso==4):
    print('El día de la semana correspondiente al 4 es jueves')   
elif(ingreso==5):
    print('El día de la semana correspondiente al 5 es viernes') 
elif(ingreso==6):
    print('El día de la semana correspondiente al 6 es sábado')   
elif(ingreso==7):
    print('El día de la semana correspondiente al 7 es domingo')  
else:
    print('El número ingresado es incorrecto, ingrese nuevamente :')        
    ingresoNuevo= int(input('ingrese un número de 1 al 7:'))
    if(ingresoNuevo<=0 | ingresoNuevo>7):
        print('usted ha ingresado nuevamente un número fuera de rango, intente más tarde')
    else:
        ingreso=ingresoNuevo
    if(ingreso==1):
         print('El día de la semana correspondiente al 1 es lunes')
    elif(ingreso==2):
         print('El día de la semana correspondiente al 2 es martes')   
    elif(ingreso==3):
         print('El día de la semana correspondiente al 3 es miércoles')   
    elif(ingreso==4):
         print('El día de la semana correspondiente al 4 es jueves')   
    elif(ingreso==5):
         print('El día de la semana correspondiente al 5 es viernes') 
    elif(ingreso==6):
         print('El día de la semana correspondiente al 6 es sábado')   
    elif(ingreso==7):
         print('El día de la semana correspondiente al 7 es domingo')    
    else:
         print('El número ingresado es incorrecto,sólo tenía un intento')        