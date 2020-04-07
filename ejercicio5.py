ladoRectangulo=int(input("Ingrese lado de rectángulo:"))
baseRectangulo=int(input("Ingrese base de rectángulo:"))

perimetroRectangulo=((ladoRectangulo*2) + (baseRectangulo*2))
areaRectangulo=baseRectangulo* ladoRectangulo

print('El perímetro del rectángulo es:',perimetroRectangulo)

print('El área del rectángulo es:',areaRectangulo)

radioCirculo=int(input("Ingrese el radio del círculo:"))
pi= 3.14

perimetroCirculo= 2*pi*radioCirculo
areaCirculo=((radioCirculo * radioCirculo) * pi)

print('El perímetro del círculo es:',perimetroCirculo)

print('El área del círculo es:',areaCirculo)
