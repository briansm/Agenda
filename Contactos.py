# -*- Coding: utf-8 -*-

class Contacts:
#-----------Constructor-----------------
    def __init__(self, nombre, correo, telefono):
#-------------_nombre es equivalente a variable privada
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

class ContactBook:

    def __init__(self, ):
        self._contacts=[]

    def add(self,nombre,correo,telefono):
        print("nombre: {} correo: {} telefono: {}".format(nombre,correo,telefono))




def run():
#--------instancia del objeto COntactBook
    contact_book= ContactBook()

    while True:
        opcion=int(input('''
                ---------BIENVENIDO-----------

                Que Desea realizar:

                1.Agregar Contacto
                2.Actualaizar Contacto
                3.Buscar Contacto
                4.Eliminar Contacto
                5.Mostrar Contactos
                6.Salir

                '''))

        if opcion==1:
            nombre=str(raw_input("Nombre Contacto: "))
            correo=str(raw_input("Correo Electronico: "))
            telefono=int(input("Numero de Telefono: "))
            contact_book.add(nombre,correo, telefono)
            print("Agregando...")
            
        elif opcion==2:
            print("Actualizando...")
        elif opcion==3:
            print("Buscando...")
        elif opcion==4:
            print("Eliminando...")
        elif opcion==5:
            print("Mostrando...")
        elif opcion==6:
            print("Saliendo")
            break

if __name__=='__main__':
    run()
