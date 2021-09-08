import random
print('EL JUEGO DE DADOS [versión 2.0]')
dado = 1, 2, 3, 4, 5, 6
puntos1 = 0
puntos2 = 0
jugada_ganada1 = 0
jugada_ganada2 = 0
jugadas_totales = 0
seguida1 = 0
seguida2 = 0
empate = False
porcentaje_ganador = False

#funcion para encontrar el mayor
def mayor(x, y, z):
    if x > y and x > z:
        mayor = x
    elif y > z:
        mayor = y
    else:
        mayor = z
    return mayor

#funcion para encontrar el menor
def menor(x, y, z):
    if x < y and x < z:
        menor = x
    elif y < z:
        menor = y
    else:
        menor = z
    return menor

#funcion para saber si la suma es par
def par(suma, paridad):
    if suma % 2 == 0 and paridad == 'par':
        return True
    return False

#funcion para saber si la suma es impar
def impar(suma, paridad):
    if suma % 2 == 1 and paridad == 'impar':
        return True
    return False

#funcion para saber si los tres dados tienen la misma paridad
def paridad(x, y, z):
    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        return True
    if x % 2 == 1 and y % 2 == 1 and z % 2 == 1:
        return True
    return False

#Comienza el juego
x = int(input('Para comenzar ingrese el puntaje a alcanzar (debe ser mayor a 10): '))
while x <= 10:
    print('ERROR. Rango incorrecto.')
    x = int(input('Por favor ingrese un valor mayor a 10: '))

jugador1 = input('Ingrese el nombre del primer jugador: ')
jugador2 = input('Ingrese el nombre del segundo jugador: ')

while puntos1 < x and puntos2 < x:
    jugadas_totales += 1
    #tiro del primer jugador
    paridad1 = input('\n'+jugador1+', ¿Apuestas por "par" o "impar"?: ').lower()
    input('Presione ENTER para tirar los dados.')

    a = random.choice(dado)
    b = random.choice(dado)
    c = random.choice(dado)
    tiro1 = a, b, c
    suma1 = a + b + c
    may1 = mayor(a, b, c)
    men1 = menor(a, b, c)

    print('Los dados son ', tiro1, ' y suman ', suma1, '.', sep='')

    if par(suma1, paridad1):
        seguida1 += 1
        puntos1 += may1
        jugada_ganada1 += 1
        print('Predicción correcta!', jugador1, 'suma', may1, 'puntos.')
        print('Puntos de ', jugador1, ': ', puntos1, sep='')

        if paridad(a, b, c):
            print('Los tres dados son de la paridad elegida ¡Se duplica el puntaje!')
            puntos1 += may1
            print('Puntos de ', jugador1, ': ', puntos1, sep='')

    elif impar(suma1, paridad1):
        seguida1 += 0
        jugada_ganada1 += 1
        puntos1 += may1
        print('Predicción correcta!', jugador1, 'suma', may1, 'puntos.')
        print('Puntos de ', jugador1, ': ', puntos1, sep='')

        if paridad(a, b, c):
            print('Los tres dados son de la paridad elegida ¡Se duplica el puntaje!')
            puntos1 += may1
            print('Puntos de ', jugador1, ': ', puntos1, sep='')

    else:
        seguida1 = 0
        puntos1 -= men1
        print('Predicción incorrecta :(', jugador1, 'resta', men1, 'puntos.')
        print('Puntos de ', jugador1, ': ', puntos1, sep='')

    #tiro del segundo jugador
    paridad2 = input('\n'+jugador2+', ¿Apuestas por "par" o "impar"?: ').lower()
    input('Presione ENTER para tirar los dados.')

    d = random.choice(dado)
    e = random.choice(dado)
    f = random.choice(dado)
    tiro2 = d, e, f
    suma2 = d + e + f
    may2 = mayor(d, e, f)
    men2 = menor(d, e, f)

    print('Los dados son ', tiro2, ' y suman ', suma2, '.', sep='')

    if par(suma2, paridad2):
        seguida2 += 1
        jugada_ganada2 += 1
        puntos2 += may2
        print('Predicción correcta!', jugador2, 'suma', may2, 'puntos.')
        print('Puntos de ', jugador2, ': ', puntos2, sep='')

        if paridad(d, e, f):
            print('Los tres dados son de la paridad elegida ¡Se duplica el puntaje!')
            puntos2 += may2
            print('Puntos de ', jugador2, ': ', puntos2, sep='')

    elif impar(suma2, paridad2):
        seguida2 += 1
        jugada_ganada2 += 1
        puntos2 += may2
        print('Predicción correcta!', jugador2, 'suma', may2, 'puntos.')
        print('Puntos de ', jugador2, ': ', puntos2, sep='')

        if paridad(d, e, f):
            print('Los tres dados son de la paridad elegida ¡Se duplica el puntaje!')
            puntos2 += may2
            print('Puntos de ', jugador2, ': ', puntos2, sep='')

    else:
        seguida2 = 0
        puntos2 -= men2
        print('Predicción incorrecta :(', jugador2, 'resta', men2, 'puntos.')
        print('Puntos de ', jugador2, ': ', puntos2, sep='')

    if puntos1 == puntos2:
        empate = True


#Fin del juego. Salidas.
print('')
porcentaje1 = jugada_ganada1*100/ jugadas_totales
porcentaje2 = jugada_ganada2*100/ jugadas_totales
promedio1 = round(puntos1 / jugadas_totales, 2)
promedio2 = round(puntos2 / jugadas_totales, 2)

if puntos1 > puntos2:
    print(jugador1, ': ', puntos1, '. WINNER.', sep='')
    print(jugador2, ': ', puntos2, '. LOOSER.', sep='')
    if porcentaje1 > porcentaje2:
        porcentaje_ganador = True

elif puntos1 < puntos2:
    print(jugador2, ': ', puntos2, '. WINNER.', sep='')
    print(jugador1, ': ', puntos1, '. LOOSER.', sep='')
    if porcentaje1 < porcentaje2:
        porcentaje_ganador = True

else:
    if jugada_ganada1 > jugada_ganada2:
        print(jugador1, 'gana por tener mayor cantidad de partidas ganadas.')
        print(jugador1, ': ', puntos1, sep='')
        print(jugador2, ': ', puntos2, sep='')

    elif jugada_ganada1 < jugada_ganada2:
        print(jugador2, 'gana por tener mayor cantidad de partidas ganadas.')
        print(jugador2, ': ', puntos2, sep='')
        print(jugador1, ': ', puntos1, sep='')

    else:
        print('EMPATE.')
        print(jugador1, ': ', puntos1, sep='')
        print(jugador2, ': ', puntos2, sep='')

print('Jugadas realizadas:', jugadas_totales)

if empate:
    print('Hubo al menos una jugada con los puntajes empatados.')

print('El promedio de puntaje de', jugador1, 'es', promedio1)
print('El promedio de puntaje de', jugador2, 'es', promedio2)

print('El promedio de jugadas ganadas de ', jugador1, ' es ', porcentaje1, '%', sep='')
print('El promedio de jugadas ganadas de ', jugador2, ' es ', porcentaje2, '%', sep='')

if porcentaje_ganador:
    print('El ganador tuvo mayor porcentaje de jugadas ganadas.')

if seguida1 >= 3:
    print(jugador1, 'acertó en tres o más partidas seguidas.')
if seguida2 >= 3:
    print(jugador2, 'acertó en tres o más partidas seguidas.')
