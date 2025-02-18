'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Contar ocurrencias con count()
Crea una lista con varios elementos repetidos, por ejemplo ["manzana", "pera", "manzana", "naranja", "manzana"].
Pide al usuario una fruta para contar cuántas veces aparece en la lista.
Usa count() y muestra el resultado.
Si la cuenta es 0, indica que la fruta no está en la lista.
'''
fruits=['tomate','tomate','naranja','naranja',"manzana", "pera", "manzana", "naranja", "manzana"]
while True:
    x=input('ingrese el nombre de una fruta: ')
    if x in fruits:
        print(fruits.count(x))
        break
    else:
        print(f'{x} no se encuentra en la lista')
