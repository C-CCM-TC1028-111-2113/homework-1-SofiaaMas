def main():
    #escribe tu código abajo de esta línea
    import math
palabras=int(input('Inserta el número de palabras:'))

if palabras >0:
    a=palabras/475
    b=math.ceil(a)
    print(b)
    cobroed=b*60
    descuento=cobroed*0.1
    costototal=cobroed-descuento
    print ('El costo de publicación es:',costototal)

else: print('Número no válido')
    pass


if __name__ == '__main__':
    main()
