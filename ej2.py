'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Extendiendo una lista
Crea una lista llamada numeros con algunos valores iniciales, por ejemplo: [1, 2, 3].
Pide al usuario que ingrese tres números adicionales separados por espacio y conviértelos a enteros.
Usa extend() para agregar estos nuevos números a la lista numeros.
Imprime la lista final.
'''
numeros=[1,2,3]
x=[]
x=map(int,input('ingrese numeros que quiera, separados por espacios: ').split(' '))
numeros.extend(x)
print(numeros)