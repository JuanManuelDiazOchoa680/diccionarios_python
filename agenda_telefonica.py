agenda_telefonica = {}

nombre = ""
telefono = ""

def eleccion_menu():
    agregar_contato = print("1. Agregar contacto")
    if agregar_contato == 1:
        adicionar_contato(nombre, telefono)
    consultar_contato = print("2. Consultar contacto")
    if consultar_contato == 2:
        consultar_contacto(nombre)
    eliminar_contato = print("3. Eliminar contacto")
    if eliminar_contato == 3:
        eliminar_contacto(nombre)
    salir = print("4. Salir")
    if salir == 4:        print("Saliendo de la agenda telefónica. ¡Hasta luego!")
    input("Elija una opción: ")

def adicionar_contato(nombre, telefono):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono =  input("Ingrese el número de teléfono del contacto: ")
    agenda_telefonica[nombre] = telefono
    print("Contacto agregado exitosamente.")
    print()
    eleccion_menu()

def consultar_contacto(nombre):
    nombre = input("Ingrese el nombre del contacto a consultar: ")
    if nombre in agenda_telefonica:
        print(f"El número de teléfono de {nombre} es: {agenda_telefonica[nombre]}")
    else:
        print("Contacto no encontrado.")
    print()
    eleccion_menu()

def eliminar_contacto(nombre):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]
        print("Contacto eliminado exitosamente.")
    else:
        print("Contacto no encontrado.")
    print()
    eleccion_menu()


eleccion_menu()
adicionar_contato(nombre, telefono)
consultar_contacto(nombre)
eliminar_contacto(nombre)

