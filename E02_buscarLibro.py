# ----- Buscar libros dentro de la biblioteca -----


libros = [
    {"titulo": "Pedro páramo", "autor": "Juan Rulfo", "año": 1955, "genero": "Novela"},
    {"titulo": "Joyland", "autor": "Stephen King ", "año": 2013, "genero": "Novela"},
    {"titulo": "En las montañas de la locura", "autor": "H.P Lovecraft", "año": 1936, "genero": "Ficción/Terror"},
    {"titulo": "El resplandor", "autor": "Stephen king", "año":"1977", "genero": "Terror/suspenso"},
    {"titulo": "Cartero", "autor":"Charles Bukowski", "año": "1971", "genero": "Novela"}
    
]

def buscarLibros(titulo):
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['año']}")
            print(f"Género: {libro['genero']}")
            return
    
    print(f"El libro '{titulo}' no está en la biblioteca.")


buscarLibros("Joyland")
