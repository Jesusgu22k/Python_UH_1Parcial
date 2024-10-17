
# ----> DECORADOR DE LIBROS <----
def decoradorMayusculas(funcion):
    def wrapper(titulo):
       
        tituloMayus = titulo.upper()
        
        return funcion(tituloMayus)
    return wrapper


@decoradorMayusculas
def buscarLibro(titulo):
   
    print(f"Buscando el libro: {titulo}...")


buscarLibro("Joyland")
