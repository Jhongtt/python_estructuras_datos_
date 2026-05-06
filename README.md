# inicio Listas #
sirve para Colección ordenada y mutable. Índices positivos y negativos, slicing, append, insert, remove, comprensiones y copias.


# Creación y Acceso #
[ ], list(), índices +/−, count(), index(), in, len()
Las listas son colecciones ordenadas y mutables. Se crean con corchetes [] o con list(). Cada elemento tiene un índice que empieza en 0. Los índices negativos permiten acceder desde el final: -1 es el último elemento.


frutas = ["manzana","plátano"] — lista literal con corchetes

numeros = list(range(1,6)) — desde iterable con list()

tareas[-1] — último elemento con índice negativo

"pan" in compras— verificar existencia en O(n)
len(lista)— número total de elementos

lista.count(x)— cuántas veces aparece x

lista.index(x)— posición de la primera ocurrencia de x

# Métodos para añadir #
append(), insert(i, val), extend(iterable)
append() agrega un único elemento al final. insert(i, val) lo coloca en la posición i desplazando los siguientes. extend() añade todos los elementos de un iterable al final — es la diferencia clave con append.

# conceptos clave #

lista.append(x) — añade x al final como elemento único
lista.insert(1, x) — inserta x en posición 1
lista.extend([x, y]) — añade x e y como elementos individuales

# Métodos para eliminar #

remove(val), pop(i), clear() — diferencias clave
remove(val) busca y elimina la primera ocurrencia de un valor; lanza ValueError si no existe. pop(i) elimina por índice y retorna el elemento eliminado. clear() vacía la lista completa sin eliminar el objeto.

# conceptos clave #
lista.remove("verde") — elimina la primera ocurrencia del valor

elem = lista.pop()— elimina y retorna el último elemento

elem = lista.pop(1)— elimina y retorna el elemento en índice 1

lista.clear()— vacía la lista: []

del lista[1]— elimina elemento en posición 1

del lista[1:3]— elimina slice de la lista

# Ordenar y reorganizar #
sort(), reverse(), sorted() — in-place vs nueva lista
sort() ordena la lista original en su lugar (devuelve None). sorted() devuelve una nueva lista ordenada sin tocar la original. reverse() invierte el orden in-place. Ambos aceptan el parámetro reverse=True para orden descendente.

# conceptos clave #
lista.sort()
— ordena la lista original (in-place)
lista.sort(reverse=True)
— orden descendente
lista.reverse()
— invierte in-place
nueva = sorted(lista)
— nueva lista ordenada, original intacta

# Recorrido de listas #
for, enumerate, range+len, zip, comprensiones
Python ofrece múltiples formas de recorrer listas. for x in lista es el más directo. enumerate() añade el índice. zip() recorre dos listas en paralelo. Las comprensiones de lista son la forma más concisa para transformar o filtrar.

# conceptos clave #
for x in lista
— recorre cada elemento directamente
for i, x in enumerate(lista, 1)
— índice + elemento
for i in range(len(lista))
— recorre por índice
for a, b in zip(l1, l2)
— dos listas en paralelo
[x*2 for x in lista]
— comprensión: transforma
[x for x in lista if x > 0]
— comprensión: filtra

# Modificación y copias #
slices, anidadas, copy() vs deepcopy()
Asignar una lista a otra variable no crea una copia — ambas apuntan al mismo objeto. copy() crea una copia superficial (los objetos anidados se siguen compartiendo). deepcopy() hace una copia completamente independiente, necesaria cuando hay listas dentro de listas.

# conceptos clave #
b = a
— misma referencia (cambiar b cambia a)
b = a.copy()
— copia superficial independiente
b = a[:]
— otra forma de copia superficial
b = copy.deepcopy(a)
— copia profunda: independiente en todos los niveles

---------------------------------------------------------------------------------------------------------------
# Módulo 02 · Básico #  
Tuplas
Colección ordenada e inmutable. Hashables, más rápidas que las listas y con desempaquetado elegante.

Inmutabilidad
TypeError al modificar, ventajas, rendimiento, contenido mutable

Una tupla, una vez creada, no puede modificarse: no es posible añadir, eliminar ni cambiar sus elementos. Intentarlo lanza un TypeError. Esta restricción aporta seguridad de datos, hashabilidad y un mejor rendimiento en ciertos escenarios. Ojo: si la tupla contiene un objeto mutable (como una lista), ese objeto sí puede modificarse internamente.

conceptos clave
coordenadas[0] = 15
— TypeError: no soporta asignación
t.append(x)
— AttributeError: no existe ese método
config[1].append(4)
— OK si config[1] es una lista mutable

Hashabilidad y rendimiento
Claves de diccionario, sets, velocidad de creación
Al ser inmutables, las tuplas son hashables y pueden usarse como claves de diccionario o elementos de conjuntos (las listas no pueden). Además, Python puede optimizar su almacenamiento: la creación de tuplas es notablemente más rápida que la de listas equivalentes.

conceptos clave
d = {(40.71, -74.00): "NY"}
— tupla como clave de diccionario
s = {(1,2), (3,4)}
— tuplas en un conjunto
d = {[40.71, -74.00]: "NY"}
— TypeError: lista no es hashable

Creación de tuplas
(), comas, tuple(), singleton (42,), generador, vacía
Las tuplas se crean con paréntesis o simplemente con comas. Lo que realmente define una tupla son las comas. Para una tupla de un solo elemento es obligatorio escribir la coma final (42,); sin ella Python interpreta el valor como un entero. La tupla vacía se crea con () o tuple().

conceptos clave
frutas = ("manzana", "naranja")
— con paréntesis
coordenadas = 10, 20, 30
— solo comas, sin paréntesis
singleton = (42,)
— coma obligatoria para un elemento
desde_lista = tuple([1,2,3])
— desde iterable
cuadrados = tuple(x**2 for x in range(5))
— desde generador
vacia = ()
— tupla vacía

Acceso a elementos
Índices, slicing, count(), index(), in, len()
El acceso a tuplas funciona igual que en listas: índices positivos desde 0 e índices negativos desde el final. El slicing devuelve una nueva tupla. Los métodos count() e index() son los únicos dos métodos de instancia que tienen las tuplas.

conceptos clave
datos[0]
— primer elemento
datos[-1]
— último elemento
datos[1:3]
— subtupla (nueva tupla)
datos[::-1]
— tupla invertida
t.count(x)
— número de ocurrencias de x
t.index(x)
— índice de la primera ocurrencia de x

Desempaquetado básico y operador *
a,b,c = t, swap, *resto, *medio
El desempaquetado permite asignar los elementos de una tupla a variables en una sola línea. El número de variables debe coincidir con el número de elementos, excepto cuando se usa * para capturar "el resto" como lista. * puede aparecer al inicio, en el medio o al final.

conceptos clave
nombre, precio = producto
— desempaquetado básico
a, b = b, a
— intercambio elegante sin variable temporal
primero, *resto = nums
— primero=1, resto=[2,3,4,5]
*inicio, ultimo = nums
— ultimo=5, inicio=[1,2,3,4]
p, *medio, u = nums
— captura el centro

Técnicas avanzadas de desempaquetado
_, bucle for, zip+enumerate, retorno múltiple, anidado
El guion bajo _ descarta campos que no necesitas. El desempaquetado en bucles for permite iterar sobre secuencias de tuplas de forma muy legible. Las funciones pueden retornar múltiples valores como tupla y desempaquetarlos al llamarlas.

conceptos clave
nombre, _, edad, _, prof = datos
— ignora campos con _
for nombre, edad, nota in estudiantes
— desempaqueta en cada iteración
for i,(n,e) in enumerate(zip(l1,l2),1)
— combina zip y enumerate
mi, ma, avg = estadisticas(lista)
— retorno múltiple
lugar, (lat, lon) = ubicacion
— desempaquetado anidado
 

# reto 2 #
Construye un catálogo de películas usando tuplas inmutables, desempaquetado y técnicas de acceso del módulo.

1
Define catalogo como tupla de tuplas ( titulo, director, año, puntuacion )
2
Desempaqueta cada película en un bucle e imprime su información
3
Usa el operador * para separar la primera película del resto
4
Implementa buscar_por_director() que devuelva tupla de coincidencias
5
Implementa obtener_estadisticas() retornando (min, max, promedio)
6
Desempaqueta el retorno de obtener_estadisticas() e imprime los tres valores
[ ocultar esqueleto ]
# Definir catalogo como tupla de subtuplas

# Recorrer catalogo con for desempaquetando los cuatro campos

# Usar operador * para separar primera pelicula del resto

# Definir buscar_por_director(director)

# Definir obtener_estadisticas(peliculas)

# Llamar a buscar_por_director e imprimir coincidencias

# Desempaquetar retorno de obtener_estadisticas

# Imprimir minima, maxima y promedio

Módulo 03 · Intermedio
Diccionarios
Pares clave→valor. Claves únicas e inmutables. Orden preservado desde Python 3.7.

Estructura Clave-Valor
Características, claves válidas, get(), in
Un diccionario almacena pares clave→valor. Las claves deben ser únicas e inmutables (strings, números, tuplas). Los valores pueden ser cualquier tipo. Desde Python 3.7 el orden de inserción se garantiza. get() evita el KeyError devolviendo un valor por defecto.

conceptos clave
d["clave"]
— acceso directo; KeyError si no existe
d.get("clave", "N/A")
— acceso seguro con valor por defecto
"clave" in d
— verifica existencia sin excepción
d["nueva"] = valor
— añade o sobreescribe

Creación de diccionarios
{}, dict(), zip, comprensión, anidados
Existen múltiples formas de crear diccionarios. La más común es con llaves. dict() acepta kwargs o iterables de pares. Con zip() se pueden construir a partir de dos listas. Los diccionarios anidados son dicts cuyo valor es otro dict.

conceptos clave
d = {"a":1, "b":2}
— literal con llaves
d = dict(rojo="#FF0000")
— con kwargs
d = dict(zip(claves, valores))
— desde dos listas
{n: n**2 for n in range(5)}
— dict comprehension
usuario["dirección"]["ciudad"]
— acceso anidado

Operaciones CRUD
update(), pop(), popitem(), clear(), copy()
update() añade o sobreescribe múltiples pares. pop(k) elimina y retorna el valor; acepta un default para no lanzar error. setdefault(k, v) inserta k:v solo si la clave no existe. fromkeys() crea un dict con claves de una secuencia y un valor común.

conceptos clave
d.update({"c":3, "d":4})
— añade/sobreescribe varios pares
val = d.pop("clave", None)
— elimina y retorna, None si no existe
k, v = d.popitem()
— elimina y retorna el último par
d.setdefault("hits", 0)
— inserta solo si no existe
d.fromkeys(lista, 0)
— dict con valor inicial para cada clave
d1 | d2
— fusión (Python 3.9+)

Iteración
keys(), values(), items(), sorted(), iteración segura
keys(), values() e items() devuelven vistas dinámicas que reflejan cambios en el dict. items() es la forma más potente: desempaqueta clave y valor en cada iteración. Nunca modifiques un dict mientras lo iteras — haz una copia de las claves primero.

conceptos clave
for k in d
— itera sobre las claves
for v in d.values()
— itera sobre los valores
for k, v in d.items()
— itera sobre pares clave-valor
sorted(d)
— claves en orden alfabético
for k in list(d.keys())
— iteración segura si vas a modificar

Comprensiones de diccionario
6 patrones: filtrar, invertir, temperatura, agrupar
Las dict comprehensions crean diccionarios en una línea con la sintaxis {k: v for x in it if cond}. Son especialmente útiles para transformar, filtrar e invertir diccionarios existentes.

conceptos clave
{n: n**2 for n in range(5)}
— cuadrados
{k: v.upper() for k,v in d.items()}
— transformar valores
{v: k for k,v in d.items()}
— invertir clave↔valor
{k:v for k,v in d.items() if v>0}
— filtrar por valor
{c: round(t*9/5+32,1) for c,t in temps.items()}
— Celsius→F

naliza un dict anidado de ventas trimestrales: calcula totales, encuentra máximos y genera reportes con porcentajes.

1
Define ventas_por_region como dict anidado { region: { Q1, Q2, Q3, Q4 } }
2
Calcula el total anual de cada región con items() y sum(values())
3
Usa max() con key=lambda para la región con mayores ventas
4
Acumula ventas por trimestre con iteración anidada
5
Genera porcentajes con dict comprehension sobre el gran total
6
Imprime reporte ordenado de mayor a menor con sorted() + items()
[ ocultar esqueleto ]
# Definir ventas_por_region

# Calcular ventas totales con items() y sum(values())

# Encontrar region con max() key=lambda

# Inicializar totales_por_trimestre

# Acumular con iteracion anidada

# Calcular gran_total

# Generar porcentajes con dict comprehension

# Imprimir reporte ordenado

Módulo 04 · Intermedio
Conjuntos
Colección desordenada de elementos únicos. Búsqueda O(1). Perfectos para eliminar duplicados y operaciones de teoría de conjuntos.

Elementos únicos y creación
{}, set(), hashabilidad, conjunto vacío set()
Un conjunto (set) almacena elementos sin duplicados y sin orden garantizado. Solo puede contener elementos hashables (inmutables). La búsqueda con in es O(1) — mucho más rápida que en una lista. Ojo: {} crea un diccionario vacío, no un set; usa set().

conceptos clave
colores = {"rojo","verde","azul","rojo"}
— duplicado ignorado automáticamente
nums = set([1,2,3,2,1])
— desde lista, elimina dupes
vacio = set()
— set vacío (no {})
{1,"hola",(1,2)}
— válido: todos inmutables
{1,[2,3]}
— TypeError: lista no es hashable

Operaciones básicas
add(), update(), remove(), discard(), pop(), clear()
add() añade un elemento (si ya existe, no hace nada). update() añade múltiples desde un iterable. remove() lanza KeyError si el elemento no existe; discard() no lanza error. pop() elimina un elemento arbitrario.

conceptos clave
s.add(x)
— añade x; sin efecto si ya existe
s.update([x,y,z])
— añade múltiples elementos
s.remove(x)
— elimina x; KeyError si no existe
s.discard(x)
— elimina x; silencioso si no existe
elem = s.pop()
— elimina y retorna un elemento aleatorio
s.clear()
— vacía el conjunto
s.copy()
— copia independiente

Métodos de teoría de conjuntos
intersection(), union(), difference(), symmetric_difference()
Estos métodos implementan las operaciones clásicas de teoría de conjuntos y devuelven nuevos sets sin modificar los originales. Sus variantes con _update modifican el set original in-place. isdisjoint() verifica si no hay elementos comunes.

conceptos clave
A.intersection(B)
— elementos comunes (A ∩ B)
A.union(B)
— todos los elementos (A ∪ B)
A.difference(B)
— en A pero no en B (A - B)
A.symmetric_difference(B)
— en uno u otro pero no en ambos (A △ B)
A.intersection_update(B)
— modifica A: deja solo los comunes
A.difference_update(B)
— modifica A: elimina los de B
A.isdisjoint(B)
— True si no comparten ningún elemento

Operadores matemáticos
| & - ^ y variantes de asignación |= &= -= ^=
Los operadores matemáticos son equivalentes a los métodos pero con sintaxis más concisa. | = union, & = intersección, - = diferencia, ^ = diferencia simétrica. Los operadores de asignación (|=, &=, -=, ^=) modifican el set original.

onceptos clave
A | B
— unión (equivale a A.union(B))
A & B
— intersección (equivale a A.intersection(B))
A - B
— diferencia (equivale a A.difference(B))
A ^ B
— dif. simétrica
A |= B
— A = A | B (modifica A)
A &= B
— A = A & B
A <= B
— A es subconjunto de B
A >= B
— A es superconjunto de B

Módulo 05 · Avanzado
Comprehensions
Sintaxis concisa para crear colecciones en una línea. Hasta 40% más rápidas que bucles equivalentes.

List comprehension
[expr for x in it if cond], comparación con bucle
Las list comprehensions crean listas en una sola línea con la sintaxis [expresión for elemento in iterable if condición]. Son más concisas y generalmente más rápidas que los bucles equivalentes con append(), gracias a optimizaciones internas de CPython. La cláusula if al final actúa como filtro.

conceptos clave
[n**2 for n in range(10)]
— lista de cuadrados
[n for n in range(10) if n%2==0]
— solo pares
[(9/5)*t+32 for t in celsius]
— Celsius → Fahrenheit
[u["nombre"] for u in usuarios]
— extraer campo de dicts
[p.upper() for p in palabras]
— transformar strings

Dict comprehension
{k:v for x in it if cond}, 6 patrones prácticos
Las dict comprehensions crean diccionarios con la sintaxis {clave: valor for elemento in iterable if condición}. Son ideales para transformar, filtrar e invertir diccionarios, o para construirlos a partir de listas.

conceptos clave
{n: n**2 for n in range(5)}
— cuadrados como dict
{k: v.upper() for k,v in d.items()}
— transformar valores
{v: k for k,v in d.items()}
— invertir clave↔valor
{f:c for f,c in stock.items() if c>0}
— filtrar por valor
{k:v for k,v in zip(claves, vals)}
— desde dos listas
{e["id"]:e["nombre"] for e in lista}
— desde lista de dicts

Set comprehension
{expr for x in it if cond}, unicidad automática
Las set comprehensions crean conjuntos con la misma sintaxis que las list comp pero con llaves. Su ventaja principal es la eliminación automática de duplicados. Son ideales cuando necesitas transformar datos y asegurar unicidad en un solo paso.

conceptos clave
{n**2 for n in range(5)}
— set de cuadrados únicos
{n for n in lista}
— elimina duplicados de lista
{p[0] for p in palabras}
— iniciales únicas
{l for l in texto if l in "aeiou"}
— vocales únicas
{n%5 for n in range(20)}
— residuos únicos


Rendimiento y cuándo NO usarlas
Velocidad, legibilidad, memoria, generadores
Las comprehensions son hasta un 40% más rápidas que los bucles equivalentes en CPython. Sin embargo, no siempre son la mejor opción: si la lógica es compleja, un bucle tradicional es más legible. Para colecciones muy grandes usa generadores (x for x in it) para no cargar todo en memoria de una vez.

conceptos clave
[x for x in range(1_000_000)]
— carga toda la lista en RAM
(x for x in range(1_000_000))
— generador: evalúa uno a uno
# Si hay más de 2 condiciones
— considera un bucle for

-------------------------------------------------------------------------------------------------------------------------------