#Escribir un programa que imprima por pantalla todas las fichas del domino, una por
#linea, sin repetir.
print('fichas del dominó')
primerNumero=1
ultimoNumero=7

while primerNumero < ultimoNumero:
    ultimoNumero-=1
    print('_________')
    print('*'*ultimoNumero,'|','*'*primerNumero)
    print('         |')
    print('_________|')

print('siguientes fichas-------------------------')
segundoNumero=2
ultimoSegundo=7
while segundoNumero< ultimoSegundo:
    ultimoSegundo-=1 
    print('_________')
    print('*'*ultimoSegundo,'|','*'*segundoNumero)
    print('_________|')

print('siguientes fichas-------------------------')
tercerNumero=3
ultimoTercero=7
while tercerNumero< ultimoTercero:
    ultimoTercero-=1
    print('_________')
    print('*'*ultimoTercero,'|','*'*tercerNumero)
    print('         |')
    print('_________|')
        
print('siguientes fichas-------------------------')
cuartoNumero=4
ultimoCuarto=7
while cuartoNumero< ultimoCuarto:
    ultimoCuarto-=1
    print('_________')
    print('*'*ultimoCuarto,'|','*'*cuartoNumero)
    print('         |')
    print('_________|')
           
print('siguientes fichas-------------------------')
quintoNumero=5
ultimoQuinto=7
while quintoNumero< ultimoQuinto:
    ultimoQuinto-=1
    print('_________')
    print('*'*ultimoQuinto,'|','*'*quintoNumero)
    print('         |')
    print('_________|')
           
print('siguientes fichas-------------------------')
sextoNumero=6
ultimoSexto=7
while sextoNumero< ultimoSexto:
    ultimoSexto-=1
    print('_________')
    print('*'*ultimoSexto,'|','*'*sextoNumero)
    print('         |')
    print('_________|')          