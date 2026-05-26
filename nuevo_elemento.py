print("** Calculadora de Productos **")
IVA = 0.19
RECARGO = 0.05

while True:
    entrada = input("\nIngrese el precio del producto: ")
    
    if entrada.lower() == "fin":
        break
    
    try:
        precio = float(entrada)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if precio <= 0:
        print("Error")
        exit()

    # Lógica de categorías y asignación de tasa de impuesto
    if precio >= 100.000: 
        categoria = "Lujo"
        tasa = IVA + RECARGO
        print(f"{categoria}: Aplica IVA 19% + Lujo 5%")
    elif precio >= 50.000:
        categoria = "Estandar"
        tasa = IVA
        print(f"{categoria}: Aplica IVA 19%")
    else:
        precio < 50.000 
        categoria = "Basico"
        tasa = 0
        print(f"{categoria}")
        
        # AQUÍ EL CAMBIO: Multiplicamos por la tasa correspondiente
    valor_final = precio * (1 + tasa)
    print(f"Subtotal con impuestos: ${valor_final:,.2f}")
print("-" * 30)



# Constante
IVA = 0.19
RECARGO_LUJO = 0.05

# Solicitar precio del producto
precio = float(input("Ingrese el precio del producto: "))

if precio <= 0:
    print("Error: precio inválido.")
else:
    # Solicitar categoría
    print("Categorías: 1 = Básico, 2 = Estándar, 3 = Lujo")
    categoria = int(input("Ingrese el código de categoría: "))

    if categoria == 1:
        # Producto básico: no paga IVA
        valor_final = precio
    elif categoria == 2:
        # Producto estándar: paga IVA
        valor_final = precio * (1 + IVA)
    elif categoria == 3:
        # Producto de lujo: paga IVA + recargo
        valor_final = precio * (1 + IVA + RECARGO_LUJO)
    else:
        print("Error: categoría inválida.")
        exit()

    print(f"El valor final del producto es: {valor_final:.2f}")