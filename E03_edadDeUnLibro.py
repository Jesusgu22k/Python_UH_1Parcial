from datetime import datetime

def edadDelLibro(año):
    
    añoActual = datetime.now().year
    
    calcularEdad = lambda año: añoActual - año
    
    return calcularEdad(año)


edad = edadDelLibro(2013)
print(f'El libro tiene la edad de:  {edad} años')
