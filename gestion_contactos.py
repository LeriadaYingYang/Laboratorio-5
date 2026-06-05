# =====================================================
# INTEGRANTE : Fabrizio Ortega
# Paso 5: Leer y mostrar el contenido del archivo línea por línea.
# Paso 6: Modificar el sistema para añadir nuevos registros sin sobrescribir los anteriores.
# ======================================================

ARCHIVO = "contactos.txt"

# 4 funciones utilizadas anteriormente 
# Función para ingresar el nombre
def ingresar_nombre():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")

# Función para ingresar el teléfono
def ingresar_telefono():
    while True:
        tel = input("Teléfono (9 dígitos): ").strip()
        if tel.isdigit() and len(tel) == 9: 
            return tel
        print("Ingrese exactamente 9 dígitos numéricos.")

# Función para ingresar el correo electrónico
def ingresar_correo():
    while True:
        correo = input("Correo electrónico: ").strip() 
        if "@" in correo and "." in correo:
            return correo
        print("Ingrese un correo válido.")

#Función para ingresar un nuevo contacto
def ingresar_contacto():
    print("\n--- INGRESAR NUEVO CONTACTO ---")
    nombre = ingresar_nombre()
    telefono = ingresar_telefono()
    correo = ingresar_correo()
    return nombre, telefono, correo


# Paso 6: Modificar el sistema para añadir nuevos registros sin sobrescribir los anteriores.
def escribir_contacto(nombre, telefono, correo):
    with open(ARCHIVO, "a", encoding="utf-8") as archivo: 
        archivo.write(f"{nombre} | {telefono} | {correo}\n") 
    print("\nContacto guardado correctamente.")
    print(f"Nombre   : {nombre}")
    print(f"Teléfono : {telefono}")
    print(f"Correo   : {correo}\n")

# Paso 5: Leer y mostrar el contenido del archivo línea por línea.
def mostrar_contactos():
    print("\n=== LISTA DE CONTACTOS ===\n")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            contador = 1
            for linea in archivo:
                linea = linea.strip() # Elimina espacios y saltos de línea
                if not linea: # Ignora líneas vacías
                    continue
                linea = linea.replace("\t", "|") # Reemplaza tabulaciones por barras verticales
                datos = [dato.strip() for dato in linea.split("|")] # Divide los datos y elimina espacios extra
                if len(datos) == 3:
                    nombre, telefono, correo = datos
                    print(f"CONTACTO {contador}")
                    print(f"Nombre   : {nombre}")
                    print(f"Teléfono : {telefono}")
                    print(f"Correo   : {correo}")
                    print("-----------------------------")
                    contador += 1
                else:
                    print(f"Línea con formato incorrecto: {linea}")
    except FileNotFoundError: # Si el archivo no existe, se muestra un mensaje
        print("El archivo aún no existe.")

def menu():
    while True:
        print("\n====== SISTEMA DE CONTACTOS ======")
        print("1. Ingresar y guardar contacto")
        print("2. Mostrar contactos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre, telefono, correo = ingresar_contacto()
            escribir_contacto(nombre, telefono, correo)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida.")
menu()