def main():
    #escribe tu código abajo de esta línea
    numeros=input('Inserte un número:')
a=0
if int(numeros[0])%2 ==0:
    a=a+1
else: a=a+0
if int(numeros[1])%2 ==0:
    a=a+1
else: a=a+0
if int(numeros[2])%2 ==0:
    a=a+1
else: a=a+0
if int(numeros[3])%2 ==0:
    a=a+1
else: a=a+0

print('El número de dígitos pares son:',a)
    pass


if __name__ == '__main__':
    main()
