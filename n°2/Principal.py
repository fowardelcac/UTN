from Soporte import *
import random


# Función para cargar el registro manualmente.
def cargar_arreglo(n):
    b = [None] * n
    v = [None] * n
    for i in range(n):
        titulo = input("Ingrese el título del libro: ")
        titulo = validar_blanco(titulo)
        genero_num = validar_rango(0, 9,
                                   "Ingrese el género del libro (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, "
                                   "4: Economía, ""5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros): ")
        # Cambio el género numerico por su cadena de caracteres.
        genero = cambiar_genero(genero_num)
        isbn = str(input("Ingrese el ISBN correspondiente (10 digitos y separados en grupo de a 4): "))
        isbn = validar_isbn(isbn)
        idioma = validar_rango(1, 5, "Ingrese el idioma del libro(1: español, 2: inglés, 3: francés, 4:italiano, 5:otros): ")
        # Cambio el idioma numerico por su cadena de caracteres.
        idioma = cambiar_idioma(idioma)
        precio = validar_precio(0, "Ingrese el precio del libro: ")
        v[i] = Libro(titulo, genero, isbn, idioma, precio)
        # En el vector "b" se guarda los géneros, pero en forma numerica.
        b[i] = genero_num
    return v, b


# Función para cargar el registro automaticamente.
def carga_automatica(n, titulos):
    b = [None] * n
    v = [None] * n
    for i in range(n):
        titulo = random.choice(titulos)
        genero_num = random.randint(0, 9)
        genero = cambiar_genero(genero_num)
        isbn = isbn_aleatorio()
        idioma = random.randint(1, 5)
        idioma = cambiar_idioma(idioma)
        precio = random.randint(0, 1000)
        v[i] = Libro(titulo, genero, isbn, idioma, precio)
        b[i] = genero_num
    return v, b


# Función para la busqueda de un ISBN y mostrar su libro.
def libros_del_colegio(v):
    n = int(input('Ingrese cantidad de libros a buscar: '))
    total = 0
    for i in range(n):
        x = str(input('Ingrese ISBN: '))
        esta = False
        for libro in v:
            if x == libro.isbn:
                print('\nTenemos el libro ', x, ' -Titulo: ', libro.titulo, ' -Precio: $', libro.precio, sep='')
                total += libro.precio
                esta = True
        if not esta:
            print('\nNo tenemos el libro', x)
    print('El total a pagar es de $', total, sep='')


# Filtrar el género popular y mostrar los libros con dicho género
def filtrar_genero(gen_popu, libro):
    ordenar_precio(libro)
    for i in range(len(libro)):
        if gen_popu == libro[i].genero:
            mostrar(libro[i])


# Filtrar el idioma elegido y mostrar el libro más caro de dicho idioma.
def filtrar_idioma(libro):
    ordenar_precio(libro)
    idioma = validar_rango(1, 5,
                           "Ingrese el idioma del libro(1: español, 2: inglés, 3: francés, 4:italiano, 5:otros): ")
    idioma = cambiar_idioma(idioma)
    print("El libro más caro para el idioma", idioma, "es:\n")
    paso_primer_idioma = False
    for i in range(len(libro)):
        if idioma == libro[i].idioma and not paso_primer_idioma:
            paso_primer_idioma = True
            mostrar(libro[i])


# Cuento los géneros de los libros y los guardos en un vector.
def contar_genero(v_genero):
    b = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía", "Infantil",
         "Otros"]
    n = len(v_genero)
    v = [0] * 10
    may = 0
    for i in range(n - 1):
        v[v_genero[i]] += 1
    v[v_genero[-1]] += 1
    for i in range(len(v)):
        if v[i] > may:
            may = v[i]
            pos_may = i
    gen_may = b[pos_may]
    return gen_may, may, v


# Buscar en los libros el ISBN ingresado.
def busqueda_isbn(v):
    x = str(input('Ingrese ISBN: '))
    esta = False
    print("El libro con ISBN:", x, "es:\n")
    for libro in v:
        if libro.isbn == x:
            mostrar_10porciento(libro)
            esta = True
    if not esta:
        print('No existe ese libro.')


# Función para transformar el código del genero a una cadena de caracteres.
def cambiar_genero(x):
    v = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía", "Infantil",
         "Otros"]
    for i in range(len(v)):
        genero = v[x]
    return genero


# Transformar el código del idioma a una cadena de caracteres.
def cambiar_idioma(x):
    v = ["Español", "Inglés", "Francés", "Italiano", "Otros"]
    for i in range(len(v)):
        idioma = v[x - 1]
    return idioma


# Función para generar un ISBN aleatorio y guardarlo en una cadena de caracteres.
def isbn_aleatorio():
    x = 1
    n = 10
    v = ""
    while x > 0:
        # Utilice la forma inversa de validar un ISBN para generarlo, primero buscando la suma que va a ser dividida por 11.
        x = 11 * random.randint(10, 30)
        for i in range(10):
            y = random.randint(0, 9)
            # Luego le resto un número random entre 0 y 9 multiplicado por su posición.
            x -= y * n
            if n == 8 or n == 4 or n == 1:
                v += "-"
            # Si se pasa a negativo, le sumo ese número que anteriormente reste, y le resto un número menor hasta que se queda en 0.
            while x < 0:
                x += y * n
                y -= 1
                x -= y * n
            # Voy agregando esos números random válidos en una cadena.
            v += str(y)
            n -= 1
        n = 10
        # Por último, si se completaron los 10 números randoms, pero el "x" no es 0, se empieza de nuevo.
        if x != 0:
            v = ""
    return v


# Validar el valor del precio
def validar_precio(valor, texto):
    n = float(input(texto))
    while n <= valor:
        print("Error, el número ingresado debe ser mayor a", valor)
        n = float(input(texto))
    return n


# Validar que sea correcto el ISBN.
def validar_isbn(x):
    cont = 0
    acu = 0
    cont_dig = 0
    n = 10
    isbn_correct = False
    anterior = None
    num = "0123456789"
    while not isbn_correct:
        for i in x:
            cont_dig += 1
            if i == "-" and anterior in num:
                cont += 1
            anterior = i
            if i in num:
                i = int(i)
                acu += i * n
                n -= 1
            if i == "-" and cont_dig == 13:
                cont -= 1
        if cont == 3 and (acu % 11 == 0):
            isbn_correct = True
            print("ISBN correcto.")
        else:
            print("ISBN incorrecto.")
            x = input("Ingrese el ISBN correspondiente (10 digitos y separados en grupo de a 4): ")
        n = 10
        cont = 0
        cont_dig = 0
        acu = 0
        anterior = None
    return x


# Validar que el título de un libro no esté en blanco.
def validar_blanco(texto):
    while texto == "" or texto == " ":
        texto = input("Ingrese el titulo del libro: ")
    return texto


# Validar que un valor este entre un mínimo y un máximo.
def validar_rango(minimo, maximo, mensage):
    numero = minimo - 1
    while numero < minimo or numero > maximo:
        numero = int(input(mensage))
        if numero < minimo or numero > maximo:
            print('Valor incorrecto!!! El valor debe estar comprendido entre', minimo, 'y', maximo, "inclusive.")
    return numero


# Validar que un número sea mayor a otro.
def mayor_a(valor, texto):
    n = int(input(texto))
    while n <= valor:
        print("Error, el número ingresado debe ser mayor a", valor)
        n = int(input(texto))

    return n


# Función para mostrar el menú y pedir la opción.
def menu():
    print("\n\nMENU DE OPCIONES: ")
    op = 0
    while op != 8:
        print("1. Generación y carga de libros.")
        print("2. Mostrar registros de libros.")
        print("3. Mostrar el género más popular.")
        print("4. Mostrar el libro más caro de un idioma a elegir.")
        print("5. Buscar libro con ISBN.")
        print("6. Mostrar los libros del genero más popular.")
        print("7. Consultar precio mediante ISBN.")
        print("8. Salir.")
        op = validar_rango(1, 8, "Ingrese la opción que necesite: ")
        return op


# Función que muestra la cantidad de los géneros de los libros utilizando el vector que los cuenta.
def mostrar_genero(gen_popular, cantidad, v_contado):
    b = ["-Autoayuda:", "-Arte:", "-Ficción:", "-Computación:", "-Economía:", "-Escolar:", "-Sociedad:",
         "-Gastronomía:", "-Infantil:", "-Otros:"]
    for i in range(len(v_contado)):
        print(b[i], v_contado[i], ", libro/s ofrecidos.")
    print("El género más popular es", gen_popular, "con", cantidad, "libro/s ofrecidos.")


# Función principal.
def principal():
    op = 0
    paso_op1 = False

    while op != 8:
        op = menu()

        if op == 1:
            manu_auto = validar_rango(1, 2, "Elige por la forma de carga, Manual(1) o Automatica(2), por favor cargue "
                                            "con el numero 1 o 2: ")
            n = mayor_a(0, "Ingrese la cantidad de libros a cargar: ")
            if manu_auto == 1:
                v, v_genero_num = cargar_arreglo(n)
            else:
                titulos = (
                    "Cyborg del sol", "Refugio en los animales", "Promesas de mi final", "Fascinación del ayer",
                    "El amor de mi vida", "Iluminado por mi pueblo", "Serpientes y reyes", "Abandonado por mi casa",
                    "Las matemáticas más precisas",
                    "El algoritmo indescifrable", "La electricidad")
                v, v_genero_num = carga_automatica(n, titulos)
            paso_op1 = True
        if op == 2:
            if paso_op1:
                ordenar_registro(v)
                n = len(v)
                for i in range(n):
                    mostrar(v[i])
            else:
                print("Por favor, cargue libros con la opción 1.")
        if op == 3:
            if paso_op1:
                print("La cantidad de libros por género:\n")
                gen_popular, cantidad, v_contado = contar_genero(v_genero_num)
                mostrar_genero(gen_popular, cantidad, v_contado)
            else:
                print('Por favor, cargue libros con la opción 1.')
        if op == 4:
            if paso_op1:
                filtrar_idioma(v)
            else:
                print('Por favor, cargue libros con la opción 1.')

        if op == 5:
            if paso_op1:
                busqueda_isbn(v)
            else:
                print('Por favor, cargue libros con la opción 1.')
        if op == 6:
            if paso_op1:
                print("Los libros del género más popular son:\n")
                gen_popular, cantidad, v_contado = contar_genero(v_genero_num)
                filtrar_genero(gen_popular, v)
            else:
                print('Por favor, cargue libros con la opción 1.')
        if op == 7:
            if paso_op1:
                libros_del_colegio(v)
            else:
                print('Por favor, cargue libros con la opción 1.')


if __name__ == "__main__":
    principal()
