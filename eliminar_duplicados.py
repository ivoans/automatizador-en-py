from pathlib import Path

def es_dir(ruta):
    path = Path(ruta)
    return path.is_dir()

def eliminar_duplicados(ruta):
    """
    Elimina los archivos duplicados de una ruta.

    Se itera en todos los archivos de un directorio y se comparan por nombre y tamaño
        si coinciden, se borra el archivo duplicado.

    El parametro ruta debe ser un objeto de tipo Path(archivo o directorio).
    """
    if not es_dir(ruta):
        print("La ruta ingresada no pertenece a un directorio")
        return
    try:
        archivos_en = {}
        for files in Path(ruta).iterdir():
            if files.is_file():
                clave = (files.name, files.stat().st_size)
                if clave in archivos_en:
                    archivos_en[clave].append(files)
                else:
                    archivos_en[clave] = [files]
        for archivo in archivos_en:
            if len(archivos_en[archivo]) > 1:
                print(f"Archivos duplicados: {archivos_en[archivo]}")
                for i in range(1, len(archivos_en[archivo])):
                    archivos_en[archivo][i].unlink()
                    print(f"Archivo eliminado: {archivos_en[archivo][i].name}")
    except Exception as error:
        print(f"No se pudo leer los archivos de {ruta}: {error}")