#tuplas

#Ejemplo 1 Inmutabilidad

coordenadas = (10, 20)
try:
    coordenadas[0] = 15
except TypeError as e:
    print(f"Error: {e}")
# 'tuple' object does not support item assignment

# Contenido mutable dentro de tupla
config = ("config_v1", [1, 2, 3])
config[1].append(4)  # OK
print(config)         # ('config_v1', [1, 2, 3, 4])

#Ejemplo 2 Hashabilidad y rendimiento

# Tuplas como claves de diccionario
ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522,-118.2437): "Los Ángeles"
}
print(ubicaciones[(40.7128, -74.0060)])  # Nueva York

# Las listas NO son hashables
try:
    d = {[40.71, -74.00]: "NY"}
except TypeError as e:
    print(f"Error: {e}")  # unhashable type: 'list'


#Ejemplo 3 Creación de tuplas

numeros  = (1, 2, 3, 4, 5)
coords   = 10, 20, 30          # también es tupla
vacia    = ()
singleton = (42,)              # coma obligatoria

desde_lista = tuple([1, 2, 3])
desde_str   = tuple("Python")  # ('P','y','t','h','o','n')
desde_rango = tuple(range(5))  # (0, 1, 2, 3, 4)

print(type((42)))   # <class 'int'>   — SIN coma
print(type((42,)))  # <class 'tuple'> — CON coma

#Ejemplo 4 Acceso a elementos

datos = ("Python", 3.9, 2023, "Tuplas")
print(datos[0])    # "Python"
print(datos[-1])   # "Tuplas"

nums = (0,1,2,3,4,5,6,7,8,9)
print(nums[2:6])   # (2,3,4,5)
print(nums[::2])   # (0,2,4,6,8)
print(nums[::-1])  # (9,8,7,6,5,4,3,2,1,0)

t = (1, 2, 3, 2, 4, 2, 5)
print(t.count(2))  # 3
print(t.index(3))  # 2

#Ejemplo 5 Desempaquetado básico y operador *

producto = ("Laptop XPS", 1299.99, "Dell")
nombre, precio, fabricante = producto
print(nombre)      # Laptop XPS
print(precio)      # 1299.99

a, b = 5, 10
a, b = b, a        # swap en una línea
print(a, b)        # 10 5

numeros = (1, 2, 3, 4, 5)
primero, *resto          = numeros  # resto=[2,3,4,5]
primero, *medio, ultimo  = numeros  # medio=[2,3,4]
*iniciales, ultimo       = numeros  # iniciales=[1,2,3,4]

#Ejemplo 6 Técnicas avanzadas de desempaquetado

datos = ("Juan","Pérez",35,"Madrid","Ingeniero")
nombre, _, edad, _, prof = datos
print(f"{nombre}, {edad}, {prof}")

estudiantes = [("Ana",22,9.5),("Carlos",20,8.7)]
for nombre, edad, nota in estudiantes:
    print(f"{nombre}: {nota}")

def estadisticas(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

minima, maxima, promedio = estadisticas([4,7,2,9,5])
print(f"min={minima} max={maxima} avg={promedio:.2f}")

#reto 2 tuplas Sistema de películas

#Sistema de películas
#reto
#Construye un catálogo de películas usando tuplas inmutables, desempaquetado y técnicas de acceso del módulo.

#1 Define catalogo como tupla de tuplas ( titulo, director, año, puntuacion )
#2 Desempaqueta cada película en un bucle e imprime su información
#3 Usa el operador * para separar la primera película del resto
#4 Implementa buscar_por_director() que devuelva tupla de coincidencias
#5 Implementa obtener_estadisticas() retornando (min, max, promedio)
#6 Desempaqueta el retorno de obtener_estadisticas() e imprime los tres valores

# 1. Catálogo como tupla de tuplas (titulo, director, año, puntuacion)
catalogo = (
    ("Interstellar",        "Christopher Nolan", 2014, 9.5),
    ("El Padrino",          "Francis Ford Coppola", 1972, 9.2),
    ("Parasite",            "Bong Joon-ho",      2019, 8.6),
    ("Spirited Away",       "Hayao Miyazaki",    2001, 8.6),
    ("The Dark Knight",     "Christopher Nolan", 2008, 9.0),
    ("Pulp Fiction",        "Quentin Tarantino", 1994, 8.9),
)

print("=" * 50)
print("         catalogo de peliculas")
print("=" * 50)

# 2. Desempaquetar cada película en un bucle
for titulo, director, año, puntuacion in catalogo:   #
    print(f" Título:     {titulo}")
    print(f"   Director:   {director}")
    print(f"   Año:        {año}")
    print(f"   Puntuación: {puntuacion}/10")
    print("-" * 50)

# 3. Operador * para separar la primera película del resto
primera, *resto = catalogo                           

print("\n primera pelicula del catalogo de peliculas:")
titulo, director, año, puntuacion = primera          
print(f"   {titulo} ({año}) - Dir: {director} -  {puntuacion}")

print(f"\n lo que sigue del catalogo ({len(resto)} películas):")
for titulo, director, año, puntuacion in resto:
    print(f"   • {titulo} ({año})")

# 4. Buscar por director
def buscar_por_director(catalogo, nombre_director):
    """Devuelve una tupla con todas las películas del director indicado."""
    coincidencias = tuple(                          
        pelicula for pelicula in catalogo
        if pelicula[1].lower() == nombre_director.lower()
    )
    return coincidencias

print("\n" + "=" * 50)
print("busqueda por director: Christopher Nolan")
print("=" * 50)

resultado = buscar_por_director(catalogo, "Christopher Nolan")

if resultado:
    for titulo, director, año, puntuacion in resultado:
        print(f"    {titulo} ({año}) -  {puntuacion}")
else:
    print("No se encontraron películas.")

# 5. Obtener estadísticas de puntuaciones
def obtener_estadisticas(catalogo):
    """Retorna (minima, maxima, promedio) de las puntuaciones."""
    puntuaciones = tuple(pelicula[3] for pelicula in catalogo)  

    minima   = min(puntuaciones)
    maxima   = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)

    return (minima, maxima, round(promedio, 2))      

# 6. Desempaquetar el retorno de obtener_estadisticas()
print("\n" + "=" * 50)
print("estaditicas de puntuaciones")
print("=" * 50)

minima, maxima, promedio = obtener_estadisticas(catalogo)   
print(f"   Mínima:   {minima}/10")
print(f"    Máxima:   {maxima}/10")
print(f"   Promedio: {promedio}/10")