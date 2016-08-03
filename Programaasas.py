from modulofinal import *
def DISENOBASE():
    import os,sys
    print("LISTO PARA DISEÑAR TU VIAJE AL CARIBE¡")
    print()
    print("1.-Modificar los puertos de salida del crucero ")
    print("2.-Modificar los categorias y precios  ")
    print("3.-Modificar los barcos ")
    print("4.-Modificar los paquetes ")
    print("5.-SALIR")
    try:
        opc=int(input("Introdusca la opcion que desea realizar :"))
    except:
        print("Esta no es una opcion valida ¡")
        print()
        DISENOBASE()
    os.system('cls')
    if opc==1:
        print("Ingrese 1 si desea anhadir un puerto ")
        print("Ingrese 2 si desea eliminar un puerto ")
        print("Ingrese 3 si desea ver los puertos ")
        print("ingrese 4 si desea modificar algun puerto ")
        try:
            abc=int(input("Introdusca la opcion que desea realizar :"))
        except:
            print("No es una opcion valida ¡")
            DISENOBASE()
        if abc==1:
            anadirpuertos()
            DISENOBASE()
        elif abc==2:
            sacarpuerto()
            DISENOBASE()
