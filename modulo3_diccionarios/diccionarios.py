#Módulo 03 · Intermedio
#Diccionarios


#Ejemplo 1 Estructura Clave-Valor
contactos = {
    "Ana":    "612345678",
    "Carlos": "698765432"
}
print(contactos["Ana"])                    # 612345678
print(contactos.get("Elena", "No encontrado"))  # No encontrado

# Claves válidas (inmutables)
valido = {"nombre":"Juan", 42:"respuesta", (1,2):"coord"}

# INVÁLIDAS
# invalido = {[1,2]: "x"}  # TypeError: unhashable type: 'list'

#ejemplo 2

colores = dict(rojo="#FF0000", verde="#00FF00", azul="#0000FF")

claves  = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]
persona = {k: v for k, v in zip(claves, valores)}

# Diccionario anidado
usuario = {
    "nombre": "Miguel", "edad": 30,
    "direccion": {"calle":"Calle Mayor","ciudad":"Madrid"}
}
ciudad = usuario["direccion"]["ciudad"]  # "Madrid"

#ejemplo 3  Operaciones CRUD

califs = {"Mates": 85, "Historia": 72}
califs.update({"Inglés": 88, "Mates": 87, "Arte": 95})

vendido = califs.pop("Inglés")      # retorna 88
par_final = califs.popitem()        # último par insertado

contador = {}
contador.setdefault("hola", 0)
contador["hola"] += 1               # → {"hola": 1}

materias = ["Mates","Historia","Arte"]
notas = dict.fromkeys(materias, 0)  # → {"Mates":0, ...}

d1 = {"nombre":"Carlos","edad":28}
d2 = {"email":"c@e.com"}
unido = d1 | d2                     # fusión Python 3.9+

# ejemplo 4 Iteración
califs = {"Mates":85, "Historia":72, "Ciencias":90}

for asig, nota in califs.items():
    print(f"{asig}: {nota}")

# Orden alfabético de claves
for asig in sorted(califs):
    print(f"{asig}: {califs[asig]}")

# Iteración segura: eliminar mientras recorres
d = {"a":1, "b":2, "c":3}
for k in list(d.keys()):
    if k == "b": del d[k]   # OK — iterando copia
print(d)  # {"a":1, "c":3}

#ejemplo 5 Comprensiones de diccionario

precios = {"laptop":899, "tablet":349}

# Aplicar descuento del 10%
rebaja = {p: round(v*0.9, 2) for p,v in precios.items()}

# Filtrar productos disponibles
stock = {"manzanas":10, "peras":0, "naranjas":25}
disponibles = {f:c for f,c in stock.items() if c > 0}

# Invertir clave-valor
original  = {"a":1, "b":2, "c":3}
invertido = {v:k for k,v in original.items()}

# Porcentaje del total
gran_total = sum(precios.values())
pct = {p: round(v/gran_total*100,1) for p,v in precios.items()}


#analiza un dict anidado de ventas trimestrales: calcula totales, encuentra máximos y genera reportes con porcentajes.

#1 Define ventas_por_region como dict anidado { region: { Q1, Q2, Q3, Q4 } }
#2 Calcula el total anual de cada región con items() y sum(values())
#3 Usa max() con key=lambda para la región con mayores ventas
#4Acumula ventas por trimestre con iteración anidada
#5Genera porcentajes con dict comprehension sobre el gran total
#6 Imprime reporte ordenado de mayor a menor con sorted() + items()

# Definir ventas_por_region

# Calcular ventas totales con items() y sum(values())

# Encontrar region con max() key=lambda

# Inicializar totales_por_trimestre

# Acumular con iteracion anidada

# Calcular gran_total

# Generar porcentajes con dict comprehension

# Imprimir reporte ordenado

#Solucion reto #1 diccionarios

# 1. Definir ventas_por_region 
ventas_por_region = {
    "Norte": {"Q1": 15000, "Q2": 18000, "Q3": 12000, "Q4": 22000},
    "Sur":   {"Q1": 10000, "Q2": 12000, "Q3": 15000, "Q4": 11000},
    "Este":  {"Q1": 20000, "Q2": 21000, "Q3": 19000, "Q4": 25000},
    "Oeste": {"Q1": 8000,  "Q2": 9500,  "Q3": 11000, "Q4": 10500}
}

# 2. Calcular el total anual de cada región con items() y sum(values())
totales_anuales = {region: sum(trimestres.values()) for region, trimestres in ventas_por_region.items()}

# 3. Encontrar región líder con max() y key=lambda
region_lider = max(totales_anuales.items(), key=lambda item: item[1])

# 4. Acumular ventas por trimestre con iteración anidada
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for region, trimestres in ventas_por_region.items():
    for q, monto in trimestres.items():
        totales_por_trimestre[q] += monto

# 5. Calcular gran total y porcentajes con dict comprehension
gran_total = sum(totales_anuales.values())
porcentajes_region = {reg: (monto / gran_total) * 100 for reg, monto in totales_anuales.items()}

# 6. Imprimir reporte ordenado de mayor a menor con sorted()
reporte_ordenado = sorted(totales_anuales.items(), key=lambda x: x[1], reverse=True)

print("--- reporte de ventas ---")
print(f"{'Región':<10} | {'Total':<10} | {' Participación'}")
print("-" * 40)

for region, total in reporte_ordenado:
    pct = porcentajes_region[region]
    print(f"{region:<10} | ${total:<9} | {pct:>12.2f}%")

print("-" * 40)
print(f"Ganador del año: {region_lider[0]} con ${region_lider[1]:}")


