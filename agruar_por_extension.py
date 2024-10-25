from pathlib import Path

def es_dir(ruta):
    path = Path(ruta)
    return path.is_dir()

def agrupar_por_extension(ruta):
    """
    Agrupa los archivos de una ruta por su extensión.

    El parametro ruta debe ser un objeto de tipo Path(archivo o directorio).

    Retorna un diccionario con las extensiones como llave y una lista de 
        nombres de archivos como valor.
    """
    path = Path(ruta)
    if not es_dir(path):
        print(f"{path} no es un directorio")
        return{}
    try:
        archivos = {}
        for archivo in path.iterdir():
            if archivo.is_file():
                extension = archivo.suffix
                if extension not in archivos:
                    archivos[extension] = []
                archivos[extension].append(archivo.name)
    except Exception as error:
        print(f"No se pudo leer los archivos de {path}: {error}")
        return {}
    
    return archivos


def mover_archivos(ruta):
    """
    Crea una carpeta por cada extensión de archivo o si la carpeta ya existe
        mueve los archivos con esa extensión a la carpeta correspondiente.

    El parametro ruta debe ser un objeto de tipo Path(archivo o directorio).
    """
    path = Path(ruta)
    archivos = agrupar_por_extension(path)

    for extension, nombres in archivos.items():
        carpeta = path / extension[1:]
        try:
            carpeta.mkdir(exist_ok=True)
        except Exception as error:
            print(f"No se pudo crear la carpeta {carpeta}: {error}")
            continue

        for nombre in nombres:
            ruta_archivo = path / nombre
            ruta_destino = carpeta / nombre
            try:
                ruta_archivo.rename(ruta_destino)
            except Exception as error:
                print(f"No se pudo mover {ruta_archivo} a {ruta_destino}: {error}")
                continue
        print(f"Se movieron {len(nombres)} archivos a {carpeta}")

# Se puede agregar una funcionalidad para que los archivos se muevan a una carpeta ya definida como la de fotos, videos, etc.
