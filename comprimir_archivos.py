from PIL import Image
from pathlib import Path


def es_dir(ruta):
    path = Path(ruta)
    return path.is_dir()

def compresor_img(ruta):
    """
    Comprime las imagenes de una ruta.

    El parametro ruta debe ser un objeto de tipo Path(archivo o directorio).

    Las imagenes se comprimen con calidad 60 y se guardan con el prefijo "compressed_".

    """
    path = Path(ruta)
    if not es_dir(path):
        print("La ruta ingresada no pertenece a un directorio")
        return
    try:
        for archivo in path.iterdir():
            if archivo.is_file() and archivo.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                img = Image.open(archivo)
                ruta_comprimida = path / f"compressed_{archivo.name}"
                img.save(ruta_comprimida , optimize=True, quality=60)
                img.close()
                if ruta_comprimida.exists():
                    archivo.unlink()
                    print(f"Imagen comprimida: {archivo.name} -> {ruta_comprimida.name}")
                else:
                    print(f"No se pudo comprimir {archivo.name}")
    except Exception as error:
        print(f"No se pudo leer los archivos de {path}: {error}")