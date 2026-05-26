import tkinter as tk
from tkinter import messagebox

# Constante de IVA
IVA = 0.19

def calcular_valor():
    try:
        precio_base = float(entry_precio.get())
        if precio_base <= 0:
            messagebox.showerror("Error", "El precio debe ser mayor que cero.")
            return
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor numérico válido para el precio.")
        return

    categoria = categoria_var.get()

    if categoria == 1:
        valor_final = precio_base
    elif categoria == 2:
        valor_final = precio_base * (1 + IVA)
    elif categoria == 3:
        valor_final = precio_base * (1 + IVA + 0.05)
    else:
        messagebox.showerror("Error", "Código de categoría inválido.")
        return

    messagebox.showinfo("Resultado", f"El valor final del producto es: ${valor_final:.2f}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Valor Final de Producto")

# Etiqueta y entrada para precio
tk.Label(ventana, text="Precio base:").grid(row=0, column=0, padx=10, pady=10)
entry_precio = tk.Entry(ventana)
entry_precio.grid(row=0, column=1, padx=10, pady=10)

# Selección de categoría
tk.Label(ventana, text="Categoría:").grid(row=1, column=0, padx=10, pady=10)
categoria_var = tk.IntVar()

tk.Radiobutton(ventana, text="Básico (sin IVA)", variable=categoria_var, value=1).grid(row=1, column=1, sticky="w")
tk.Radiobutton(ventana, text="Estándar (IVA 19%)", variable=categoria_var, value=2).grid(row=2, column=1, sticky="w")
tk.Radiobutton(ventana, text="Lujo (IVA 19% + 5%)", variable=categoria_var, value=3).grid(row=3, column=1, sticky="w")

# Botón de cálculo
tk.Button(ventana, text="Calcular", command=calcular_valor).grid(row=4, column=0, columnspan=2, pady=20)

ventana.mainloop()