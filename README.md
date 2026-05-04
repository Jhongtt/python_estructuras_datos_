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