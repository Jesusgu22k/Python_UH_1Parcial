
nombre = (input("¿Cúal es tu nombre?"))
edad = int(input("¿Cúal es tu edad?"))

if edad <=17:
    print (f"Te llamas {nombre} y eres ilegal")
if edad >= 18 and edad <= 25:
      print(f"Te llamas {nombre} y ya eres mayor de edad")
else:
    print(f"Te llamas {nombre} y ya estas viejo")

