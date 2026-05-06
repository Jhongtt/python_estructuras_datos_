#Módulo 05 · Avanzado
#Comprehensions
#Sintaxis concisa para crear colecciones en una línea. Hasta 40% más rápidas que bucles equivalentes.

#ejemplo 1

# Bucle tradicional
cuadrados = []
for n in range(10):
    cuadrados.append(n**2)

# List comprehension — equivalente más conciso
cuadrados = [n**2 for n in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Con filtro
pares = [n for n in range(10) if n%2 == 0]
# [0, 2, 4, 6, 8]

# Transformación + extracción
celsius = [0, 10, 20, 30, 40]
fahr = [(9/5)*t + 32 for t in celsius]

usuarios = [{"nombre":"Ana","edad":28},{"nombre":"Carlos","edad":35}]
nombres = [u["nombre"] for u in usuarios]  # ['Ana','Carlos']


#ejemplo 2

# Cuadrados
cuadrados = {n: n**2 for n in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Filtrar stock disponible
stock = {"manzanas":10,"platanos":3,"naranjas":25,"peras":0}
disponibles = {f:c for f,c in stock.items() if c > 0}

# Invertir diccionario
original  = {"a":1, "b":2, "c":3}
invertido = {v:k for k,v in original.items()}  # {1:"a", 2:"b", 3:"c"}

# Desde lista de dicts
estudiantes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Carlos"}]
id_nombre = {e["id"]: e["nombre"] for e in estudiantes}

#ejemplo 3

# Eliminar duplicados con transformación
numeros = [1,2,2,3,4,3,5,5,1]
unicos  = {n for n in numeros}  # {1,2,3,4,5}

# Iniciales únicas
palabras   = ["manzana","banana","mango","mora","naranja"]
iniciales  = {p[0] for p in palabras}  # {'m','b','n'}

# Vocales únicas en un texto
texto  = "python es un lenguaje versátil"
vocales = {l for l in texto.lower() if l in "aeiou"}

# Filtro: cuadrados de pares únicos
pares_cuad = {n**2 for n in range(10) if n%2==0}
# {0, 4, 16, 36, 64}


#ejemplo 4

ventas = [
    {"producto":"laptop",  "unidades":20, "precio":800},
    {"producto":"teclado", "unidades":50, "precio":25},
    {"producto":"mouse",   "unidades":30, "precio":15},
    {"producto":"monitor", "unidades":10, "precio":200}
]
# List comp: valor total por producto
valor_por_producto = [i["unidades"]*i["precio"] for i in ventas]
# [16000, 1250, 450, 2000]

# List comp con filtro: alto valor
alto_valor = [i["producto"] for i in ventas
              if i["unidades"]*i["precio"] > 1000]
# ['laptop','teclado','monitor']

# Dict comp: nombre → valor total
resumen = {i["producto"]: i["unidades"]*i["precio"] for i in ventas}

# Gran total
gran_total = sum(valor_por_producto)  # 19700

#ejemplo 5

# Comprehension simple — legible y eficiente
cuadrados = [n**2 for n in range(100)]

# Generador para colecciones grandes — ahorra memoria
gen = (n**2 for n in range(1_000_000))
primero = next(gen)  # solo calcula uno a la vez

# Cuándo usar bucle tradicional — lógica compleja
#resultados = []
#for item in datos:
 #   if item["activo"]:
  #      valor = calcular(item)
    #    if valor > umbral:
     #       resultados.append(transformar(valor))
# Esta lógica es más clara en bucle que en comprehension


# Dataset de ventas: (producto, unidades, precio, categoria)
ventas = [
    ("Auriculares Pro",   45,  89.99, "Electrónica"),
    ("Camiseta Básica",  120,  19.99, "Ropa"),
    ("Silla Ergonómica",  18, 299.99, "Muebles"),
    ("Teclado Mecánico",  30,  74.99, "Electrónica"),
    ("Botella Térmica",   75,  34.99, "Hogar"),
    ("Monitor 4K",        12, 499.99, "Electrónica"),
]
 

# 1. valor_total = unidades × precio por producto

valor_total = [
    (nombre, round(unidades * precio, 2))
    for nombre, unidades, precio, _ in ventas
]
 
print("─" * 50)
print("valor total por producto")
print("─" * 50)
for nombre, total in valor_total:
    print(f"  {nombre:<22} ${total:>8,.2f}")
 

# 2.  productos con valor_total > 1000

productos_destacados = [
    nombre
    for nombre, unidades, precio, _ in ventas
    if unidades * precio > 1000
]
 
print("Productos destacados (valor > $1,000)")
print("─" * 50)
for p in productos_destacados:
    print("{p}")
 

# 3.  producto_info → nombre: {valor, unidades}

producto_info = {
    nombre: {"valor": round(unidades * precio, 2), "unidades": unidades}
    for nombre, unidades, precio, _ in ventas
}
 
print(" informacion de producti (nombre → valor + unidades)")
print("─" * 50)
for nombre, info in producto_info.items():
    print(f"  {nombre:<22} → ${info['valor']:>8,.2f}  |  {info['unidades']} uds.")
 
#
# 4.  ranking_premium (precio > 50)


ranking_premium = dict(
    sorted(
        {
            nombre: round(unidades * precio, 2)
            for nombre, unidades, precio, _ in ventas
            if precio > 50
        }.items(),
        key=lambda x: x[1],
        reverse=True
    )
)
 
print(" rankinf de premio (precio > $50, orden por valor desc)")
print("─" * 50)
for pos, (nombre, valor) in enumerate(ranking_premium.items(), start=1):
    print(f"  #{pos}  {nombre:<22} ${valor:>8,.2f}")
 

# 5. categorias_unicas + productos_baratos (precio ≤ 50)

categorias_unicas = {categoria for _, _, _, categoria in ventas}
 
productos_baratos = {
    nombre
    for nombre, _, precio, _ in ventas
    if precio <= 50
}
 
print("categorias unica ebbe")
print("─" * 50)
print(f"  {categorias_unicas}")
 
print("producto baratos de china (precio ≤ $50)")
print("─" * 50)
print(f"  {productos_baratos}")

# 6.  resumen_formateado + gran_total

resumen_formateado = {
    nombre: f"${round(unidades * precio, 2):,.2f} ({unidades} uds.)"
    for nombre, unidades, precio, _ in ventas
    if unidades * precio > 1000          # solo los que destacan
}
 
gran_total = sum(unidades * precio for _, unidades, precio, _ in ventas)
 
print("resumen formateado (valor > $1,000)")
print("─" * 50)
for nombre, resumen in resumen_formateado.items():
    print(f"  {nombre:<22} → {resumen}")
 
print("\n" + "═" * 50)
print(f" el gran total de ventasS:      ${gran_total:>10,.2f}")
print("═" * 50)