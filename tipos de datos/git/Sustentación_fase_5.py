

import sys
def cargar_videoteca():
    """Devuelve la lista de títulos de la videoteca."""
    return [
        ["El Origen", 2010, 9.0, "Ciencia ficción"],
        ["La Gran Aventura", 2021, 8.5, "Acción"],
        ["Misterio Nocturno", 2018, 7.2, "Suspense"],
        ["Ritmo del Corazón", 2023, 9.2, "Romance"],
        ["Tecnología Extrema", 2022, 8.0, "Documental"],
        ["Risas en la Ciudad", 2019, 6.8, "Comedia"],
        ["Viaje Interplanetario", 2024, 9.5, "Aventura"],
    ]


def solicitar_umbral_calificacion():
    """Pide al usuario el umbral mínimo de calificación."""
    while True:
        try:
            valor = float(input("Ingrese el umbral de calificación mínima (1.0 - 10.0): "))
            if 1.0 <= valor <= 10.0:
                return valor
            print("ERROR: La calificación debe estar entre 1.0 y 10.0.")
        except ValueError:
            print("ERROR: Ingrese un número válido para la calificación.")


def solicitar_anio_minimo():
    """Pide al usuario el año mínimo para la auditoría."""
    while True:
        try:
            valor = int(input("Ingrese el año mínimo (por ejemplo, 2000): "))
            if valor > 0:
                return valor
            print("ERROR: Ingrese un año válido mayor que 0.")
        except ValueError:
            print("ERROR: Ingrese un número entero válido para el año.")


def solicitar_opcion_inicial():
    """Pide al usuario seleccionar la opción de preferencia."""
    print("+-----------------------------------------------------+")
    print("|   **** Seleccione la opción de preferencia   ****   |")
    print("+-----------+-----------------------------------------+")
    print("| Opción    |           Descripción                   |")
    print("+-----------+-----------------------------------------+")
    print("| 1         | Ver lista de la audioteca               |")
    print("| 2         | Continuar con la auditoría              |")
    print("| 3         | Salir y cerrar programa                 |")
    print("+-----------+-----------------------------------------+\n")

    while True:
        respuesta = input("Ingrese 1, 2 o 3: ").strip()
        if respuesta in {"1", "2", "3"}:
            return respuesta
        print("ERROR: Seleccione 1, 2 o 3.")


def mostrar_lista_videoteca(videoteca):
    """Muestra la lista completa de la videoteca en una tabla ordenada."""
    ancho_titulo = 30
    ancho_anio = 6
    ancho_calificacion = 12
    ancho_genero = 16
    ancho_total = ancho_titulo + ancho_anio + ancho_calificacion + ancho_genero + 15

    print("\n=== Lista de la audioteca ===")
    print("+" + "-" * (ancho_total - 2) + "+")
    print(
        f"| {'Título':<{ancho_titulo}} | {'Año':^{ancho_anio}} | {'Calificación':^{ancho_calificacion}} | {'Género':<{ancho_genero}} |"
    )
    print("+" + "=" * (ancho_total - 2) + "+")
    for titulo, anio, calificacion, genero in videoteca:
        print(
            f"| {titulo:<{ancho_titulo}} | {anio:^{ancho_anio}} | {calificacion:^{ancho_calificacion}.1f} | {genero:<{ancho_genero}} |"
        )
    print("+" + "-" * (ancho_total - 2) + "+")
    print()


def contar_titulos_populares_recientes(videoteca, umbral_calificacion, anio_minimo):
    """Cuenta los títulos que cumplen con la calificación y el año mínimo."""
    conteo = 0
    for titulo, anio, calificacion, genero in videoteca:
        if calificacion >= umbral_calificacion and anio >= anio_minimo:
            conteo += 1
    return conteo


def obtener_titulos_filtrados(videoteca, umbral_calificacion, anio_minimo):
    """Devuelve los títulos que cumplen los criterios de auditoría."""
    return [
        titulo
        for titulo, anio, calificacion, genero in videoteca
        if calificacion >= umbral_calificacion and anio >= anio_minimo
    ]


def mostrar_resultado(videoteca, umbral_calificacion, anio_minimo, conteo, titulos):
    """Muestra el resultado de la auditoría en pantalla."""
    print("\n=== Auditoría de Videoteca ===")
    print(f"Umbral de calificación mínima: {umbral_calificacion}")
    print(f"Año mínimo: {anio_minimo}")
    print(f"Cantidad de títulos aprobados: {conteo}")
    if titulos:
        print("Títulos que cumplen los criterios:")
        for titulo in titulos:
            print(f"- {titulo}")
    else:
        print("No hay títulos que cumplan los criterios seleccionados.")


def solicitar_otra_consulta():
    """Pregunta al usuario si desea realizar otra auditoría o salir."""
    while True:
        respuesta = input("\n¿Desea otra consulta? (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("ERROR: Responda con 's' para sí o 'n' para no.")


def repetir_mensaje(mensaje, veces):
    """Imprime un mensaje repetido la cantidad de veces indicada."""
    for _ in range(veces):
        print(mensaje)


def finalizar_programa():
    """Muestra el mensaje de despedida."""
    print("\nGracias por usar el sistema de auditoría. Hasta luego.")


def main():
    print("\n=== sistemas de auditoria-videoteca. ===\n")
    videoteca = cargar_videoteca()

    while True:
        opcion = solicitar_opcion_inicial()
        if opcion == "1":
            mostrar_lista_videoteca(videoteca)
        elif opcion == "3":
            print("Saliendo del programa...")
            finalizar_programa()
            sys.exit(0)

        umbral_calificacion = solicitar_umbral_calificacion()
        anio_minimo = solicitar_anio_minimo()

        conteo = contar_titulos_populares_recientes(videoteca, umbral_calificacion, anio_minimo)
        titulos = obtener_titulos_filtrados(videoteca, umbral_calificacion, anio_minimo)

        mostrar_resultado(videoteca, umbral_calificacion, anio_minimo, conteo, titulos)

        if solicitar_otra_consulta():
            continue
        finalizar_programa()
        break


if __name__ == "__main__":
    main()
print("end")
