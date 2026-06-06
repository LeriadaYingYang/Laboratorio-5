ARCHIVO = "contactos.txt"
ARCHIVO_BINARIO = "contactos.dat"

# PASO 7: 
def procesar_busqueda_conteo():
    print("\n=== [PASO 7] PROCESAR DATOS: BÚSQUEDA Y CONTEO ===")
    criterio = input("Ingrese el nombre (o inicial) a buscar: ").strip().lower()
    total_registros = 0
    coincidencias = 0

    print("\n--- Resultados de la Búsqueda ---")
    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                linea = linea.replace("\t", "|")
                datos = [dato.strip() for dato in linea.split("|")]
                if len(datos) == 3:
                    total_registros += 1
                    nombre, telefono, correo = datos
                    if criterio in nombre.lower():
                        print(f" -> Encontrado: {nombre} | Tel: {telefono} | Correo: {correo}")
                        coincidencias += 1
        print("\n--- Estadísticas del Procesamiento ---")
        print(f" Total de contactos registrados evaluados: {total_registros}")
        print(f" Total de coincidencias encontradas: {coincidencias}")
    except FileNotFoundError:
        print("El archivo de texto aún no existe. No hay datos para procesar.")

# PASO 8:
def guardar_estructura_binaria():
    print("\n=== [PASO 8] GUARDANDO ESTRUCTURAS EN ARCHIVO BINARIO ===")
    lista_estructuras = []
    
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                linea = linea.replace("\t", "|")
                datos = [dato.strip() for dato in linea.split("|")]
                
                if len(datos) == 3:

                    contacto_objeto = {
                        "nombre": datos[0],
                        "telefono": datos[1],
                        "correo": datos[2]
                    }
                    lista_estructuras.append(contacto_objeto)
        with open(ARCHIVO_BINARIO, "wb") as archivo_bin:
            datos_en_texto = str(lista_estructuras)
            datos_en_bytes = datos_en_texto.encode('utf-8')
            archivo_bin.write(datos_en_bytes)    
        print(f" ¡Éxito! Se han guardado {len(lista_estructuras)} estructuras en '{ARCHIVO_BINARIO}'.")
    except FileNotFoundError:
        print("No existe el archivo de texto para migrar a binario.")
def recuperar_estructura_binaria():
    print("\n=== [PASO 8] RECUPERANDO DATOS DESDE ARCHIVO BINARIO ===")
    try:
        with open(ARCHIVO_BINARIO, "rb") as archivo_bin:
            datos_en_bytes = archivo_bin.read()
            datos_en_texto = datos_en_bytes.decode('utf-8')
            
            contactos_recuperados = eval(datos_en_texto)
        print("\n--- Estructuras recuperadas ---")
        for i, contacto in enumerate(contactos_recuperados, 1):
            print(f" Objeto [{i}] -> Nombre: {contacto['nombre']} | Teléfono: {contacto['telefono']} | Correo: {contacto['correo']}") 
    except FileNotFoundError:
        print("El archivo binario no existe. Genérelo primero con la opción 4.")
