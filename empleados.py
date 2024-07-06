import json
import globales
import random

def asignar_nombres():
    empleados = [
        "Luisa Morales",
        "Javier Torres",
        "Sofia Ramirez",
        "Martin Gutierrez",
        "Valeria Castillo",
        "Diego Vargas",
        "Camila Ruiz",
        "Alejandro Medina",
        "Carolina Herrera",
        "Andres Silva",
        "Paula Ortiz",
        "Gabriel Ramos"
    ]

    todos_los_empleados = []
    for empleado in empleados:
        nombre = empleado
        sueldo = random.randint(900, 15000) * 100
        salud = sueldo * 0.7
        afp = sueldo * 0.12
        

        nuevo_empleado = {
            'nombre': nombre,
            'salud': int(salud),
            'afp' :	int(afp),
            'sueldo_liquido': int(sueldo)
        }
        
        todos_los_empleados.append(nuevo_empleado)
    
    globales.guardar_archivo_json("sueldos.json", todos_los_empleados)
    print("--Sueldos registrados--")

asignar_nombres()

