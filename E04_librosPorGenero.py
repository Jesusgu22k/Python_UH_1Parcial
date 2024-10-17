

# -----> LIBROS POR GENERO <-----
libros = [
     {"titulo": "Pedro páramo", "genero": "Novela"},
    {"titulo": "Joyland", "genero": "Novela"},
    {"titulo": "En las montañas de la locura", "genero": "Ficción/Terror"},
    {"titulo": "El resplandor", "genero": "Terror"},
    {"titulo": "Cartero", "genero": "Novela"}
]


def librosPorGenero(genero):
    
    libros_filtrados = [libro['titulo'] for libro in libros if libro['genero'] == genero]
    
    
    if libros_filtrados:
        print(f"Libros en el género '{genero}':")
        for libro in libros_filtrados:
            print(f"- {libro}")
    else:
        print(f"No se encontraron libros en el género '{genero}'.")


librosPorGenero("Terror")
