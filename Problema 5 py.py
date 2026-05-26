# Matriz con nombre y horas trabajadas de lunes a viernes
recursos = [
    ["Carlos", 8, 8, 9, 8, 10],
    ["Ana", 7, 8, 8, 7, 8],
    ["Luis", 9, 9, 8, 9, 9],
    ["María", 6, 7, 6, 7, 6]
]

# Función para calcular total y clasificación
def calcular_jornada(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion

# Mostrar resultados
print("REPORTE DE HORAS SEMANALES\n")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_jornada(horas)

    print("Nombre:", nombre)
    print("Total Horas:", total)
    print("Clasificación:", clasificacion)
    print("---------------------------")