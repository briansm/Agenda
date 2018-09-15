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
                print("CONTACTO ELIMINADO")
                break

    def search(self,nombre):
        for contact in self._contacts:
            if contact.nombre.lower()==nombre.lower():
                self._print_contact(contact)
                break
        else:
            print("NO SE ENCONTRO")

    def update(self,nombre):

        for idx,contact in enumerate(self._contacts):
            if contact.nombre.lower()==nombre.lower():
                contact.nombre=str(raw_input("Nuevo nombre: "))
                contact.correo=str(raw_input("Nuevo correo: "))
                contact.telefono=int(input("Nuevo telefono: "))
                self._contacts[idx]=contact
                break
        else:
            print("NO SE ENCONTRO")



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
            nombre=str(raw_input("Nombre Contacto a Actualizar: "))
            contact_book.update(nombre)
        elif opcion==3:
            nombre=str(raw_input("Nombre Contacto a BUSCAR: "))
            contact_book.search(nombre)
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
