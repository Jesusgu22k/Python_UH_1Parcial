class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


libro = Libro("Pedro Páramo", "Juan Rulfo", 122)
print(f"Título del libro: {libro.titulo}")
print(f"Autor del libro: {libro.autor}")
print(f"Número de páginas: {libro.paginas}")