# -*- coding: utf-8 -*-

class Contacts:
#-----------Constructor-----------------
    def __init__(self, nombre, correo, telefono):
#-------------_nombre es equivalente a variable privada
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

class ContactBook:

    def __init__(self, ):
        self._contacts=[]

    def add(self,nombre,correo,telefono):
        contact=Contacts(nombre,correo,telefono)
        self._contacts.append(contact)

    def show_all(self):
    #---------iteracion  que imprime cada contacto agregado con add()
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self,nombre):
        for idx,contact in enumerate(self._contacts):
            if contact.nombre.lower()==nombre.lower():
                del self._contacts[idx]
                break


    def _print_contact(self,contact):
        print("-------*-------*------*-----*-----*----*---")
        print("Nombre: {}".format(contact.nombre))
        print("Correo: {}".format(contact.correo))
        print("Teléfono: {}".format(contact.telefono))
        print("-------*-------*------*-----*-----*----*---")



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
            contact_book.add(nombre,correo,telefono)

        elif opcion==2:
            print("Actualizando...")
        elif opcion==3:
            print("Buscando...")
        elif opcion==4:
            nombre=str(raw_input("Nombre Contacto a ELIMINAR: "))
            contact_book.delete(nombre)
        elif opcion==5:
            contact_book.show_all()
        elif opcion==6:
            print("Saliendo")
            break

if __name__=='__main__':
    run()
