def main():
    #escribe tu código abajo de esta línea
    santerior=float(input('Inserte su saldo del mes anterior:'))
ingresos=float(input('Inserte sus ingresos:'))
egresos=float(input('Inserte sus egresos:'))
cheques=int(input('Inserte el número de cheques expedidos:'))

c=13
costcheques=cheques*c

stotal=santerior+ingresos-egresos-costcheques

interes=stotal*0.075
smensual=stotal-interes
print('El saldo final mensual es:',smensual)
    pass

if __name__ == '__main__':
    main()
