print("Kevin Andres Vasquez Ocoro")
print("grupo:213022A_2201")
print("Ingeneria de Sistemas")
print("Autoria Propia")

total_encuestados = 10
datos_equipos = {} 
conteo_articulos = {"camiseta": 0, "chaqueta": 0, "gorra": 0, "morral con el logo de su equipo favorito": 0}
total_dias_estadio = 0

print("--- ENCUESTA PARA HINCHAS DE FÚTBOL COLOMBIANO ---")

for i in range(total_encuestados):
    print(f"\nEncuestado N° {i + 1}:")
    
    equipo = input("¿Cuál es su equipo favorito?: ").strip().capitalize()
    articulo = input("Artículo preferido (camiseta, chaqueta, gorra, morral con el logo de su equipo favorito): ").strip().lower()
    edad = int(input("¿Qué edad tiene?: "))
    dias_estadio = int(input("¿Cuántos días al año asiste al estadio?: "))

    if equipo not in datos_equipos:
        datos_equipos[equipo] = [0, 0] 
    datos_equipos[equipo][0] += 1
    datos_equipos[equipo][1] += edad
    if articulo in conteo_articulos:
        conteo_articulos[articulo] += 1

    total_dias_estadio += dias_estadio

print("\n" + "="*30)
print("RESULTADOS DE LA ENCUESTA")
print("="*30)

print("\nEstadísticas por Equipo:")
for equipo, datos in datos_equipos.items():
    cantidad = datos[0]
    promedio_edad = datos[1] / cantidad
    print(f"- {equipo}: {cantidad} fanático(s). Promedio de edad: {promedio_edad:.0f} años.")

articulo_mas_votado = max(conteo_articulos, key=conteo_articulos.get)
print(f"\nArtículo deportivo preferido: {articulo_mas_votado.capitalize()}")

promedio_estadio = total_dias_estadio / total_encuestados
print(f"Promedio de asistencia al estadio: {promedio_estadio:.0f} días al año.")
