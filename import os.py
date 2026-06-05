import os
import pickle

# =====================================================
# INTEGRANTES : Sánchez Muñoz Juan Xavier
# Paso 7 y 8: Procesar, buscar y usar archivos binarios. 
# ======================================================

def buscar_y_contar_contactos():
    print("\n=== PROCESAMIENTO Y BÚSQUEDA DE CONTACTOS ===")
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lista_datos = []
            for linea in archivo:
                linea = linea.strip()
                if not linea: continue
                linea = linea.replace("\t", "|")
                datos = [dato.strip() for dato in linea.split("|") if dato.strip()]
                # El archivo txt original tiene un salto de línea en Pedro Salazar, 
                # esta validación asegura que solo procesemos líneas completas.
                if len(datos) == 3:
                    lista_datos.append(datos)
            
            print(f"📊 Total de contactos válidos registrados: {len(lista_datos)}")
            
            termino = input("Ingrese el nombre del contacto a buscar: ").strip().lower()
            encontrados = 0
            
            for datos in lista_datos:
                nombre, telefono, correo = datos
                if termino in nombre.lower():
                    print(f"\n✅ ENCONTRADO:")
                    print(f"Nombre   : {nombre}")
                    print(f"Teléfono : {telefono}")
                    print(f"Correo   : {correo}")
                    encontrados += 1
            
            if encontrados == 0:
                print("\n❌ No se encontraron contactos con ese nombre.")
    except FileNotFoundError:
        print("El archivo aún no existe. Guarde un contacto primero.")
def probar_archivo_binario():
    print("\n=== PRUEBA DE ARCHIVO BINARIO (INVENTARIO) ===")

    inventario = [
        {"sku": "FRT-001", "producto": "Chips de Aguaymanto Deshidratado", "stock": 150, "precio": 5.50},
        {"sku": "FRT-002", "producto": "Chips de Betarraga Crujiente", "stock": 200, "precio": 4.80},
        {"sku": "FRT-003", "producto": "Mix Frutaxa Energy", "stock": 85, "precio": 7.00}
    ]
    
    print("💾 Empaquetando estructura de inventario en archivo binario...")
    with open(ARCHIVO_BINARIO, "wb") as archivo_bin:
        pickle.dump(inventario, archivo_bin)
    print("¡Archivo 'inventario_binario.dat' creado y guardado con éxito!")
    
    print("\n📂 Recuperando datos desde el binario...")
    if os.path.exists(ARCHIVO_BINARIO):
        with open(ARCHIVO_BINARIO, "rb") as archivo_bin:
            datos_recuperados = pickle.load(archivo_bin)
            
        print(f"\n{'SKU':<8} | {'PRODUCTO':<35} | {'STOCK':<5} | {'PRECIO'}")
        print("-" * 65)
        for item in datos_recuperados:
            print(f"{item['sku']:<8} | {item['producto']:<35} | {item['stock']:<5} | S/.{item['precio']:.2f}")
    else:
        print("Error: No se encontró el archivo binario.")


# --- MENÚ ACTUALIZADO ---
def menu():
    while True:
        print("\n====== SISTEMA DE CONTACTOS E INVENTARIO ======")
        print("1. Ingresar y guardar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar y contar contactos (Punto 7)")
        print("4. Probar archivo binario (Punto 8)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre, telefono, correo = ingresar_contacto()
            escribir_contacto(nombre, telefono, correo)
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_y_contar_contactos()
        elif opcion == "4":
            probar_archivo_binario()
        elif opcion == "5":
            print("Cerrando sistema... Archivos cerrados de manera segura.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
