#Turno 04 – Enunciado 03 [T4E3]:

#Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

#1.)    Ingrese los tiempos de tres competidores en una prueba de natación, y cargue también los
# nombres de esos competidores. Determine y muestre el tiempo del ganador pero muestre también su nombre.
# Calcule y muestre las diferencias entre el tiempo del ganador y el tiempo de los otros dos.

#2.)    Ingrese por teclado una secuencia de n números enteros (n se carga también por teclado),
# a razón de uno por vuelta de ciclo. Determine el promedio de todos los números cargados que hayan
# sido mayores que cero. Informe si ese promedio es menor, igual o mayor que un valor x que se carga por teclado.

#3.)    Terminar el programa.

_Autor_ = "Saldaño Juan Cruz 1K7(91502)"

# Presento el menu de opciones
print("\t Menu de opciones.")
print("-" * 80)
print("1) Prueba de natacion.")
print("2) Secuencia de numeros enteros.")
print("3) Terminar el programa.")
print("-" * 80)

# Inicio ciclo
opcion = None
while opcion != 3:
    # Input para ingresar opcion
    opcion = int(input("Ingresar una opcion: "))

    # Opcion uno
    if opcion == 1:

        # Contadores
        menor_tiempo = 0
        mejor_competidor = 0

        # Banderas
        primer_competidor = True

        # Inicio ciclo
        for i in range(3):

            # Carga de datos
            competidor = input("Ingrese el nombre del competidor: ")
            tiempo = int(input("Ingrese el tiempo del competidor.(En segundos.): "))

            # Calculos para el primer competidor
            if primer_competidor:
                mejor_competidor = competidor
                menor_tiempo = tiempo
                primer_competidor = False

            else:
                if menor_tiempo > tiempo:
                    mejor_competidor = competidor
                    menor_tiempo = tiempo

        # Visualizacion
        print("El gandor es:", mejor_competidor, "Su tiempo fue:", menor_tiempo, "s")

        print("Terminado, ingrese otra opcion.")
        print("-" * 80)
    # Opcion 2
    elif opcion == 2:

        # Contadores
        suma_de_secuencia = 0
        contador = 0

        # Ingreso cantidad de numeros
        n = int(input("Ingresar la cantidad de numeros que desea obtener en la secuencia: "))
        # Comienzo ciclo
        for num in range(n):
            numero = int(input("Ingresar secuencia de numeros enteros(SOLO ENTEROS!!): "))
            suma_de_secuencia += numero
            contador += 1
        # Para evitar errores compruebo si el contador es != cero.
        # Solo numeros mayores a cero.
        if contador != 0 and numero > 0:
            promedio = round(suma_de_secuencia / contador, 2)
            print("El promedio de la secuencia es:", promedio)

            # Cargar nuevo numero.
            x = int(input("Ingresar nuevo numero: "))

            if promedio == x:
                print("El promedio es igual al valor del nuevo numero.")

            elif promedio > x:
                print("El promedio es mayor al valor del nuevo numero.")

            else:
                print("El promedio es menor al valor del nuevo numero. ")

        print("Terminado, ingrese otra opcion.")
        print("-" * 80)

    # opcion tres
    elif opcion == 3:
        print("Programa finalizado. Hasta pronto.")
        print("-" * 80)

    # Si el usuario se equivoca comienza de nuevo
    else:
        print("ERROR!!! \nIngresar una opcion valida del menu.")