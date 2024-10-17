def lista_invitados():
    invitados = input('Ingrese el nombre del invitado o "end" para cerrar: ')
    lista =[]
    while invitados != "end":
        lista.append(invitados)
        invitados = input('Ingrese el nombre del invitado o "end" para cerrar: ')
    
    return lista

print()
print()     
print("Los invitados a la fiesta son: ",lista_invitados())
