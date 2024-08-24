print('Programa que determina si un año es bisiesto')

dias = int(input('Ingrese la cantidad de dias que tuvo el año \t'))

if dias % 4 == 0:
    if dias % 100 == 0:
        if dias % 400 == 0:
            print('El año si es bisiesto')
            
        else:
            print('El año no es bisiesto')
            
    else:
            print('El año si es bisiesto')
else:
    print('El año no es bisiesto')