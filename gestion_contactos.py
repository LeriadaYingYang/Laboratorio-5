def registrar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

    while len(telefono) != 9:
        print("Teléfono inválido")
        telefono = input("Teléfono (9 digitos): ")

    archivo = open("contactos.txt", "a")
    archivo.write(nombre + "," + telefono + "," + correo + "\n")
    archivo.close()

    print("Contacto registrado")

def mostrar_contactos():
    try:
        archivo = open("contactos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for l in lineas:
            datos = l.strip().split(",")
            print("Nombre: ", datos[0], "| Teléfono:", datos[1], "| Correo:", datos[2])

    except: 
        print("No existe el archivo")

## Menu principal
while True:
    print("\n ------- MENU DE CONTACTOS -------")
    print("1. Registrar contacto")
    print("2. Mostrar contactos")
    print("3. Salir")

    opcion  = input("Elija una opción:")
    if opcion == "1":
        registrar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")