import pickle
import os

# =====================================================
# INTEGRANTE : Juan Xavier Sánchez
# Paso 7: Implementar una función que lea los datos, los procese y los muestre.
# Paso 8: Probar con archivos binarios almacenando y recuperando datos con estructuras propias.
# ======================================================

ARCHIVO = "contactos.txt"

def ingresar_nombre():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")
def ingresar_telefono():
    while True:
        tel = input("Teléfono (9 dígitos): ").strip()
        if tel.isdigit() and len(tel) == 9: 
            return tel
        print("Ingrese exactamente 9 dígitos numéricos.")
def ingresar_correo():
    while True:
        correo = input("Correo electrónico: ").strip() 
        if "@" in correo and "." in correo:
            return correo
        print("Ingrese un correo válido.")
def ingresar_contacto():
    print("\n--- INGRESAR NUEVO CONTACTO ---")
    nombre = ingresar_nombre()
    telefono = ingresar_telefono()
    correo = ingresar_correo()
    return nombre, telefono, correo
def escribir_contacto(nombre, telefono, correo):
    with open(ARCHIVO, "a", encoding="utf-8") as archivo: 
        archivo.write(f"{nombre} | {telefono} | {correo}\n") 
    print("\nContacto guardado correctamente.")
    print(f"Nombre   : {nombre}")
    print(f"Teléfono : {telefono}")
    print(f"Correo   : {correo}\n")
def mostrar_contactos():
    print("\n=== LISTA DE CONTACTOS ===\n")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            contador = 1
            for linea in archivo:
                linea = linea.strip() 
                if not linea:
                    continue
                linea = linea.replace("\t", "|") 
                datos = [dato.strip() for dato in linea.split("|")]
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
    except FileNotFoundError:
        print("El archivo aún no existe.")
def buscar_y_procesar():
    print("\n=== BUSCAR Y CONTAR CONTACTOS ===")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            contactos = []
            for linea in archivo:
                linea = linea.strip()
                if not linea: continue
                linea = linea.replace("\t", "|")
                datos = [dato.strip() for dato in linea.split("|")]
                if len(datos) == 3:
                    contactos.append(datos)
            print(f"Se han registrado un total de {len(contactos)} contactos válidos.")
            
            termino = input("Ingrese el nombre a buscar: ").strip().lower()
            encontrados = 0
            for datos in contactos:
                if termino in datos[0].lower():
                    print(f"Encontrado: {datos[0]} | Tel: {datos[1]} | Correo: {datos[2]}")
                    encontrados += 1
            if encontrados == 0:
                print("No se encontraron coincidencias.")
    except FileNotFoundError:
        print("El archivo aún no existe.")
def manejar_binario():
    print("\n=== ARCHIVO BINARIO: INVENTARIO ===")
    archivo_bin = "inventario_frutaxa.dat"
    
    inventario = [
        {"producto": "Chips de Aguaymanto", "stock": 150, "precio": 5.50},
        {"producto": "Chips de Betarraga", "stock": 200, "precio": 4.80}
    ]
    
    print("Guardando estructura en archivo binario...")
    with open(archivo_bin, "wb") as f:
        pickle.dump(inventario, f)
    
    print("Leyendo y recuperando desde el archivo binario...")
    if os.path.exists(archivo_bin):
        with open(archivo_bin, "rb") as f:
            datos_recuperados = pickle.load(f)
            
        for item in datos_recuperados:
            print(f"- {item['producto']} | Stock: {item['stock']} | S/.{item['precio']:.2f}")

def menu():
    while True:
        print("\n====== SISTEMA DE CONTACTOS ======")
        print("1. Ingresar y guardar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar y contar contactos (Paso 7)")
        print("4. Probar archivo binario (Paso 8)")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre, telefono, correo = ingresar_contacto()
            escribir_contacto(nombre, telefono, correo)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_y_procesar()
        elif opcion == "4":
            manejar_binario()
        elif opcion == "5":
            print("Cerrando sistema... ¡Archivos liberados con éxito!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()