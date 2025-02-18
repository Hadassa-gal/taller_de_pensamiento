'''
nombre: Hadassa Galindo
Fecha: 3 de febrero 2025
descripción del ejercicio:
Creación de una agenda de contactos
Crea una lista vacía para almacenar contactos.
Cada contacto será un diccionario con {"nombre": <str>, "tel": <str>}.
Crea una función llamada agregar_contacto que reciba la lista y agregue un nuevo contacto a partir de datos ingresados por el usuario.
La función debe usar append() para insertar el diccionario.
Muestra la lista de contactos después de cada inserción.
'''
contactos=[]
persona={
    'nombre':'hadassa',
    'tel':'1234567890'
}
def agregar_contacto():
    contactos.append(dict(Nombre=input('ingrese el nombre del nuevo contacto: '),
tel=input('ingrese el telefono del contacto: ')))
    return contactos

while True:
    op=int(input('--ingresar contactos--\n1)si\n2)no\nhaga su elección: '))
    match(op):
        case 1:
            agregar_contacto()
            print(contactos)
        case 2:
            print('saliendo . . .')
            break
