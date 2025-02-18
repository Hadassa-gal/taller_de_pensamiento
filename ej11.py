'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Copiar listas con copy()
Crea una lista llamada lista_original con varios elementos.
Asigna lista_copia = lista_original.copy().
Modifica la lista original (por ejemplo, cambia un elemento).
Imprime ambas listas para comprobar que la copia se mantiene independiente.
'''
lista_original=[2,'s',3,4,5,'f',6,7,8,'j',9,]
lista_copia=lista_original.copy()
lista_original.reverse()
print(lista_original)
print(lista_copia)
print(lista_original)