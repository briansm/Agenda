# -*- Coding: utf-8 -*-






def run():
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
