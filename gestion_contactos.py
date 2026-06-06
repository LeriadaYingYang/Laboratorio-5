# ==============================================================================
# SISEstudiante: Juan Xavier Sánchez 
# Parte 7 y 8, laboratorio 5
# ==============================================================================

ARCHIVO_TXT = "contactos.txt"
ARCHIVO_DAT = "contactos.dat"

# PASO 3: Funciones de entrada
def ingresar_nombre():
    while True:
        nombre = input("Nombre completo: ").strip()
        if nombre: return nombre
        print("El nombre no puede estar vacío.")

def ingresar_telefono():
    while True:
        tel = input("Teléfono (9 dígitos): ").strip()
        if tel.isdigit() and len(tel) == 9: return tel
        print("Ingrese exactamente 9 dígitos.")

def ingresar_correo():
    while True:
        correo = input("Correo electrónico: ").strip()
        if "@" in correo and "." in correo: return correo
        print("Ingrese un correo válido.")

# PASO 4 y 6: Escritura y adición
def escribir_contacto():
    nombre, tel, correo = ingresar_nombre(), ingresar_telefono(), ingresar_correo()
    with open(ARCHIVO_TXT, "a", encoding="utf-8") as f:
        f.write(f"{nombre} | {tel} | {correo}\n")
    print("\n[+] Contacto registrado con éxito.")

# PASO 5: Lectura línea por línea ---
def mostrar_contactos():
    print("\n--- LISTA DE CONTACTOS (.txt) ---")
    try:
        with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
            for i, linea in enumerate(f, 1):
                print(f"{i}. {linea.strip()}")
    except FileNotFoundError:
        print("[!] El archivo no existe aún.")

# PASO 7: Procesamiento (Búsqueda y Conteo) 
def procesar_datos():
    criterio = input("Buscar nombre: ").strip().lower()
    total, encontrados = 0, 0
    try:
        with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
            for linea in f:
                datos = [d.strip() for d in linea.split("|")]
                if len(datos) == 3:
                    total += 1
                    if criterio in datos[0].lower():
                        print(f" -> {datos[0]} | {datos[1]} | {datos[2]}")
                        encontrados += 1
        print(f"\nResultados: Evaluados {total}, Encontrados {encontrados}")
    except FileNotFoundError:
        print("[!] No hay datos para procesar.")

# PASO 8: Archivo Binario (Persistencia de estructuras)
def guardar_binario():
    lista = []
    try:
        with open(ARCHIVO_TXT, "r", encoding="utf-8") as f:
            for linea in f:
                d = [x.strip() for x in linea.split("|")]
                if len(d) == 3:
                    lista.append({"nom": d[0], "tel": d[1], "cor": d[2]})
        
        # Guardado binario nativo: convertir a string y codificar a bytes
        with open(ARCHIVO_DAT, "wb") as f:
            f.write(str(lista).encode('utf-8'))
        print(f"[+] {len(lista)} registros migrados a binario.")
    except FileNotFoundError:
        print("[!] Error: No hay archivo TXT para migrar.")

def leer_binario():
    try:
        with open(ARCHIVO_DAT, "rb") as f:
            # Reconstrucción del objeto desde bytes
            datos = eval(f.read().decode('utf-8'))
            for c in datos:
                print(f"Nombre: {c['nom']} | Tel: {c['tel']}")
    except FileNotFoundError:
        print("[!] Error: No existe el archivo binario.")

# MENÚ PRINCIPAL 
def menu():
    while True:
        print("\n=== SISTEMA DE GESTIÓN ===")
        print("1. Registrar | 2. Listar | 3. Buscar/Contar | 4. Migrar a DAT | 5. Leer DAT | 6. Salir")
        op = input("Opción: ")
        if op == "1": escribir_contacto()
        elif op == "2": mostrar_contactos()
        elif op == "3": procesar_datos()
        elif op == "4": guardar_binario()
        elif op == "5": leer_binario()
        elif op == "6": print("Saliendo..."); break

if __name__ == "__main__":
    menu()
