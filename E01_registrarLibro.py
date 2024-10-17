# Registro de libro utilizando una función


def registroLibro (**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
print("-----------------------------------------------")
print(" Libro a registrar: ")
registroLibro(Titulo ="El hombre más rico de babilonia",Autor="George S. Clason",Publicación = "1926", Categoria = "Libro de autoayuda")

print ("Libro registrado en la biblioteca correctamente!")
print("-----------------------------------------------")