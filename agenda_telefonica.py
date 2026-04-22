agenda_telefonica = {}

nombre = ""
telefono = ""
opcion = None

print("██╗  ██╗ ██████╗ ██╗      █████╗     ██████╗ ███████╗██████╗  █████╗ ")
print("██║  ██║██╔═══██╗██║     ██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗")
print("███████║██║   ██║██║     ███████║    ██████╔╝█████╗  ██████╔╝███████║")
print("██╔══██║██║   ██║██║     ██╔══██║    ██╔═══╝ ██╔══╝  ██╔═══╝ ██╔══██║")
print("██║  ██║╚██████╔╝███████╗██║  ██║    ██║     ███████╗██║     ██║  ██║")
print("╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝╚═╝     ╚═╝  ╚═╝")

def eleccion_menu():
    print("1. Agregar contacto")
    print("2. Consultar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar agenda")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        adicionar_contato(nombre, telefono)
        eleccion_menu()
    elif opcion == 2:
        consultar_contacto(nombre)
        eleccion_menu()
    elif opcion == 3:
        eliminar_contacto(nombre)
        eleccion_menu()
    elif opcion == 4:
        mostrar_agenda()
        eleccion_menu()
    elif opcion == 5:
        print("Saliendo de la agenda telefónica. ¡Hasta luego!")
    else:    
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
        eleccion_menu()

def adicionar_contato(nombre, telefono):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono =  input("Ingrese el número de teléfono del contacto: ")
    agenda_telefonica[nombre] = telefono
    print("Contacto agregado exitosamente.")
    print()

def consultar_contacto(nombre):
    nombre = input("Ingrese el nombre del contacto a consultar: ")
    if nombre in agenda_telefonica:
        print(f"El número de teléfono de {nombre} es: {agenda_telefonica[nombre]}")
    else:
        print("Contacto no encontrado.")
    print()

def eliminar_contacto(nombre):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]
        print("Contacto eliminado exitosamente.")
    else:
        print("Contacto no encontrado.")
    print()

def mostrar_agenda():
    if not agenda_telefonica:
        print("La agenda telefónica está vacía.")
    else:
        print("Agenda Telefónica:")
        for nombre, telefono in agenda_telefonica.items():
            print(f"{nombre}: {telefono}")
    print() 


eleccion_menu()

