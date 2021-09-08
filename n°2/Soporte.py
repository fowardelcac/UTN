class Libro:
    def __init__(self, titulo, genero, isbn, idioma, precio):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.idioma = idioma
        self.precio = precio


def mostrar(libro):
    print('\nTítulo:', libro.titulo, end=' ')
    print('- Género:', libro.genero, end=' ')
    print('- ISBN:', libro.isbn, end=' ')
    print('- Idioma:', libro.idioma, end=' ')
    print('- Precio: $', libro.precio, sep='')


def mostrar_10porciento(libro):
    libro.precio += libro.precio * 0.1
    print('\nTítulo:', libro.titulo, end=' ')
    print('-Género:', libro.genero, end=' ')
    print('-ISBN:', libro.isbn, end=' ')
    print('-Idioma:', libro.idioma, end=' ')
    print('-Precio: $', libro.precio, sep='')


def mostrar_libros_colegio(estan):
    print('\nISBN:', estan.isbn, ' -Titulo:', estan.titulo, '-Precio: $', estan.precio, sep='')


def ordenar_registro(libro):
    n = len(libro)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if libro[i].titulo > libro[j].titulo:
                libro[i], libro[j] = libro[j], libro[i]


def ordenar_precio(libro):
    n = len(libro)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if libro[i].precio < libro[j].precio:
                libro[i], libro[j] = libro[j], libro[i]
