'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Ordenar una lista con sort()
Crea una lista de números desordenados: por ejemplo [3, 8, 1, 7, 2].

Aplica sort() para ordenarla de forma ascendente.

Imprime la lista resultante.

Pide al usuario que indique si desea el orden

ascendente o descendente

Si indica descendente, vuelve a aplicar sort(reverse=True).
Imprime el resultado final.
'''
lista=[3, 8, 1, 7, 2]
print(f'lista desordenada: {lista}')
lista.sort()
print(f'lista ordenada: {lista}')
while True:
    try:
        op=int(input('como quiere organizar la lista? \n 1) orden ascendente\n 2) orden desendente\n ingrese su elección: '))
    except ValueError:
        print('error, vuelva a ingresar . . .')
    else:
        break
match(op):
    case 1:
        lista.sort()
        print(f'de forma ascendente: {lista}')
    case 2:
        lista.sort(reverse=True)
        print(f'de forma descendente: {lista}')