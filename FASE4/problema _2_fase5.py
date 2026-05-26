def clasificar_jornada(horas):

    total = sum(horas)

    if total > 40:

        return total, "Sobretiempo"

    else:

        return total, "Horario Estándar"

matriz = [

    ["Ana", 8, 8, 8, 8, 8],

    ["Luis", 9, 8, 9, 8, 8],

    ["María", 7, 8, 8, 7, 8],

    ["Carlos", 10, 9, 8, 9, 8]

]

for recurso in matriz:

    nombre = recurso[0]

    horas = recurso[1:]

    total, clasificacion = clasificar_jornada(horas)

    print("Recurso:", nombre)

    print("Total de horas:", total)

    print("Clasificación:", clasificacion)

    print()