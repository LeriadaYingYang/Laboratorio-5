# =====================================================
# INTEGRANTE : Pablo Diaz

# Pasos      : 3 - Ingresar datos por teclado
#              4 - Escribir datos en archivo .txt

# Archivo    : contactos.txt
# =====================================================

ARCHIVO = "contactos.txt"

# PASO 3: Funciones para ingresar datos por teclado

def ingresar_nombre():
    while True:
        nombre = input("Nombre completo : ").strip()
        if nombre:
            return nombre
        print("  El nombre no puede estar vacío.")

def ingresar_telefono():
    while True:
        tel = input("Teléfono (9 dígitos): ").strip()
        if tel.isdigit() and len(tel) == 9:
            return tel
        print("  Ingrese exactamente 9 dígitos numéricos.")

def ingresar_correo():
    while True:
        correo = input("Correo electrónico: ").strip()
        if "@" in correo and "." in correo:
            return correo
        print("  Ingrese un correo válido (debe tener @ y .)")

def ingresar_contacto():
    """Reúne todos los datos del contacto por teclado."""
    print("\n--- INGRESAR NUEVO CONTACTO ---")
    nombre   = ingresar_nombre()
    telefono = ingresar_telefono()
    correo   = ingresar_correo()
    return nombre, telefono, correo


# PASO 4: Escribir los datos en archivo de texto

def escribir_contacto(nombre, telefono, correo):
    """
    Escribe el contacto en el archivo .txt.
    Modo 'a' (append) conserva los datos previos.
    """
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} | {telefono} | {correo}\n")
    # El archivo se cierra automáticamente al salir del 'with'

    print(f"\nContacto guardado correctamente en '{ARCHIVO}'.")
    print(f"  Nombre  : {nombre}")
    print(f"  Teléfono: {telefono}")
    print(f"  Correo  : {correo}\n")

def menu():
    while True:
        print("=== REGISTRO DE CONTACTOS  ===")
        print("1. Ingresar y guardar contacto")
        print("2. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre, telefono, correo = ingresar_contacto()
            escribir_contacto(nombre, telefono, correo)
        elif opcion == "2":
            print("Cerrando módulo. ¡Hasta luego!.")
            break
        else:
            print("Opción inválida.\n")

menu()
