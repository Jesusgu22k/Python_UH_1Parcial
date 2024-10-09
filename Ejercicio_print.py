import pint 

ureg = pint.UnitRegistry()

def CelaFa():
    #Convierte de celsius a farenheit

    celcius = float(input("¿Cuantos grados Celcius quieres convertir?: "))

    valor =  celcius*ureg('degF')
    
    return valor

while True:
    print ("---- Bienvenido ----")
    print("1. Covertir de Grados Celcius a Farenheit")
    print("2. Restar dos números")
    print("3. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        CelaFa()
    elif opcion == "2":
        restar()
    elif opcion == "3":
        salir()
    else:
        print("Opción inválida. Intente nuevamente.")





