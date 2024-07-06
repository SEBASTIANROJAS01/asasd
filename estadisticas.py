import json
import math
import globales

def promedio():
    todos_los_empleados = globales.leer_archivo_json("sueldos.json")

    suma = 0
    cantidad = 0

    for empleado in todos_los_empleados:
        suma += empleado ['sueldo_liquido']
        cantidad += 1
      
    
    average = int(suma/cantidad)

    print(f"El promedio del sueldo es: ${average}")

def media_geo():
    todos_los_empleados = globales.leer_archivo_json("sueldos.json")

    suma = 0
    cantidad = 0

    for empleado in todos_los_empleados:
        suma += math.log(empleado['sueldo_liquido'])
        cantidad += 1
    
    average = math.exp(suma/cantidad)

    print(f"La media geometrica del sueldo es: ${int(average)}")


def sueldo_mas_alto():
    todos_los_empleados = globales.leer_archivo_json("sueldos.json")

    empleados_ordenados = sorted(todos_los_empleados, key= lambda x: x['sueldo_liquido'], reverse=True)

    for empleado in empleados_ordenados[:1]:
        print(f"El sueldo liquido más alto es {empleado['nombre']}: ${empleado['sueldo_liquido']}")
        return

def sueldo_mas_bajo():
    todos_los_empleados = globales.leer_archivo_json("sueldos.json")

    empleados_ordenados = sorted(todos_los_empleados, key= lambda x: x['sueldo_liquido'], reverse=False)

    for empleado in empleados_ordenados[:1]:
        print(f"El sueldo liquido más bajo es {empleado['nombre']}: ${empleado['sueldo_liquido']}")
        return

sueldo_mas_bajo()