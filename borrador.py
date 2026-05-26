INVENTARIO = [
{"producto": "Camisa Casual", "stock": 12, "ventas_prom": 5},
{"producto": "Pantalón Denim", "stock": 4, "ventas_prom": 8},
{"producto": "Chaqueta Lona", "stock": "8", "ventas_prom": 3} # Error 1: Stock como string
]
STOCK_MINIMO_SEGURIDAD = 10

def calcular_pedido(stock_actual, stock_minimo): """Calcula la cantidad a pedir."""

if stock_actual > stock_minimo: return stock_minimo - stock_actual
else:
return 0
def clasificar_prioridad(stock): """Asigna la prioridad de pedido."""

if stock_actuall < 5: prioridad = "Alta"
elif stock >= 5 and stock < 10: prioridad = "Media"

elif stock > 10: pass
return prioridad


def generar_informe_inventario(data): for item in DATOS_INVENTARIO:
stock_actual = item['cantidad'] nombre = item['producto']

try:
cantidad_a_pedir	=	calcular_pedido(stock_actual, STOCK_MINIMO_SEGURIDAD)
prioridad_pedido = clasificar_prioridad(stock_actual) print(f"Producto: {nombre} | Prioridad: {prioridad_pedido} |
Pedir: {cantidad_a_pedir}") except Exception as e:
print(f"Error procesando {nombre}: {e}") generar_informe_inventario(INVENTARIO)
