import os
import globales
import empleados
import estadisticas
os.system("cls")

def menu_estadisticas():
    while True:
        os.system("cls")
        print("1. Sueldo líquido más alto.")
        print("2. Sueldo líquido más bajo.")
        print("3. Promedio de sueldos líquido.")
        print("4. Media geométrica sueldo líquido")
        print("5. Salir")

        opciones = globales.seleccionar_opcion(5)

        if opciones == 1:
            estadisticas.sueldo_mas_alto()
        elif opciones == 2:
            estadisticas.sueldo_mas_bajo()
        elif opciones == 3:
            estadisticas.promedio()
        elif opciones == 4:
            estadisticas.media_geo()
        elif opciones == 5:
            print("Saliendo.")
            return

        input()

def menu_general():
    while True:
        os.system("cls")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")

        opciones = globales.seleccionar_opcion(3)

        if opciones == 1:
            empleados.asignar_nombres()
        elif opciones == 2:
            menu_estadisticas()
        elif opciones == 3:
            print("3. Salir.")
            return

        input()


menu_general()