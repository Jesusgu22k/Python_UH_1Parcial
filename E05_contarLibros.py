# ----> CONTAR LIBROS <-----
libros = [
    "El resplandor",
    "Joyland",
    "En las montañas de la locura",
    "El hombre mas rico de babilonia",
    "Habitos atomicos",
    
]


def contarLibros(lista_libros):
    
    if not lista_libros:
        return 0
   
    return 1 + contarLibros(lista_libros[1:])


totalLibros = contarLibros(libros)
print(f'El total de libros en la biblioteca es: {totalLibros}')
