from pathlib import Path
from datetime import datetime

def es_dir(ruta):
    path = Path(ruta)
    return path.is_dir()

def agrupar_por_fecha(ruta):
    """
    Agrupa los archivos de un directorio por fecha de modificacion,
        por mes y año
    """
    archivos = {}
    if not es_dir(ruta):
        print(f"{ruta} no es un directorio")
        return {}
    for archivo in Path(ruta).iterdir():
        if archivo.is_file():
            fecha = archivo.stat().st_mtime   # st_mine retorna la fecha que se modifico el archivo (en segundos) 
            fecha = datetime.fromtimestamp(fecha)  # convierte la los segundos a una fecha legible(objeto datetime)
            fecha = fecha.strftime("%B %Y")    # retorna la fecha en formato mes año
            if fecha not in archivos:
                archivos[fecha] = []
            archivos[fecha].append(archivo.name)
    return archivos


def crear_carpeta(ruta):
    """
    Crea una carpeta por cada fecha de modificacion de los archivos.
    Mueve los archivos a la carpeta correspondiente.
    """
    path = Path(ruta)
    if not es_dir(path):
        print(f"{path} no es un directorio")
        return
    archivos = agrupar_por_fecha(path)
    for fecha, nombres in archivos.items():
        carpeta = path / fecha.replace(" ", "_").lower()
        try:
            carpeta.mkdir(exist_ok=True)
        except Exception as error:
            print(f"No se pudo crear la carpeta {carpeta}: {error}")
            continue
        for nombre in nombres:
            ruta_archivo = path / nombre
            ruta_destino = carpeta / nombre
            try:
                if not ruta_destino.exists():
                    ruta_archivo.rename(ruta_destino)
                    print(f"Se movio {ruta_archivo} a {ruta_destino}")
                else:
                    print(f"El archivo {ruta_destino} ya existe")
            except Exception as error:
                print(f"No se pudo mover {ruta_archivo} a {ruta_destino}: {error}")
                continue

