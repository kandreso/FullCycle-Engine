print("Kevin Andres Vasquez Ocoro")
print("grupo:213022A_2201")
print("Ingeneria de Sistemas")
print("Autoria Propia")

matriz_a = [
    [5, 8, 4],  
    [6, 3, 7],  
    [4, 5, 5],  
    [2, 9, 6]   
]

matriz_b = [
    [10, 12, 15], 
    [11, 20, 10], 
    [15, 15, 12], 
    [25, 10, 18]  
]

filas = 4
columnas = 3
matriz_c = []

for i in range(filas):
    fila_nueva = []
    for j in range(columnas):
        tiempo_total = matriz_a[i][j] * matriz_b[i][j]
        fila_nueva.append(tiempo_total)
    matriz_c.append(fila_nueva)


print("MATRIZ C: Tiempo total trabajado por cada empleado cada día.")
for i in range(filas):
    print(f"Empleado {i+1}:")
    for j in range(columnas):
        print(f"  Día {j+1}: {matriz_c[i][j]} minutos")
print("-" * 50)


totales_empleados = []
for i in range(filas):
    suma_empleado = sum(matriz_c[i])
    totales_empleados.append(suma_empleado)

max_tiempo_emp = max(totales_empleados)
indice_emp = totales_empleados.index(max_tiempo_emp)

print(f"RESULTADO: El empleado que acumuló más tiempo fue el Empleado {indice_emp + 1}")
print(f"Total: {max_tiempo_emp} minutos sumando sus tres días.")
print("-" * 50)

totales_dias = []
for j in range(columnas):
    suma_dia = 0
    for i in range(filas):
        suma_dia += matriz_c[i][j]
    totales_dias.append(suma_dia)

max_tiempo_dia = max(totales_dias)
indice_dia = totales_dias.index(max_tiempo_dia)

print(f"RESULTADO: El día que registró el mayor tiempo total fue el Día {indice_dia + 1}")
print(f"Total del equipo ese día: {max_tiempo_dia} minutos.")
