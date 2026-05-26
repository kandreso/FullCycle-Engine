print("Kevin Andres Vasquez Ocoro")
print("grupo:213022A_2201")
print("Ingeneria de sistemas")

print("** Calculadora de Productos **")
IVA = 0.19
precio_base = float(input("Ingrese el precio del producto: "))
    
if precio_base <= 0:
    print("Error.")
else:
    print("Categorías: 1 = Producto Básico, 2 = Producto Estándar, 3 = Producto de Lujo")
    categoria = int(input("Ingrese el código de categoría: "))

    if categoria == 1:
        print("*** No paga Iva ***")
        valor_final = precio_base 
    elif categoria == 2:
        print("*** Paga IVA del 19%. ***")
        valor_final = precio_base * (1 + IVA)
    elif categoria == 3:
        print("*** Paga IVA del 19% + recargo del 5%. ***")
        valor_final = precio_base * (1 + IVA + 0.05 )
    else:
        print("Error: categoría inválida.")
        exit()
    print(f"El valor final del producto es: {valor_final:.2f}")
