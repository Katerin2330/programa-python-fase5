## Problema 2
# Promoción en menú de restaurante

# Matriz de productos
menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 30000],
    ["Ensalada", "Saludable", 18000],
    ["Pasta", "Italiana", 28000],
    ["Sushi", "Japonesa", 40000],
    ["Taco", "Comida Rapida", 22000]
]

# Función para calcular precio final
def calcular_precio_final(categoria, precio_base):
    
    categoria_objetivo = "Comida Rapida"
    umbral = 23000

    if categoria == categoria_objetivo and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final

# Mostrar resultados
print("PROMOCIONES DEL MENÚ")
print("-----------------------------------")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base:", precio_base)
    print("Precio Final:", precio_final)
    print("-----------------------------------")