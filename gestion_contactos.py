ARCHIVO = "contactos.txt"
ARCHIVO_BINARIO = "contactos.dat"

#solicitar y validar nombre
def ingresar_nombre():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")

#solicitar y validar teléfono
def ingresar_telefono():
    while True:
        telefono = input("Teléfono (9 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 9:
            return telefono
        print("Ingrese exactamente 9 dígitos numéricos.")

#solicitar y validar correo electrónico
def ingresar_correo():
    while True:
        correo = input("Correo electrónico: ").strip()
        if "@" in correo and "." in correo:
            return correo
        print("Ingrese un correo válido.")

#recopilar datos completos del contacto
def ingresar_contacto():
    print("\n--- INGRESAR NUEVO CONTACTO ---")
    nombre = ingresar_nombre()
    telefono = ingresar_telefono()
    correo = ingresar_correo()
    return nombre, telefono, correo

#guardar contacto en archivo de texto
def escribir_contacto(nombre, telefono, correo):
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} | {telefono} | {correo}\n")

    print("\nContacto guardado correctamente.")
    print(f"Nombre   : {nombre}")
    print(f"Teléfono : {telefono}")
    print(f"Correo   : {correo}")

#mostrar todos los contactos registrados en forma de tabla
def mostrar_contactos():
    print("\n--- lista de contactos ---")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            contactos = []
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                datos = [dato.strip() for dato in linea.split("|")]
                if len(datos) == 3:
                    contactos.append(datos)
            if not contactos:
                print("No hay contactos registrados.")
                return

            print(f"{'ID':<5}{'Nombre':<25}{'Teléfono':<15}{'Correo'}")
            print("-" * 65)
            for i, contacto in enumerate(contactos, 1):
                print(f"{i:<5}{contacto[0]:<25}{contacto[1]:<15}{contacto[2]}")

    except FileNotFoundError:
        print("El archivo aún no existe.")

#contar contactos y buscar coincidencias por nombre
def buscar_y_procesar():
    print("\n--- buscar y contar contactos ---")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            contactos = []
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                datos = [dato.strip() for dato in linea.split("|")]
                if len(datos) == 3:
                    contactos.append(datos)
            print(f"Se han registrado un total de {len(contactos)} contactos válidos.")
            termino = input("Ingrese el nombre a buscar: ").strip().lower()
            encontrados = 0
            for contacto in contactos:
                if termino in contacto[0].lower():
                    print(
                        f"Encontrado: {contacto[0]} | Tel: {contacto[1]} | Correo: {contacto[2]}")
                    encontrados += 1
            if encontrados == 0:
                print("No se encontraron coincidencias.")
    except FileNotFoundError:
        print("El archivo aún no existe.")

# guardar contactos del archivo txt en un archivo binario
def guardar_contactos_binario():
    print("\n--- guardar contactos en binario ---")
    contactos = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                datos = [dato.strip() for dato in linea.split("|")]
                if len(datos) == 3:
                    contactos.append({
                        "nombre": datos[0],
                        "telefono": datos[1],
                        "correo": datos[2]})
        with open(ARCHIVO_BINARIO, "wb") as archivo_binario:
            archivo_binario.write(str(contactos).encode("utf-8"))
        print(f"Se guardaron {len(contactos)} contactos en {ARCHIVO_BINARIO}")
    except FileNotFoundError:
        print("El archivo de contactos aún no existe.")

#leer contactos desde el archivo binario en forma de tabla
def leer_contactos_binario():
    print("\n--- leer contactos desde binario ---")
    try:
        with open(ARCHIVO_BINARIO, "rb") as archivo_binario:
            datos_binarios = archivo_binario.read()
        datos_texto = datos_binarios.decode("utf-8")
        contactos = eval(datos_texto)
        if not contactos:
            print("No hay contactos guardados en el archivo binario.")
            return
        print(f"{'ID':<5}{'Nombre':<25}{'Teléfono':<15}{'Correo'}")
        print("-" * 65)
        for i, contacto in enumerate(contactos, 1):
            print(
                f"{i:<5}{contacto['nombre']:<25}{contacto['telefono']:<15}{contacto['correo']}")
    except FileNotFoundError:
        print("El archivo binario aún no existe.")

# verificar el archivo binario generado
def verificar_archivo_generado():
    print("\n--- verificar archivo generado ---")

    try:
        with open(ARCHIVO_BINARIO, "rb") as archivo_binario:
            datos = archivo_binario.read()

        print("Archivo encontrado correctamente.")
        print(f"Nombre del archivo: {ARCHIVO_BINARIO}")
        print(f"Contenido en bytes:")
        print(datos)
        print("\nPuedes abrir el archivo contactos.dat con un editor externo como Bloc de notas o Visual Studio Code.")

    except FileNotFoundError:
        print("El archivo binario aún no existe. Primero debe generarlo.")

#menú principal del sistema
def menu():
    while True:
        print("1. Ingresar y guardar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar y contar contactos")
        print("4. Guardar contactos en binario")
        print("5. Leer contactos desde binario")
        print("6. Verificar archivo generado")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre, telefono, correo = ingresar_contacto()
            escribir_contacto(nombre, telefono, correo)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_y_procesar()
        elif opcion == "4":
            guardar_contactos_binario()
        elif opcion == "5":
            leer_contactos_binario()
        elif opcion == "6":
            verificar_archivo_generado()
        elif opcion == "7":
            print("Cerrando sistema")
            break
        else:
            print("Opción inválida.")

#punto de entrada del programa
if __name__ == "__main__":
    menu()