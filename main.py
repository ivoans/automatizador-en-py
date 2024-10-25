from agruar_por_extension import mover_archivos
from comprimir_archivos import compresor_img
from eliminar_duplicados import eliminar_duplicados
from agrupar_por_fecha import crear_carpeta


def main():
    print("Ingrese que desea realizar:\n1. Comprimir archivos\n2. Eliminar archivos duplicados\n3. Agrupar archivos por fecha\n4. Agrupar archivos por extension\n5. Salir")
    accion = 0
    while accion < 1 or accion > 5:
        accion = int(input())
        if accion < 1 or accion > 5:
            print("Opcion no valida, intente de nuevo")
    print("\033[H\033[J")
    
    while accion != 5:
        print("Ingrese que desea realizar:\n1. Comprimir archivos\n2. Eliminar archivos duplicados\n3. Agrupar archivos por fecha\n4. Agrupar archivos por extension\n5. Salir")
        if accion == 1:
            print("Comprimir archivos")
            ruta = input("Ingrese la ruta del directorio: ")
            print(f"Estas seguro que {ruta} es la ruta correcta? (s/n)")
            confirmacion = input()
            if confirmacion.lower() == "s":
                compresor_img(ruta)
            else:
                print("Salir")
        elif accion == 2:
            print("Eliminar archivos duplicados")
            ruta = input("Ingrese la ruta del directorio: ")
            print(f"Estas seguro que {ruta} es la ruta correcta? (s/n)")
            confirmacion = input()
            if confirmacion.lower() == "s":
                eliminar_duplicados(ruta)
            else:
                print("Salir")
        elif accion == 3:
            print("Agrupar archivos por fecha")
            ruta = input("Ingrese la ruta del directorio: ")
            print(f"Estas seguro que {ruta} es la ruta correcta? (s/n)")
            confirmacion = input()
            if confirmacion.lower() == "s":
                crear_carpeta(ruta)
            else:
                print("Salir")
        elif accion == 4:
            print("Agrupar archivos por extension")
            ruta = input("Ingrese la ruta del directorio: ")
            print(f"Estas seguro que {ruta} es la ruta correcta? (s/n)")
            confirmacion = input()
            if confirmacion.lower() == "s":
                mover_archivos(ruta)
            else:
                print("Salir")
        else:
            print("Salir")
        print("\033[H\033[J")


if __name__ == "__main__":
    main()