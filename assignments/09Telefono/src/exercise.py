def main():
    #escribe tu código abajo de esta línea
    mensaje=int(input('Inserte el número de mensajes:'))
megas=float(input('Inserte el número de megas:'))
minutos=int(input('Inserte el número de minutos:'))
costo=0.8
x=mensaje*costo
y=megas*costo
z=minutos*costo

mensual=x+y+z
print('El costo mensual es:', mensual)
    #Leer los datos
    pass


if __name__ == '__main__':
    main()
