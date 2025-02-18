'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Extrayendo elementos con pop()
Crea una lista con números del 1 al 5.
Crea un menú usando un ciclo que pregunte al usuario:
1. Hacer pop sin índice (pop al final)
2. Hacer pop con índice
3. Salir
En el caso 1, haz pop() sin argumentos para extraer el último elemento y muéstralo en pantalla.
En el caso 2, pide al usuario el índice y haz pop(indice). Muestra el elemento extraído.
En cada extracción, imprime la lista resultante.
'''
msg='''
          MENU
1) hacer pop sin indice(pop al final)
    2) hacer pop con indice
        3) salir
'''
number=[1,2,3,4,5]
while True:
    print(msg)
    op=input('ingrese su elección: ')
    match(op):
        case 1:
            print(number)
            number.pop()
            print(number)
        case 2:
            print(number)
            while True:
                x=input('ingrese el numero que quiera quitar de la lista: ')
                if x in number:
                    number.pop(x)
                    break
                else:
                    continue
            print(number)
        case 3:
            print(number)
            print('saliendo . . .')
            break
        case _:
            print('opción no valida, vuelva a ingresar . . .')