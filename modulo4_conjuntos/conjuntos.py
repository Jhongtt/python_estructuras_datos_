# conjuntos

#ejemplo #1 

colores = {"rojo","verde","azul","rojo"}
print(colores)  # {'verde','azul','rojo'} — sin "rojo" duplicado

numeros = set([1, 2, 3, 2, 1])
print(numeros)  # {1, 2, 3}

# Búsqueda eficiente
frutas = {"manzana","naranja","plátano"}
print("manzana" in frutas)  # True — O(1)

# Conjunto vacío
vacio = set()
print(type({}))   # <class 'dict'>   — NO es un set
print(type(set())) # <class 'set'>   — correcto


# ejemplo 2

tecnologias = {"Python","JavaScript","SQL"}
tecnologias.add("Java")
tecnologias.update(["Go","Rust"])

frutas = {"manzana","naranja","platano"}
frutas.remove("naranja")    # OK
frutas.discard("kiwi")      # silencioso — kiwi no existe
elem = frutas.pop()         # aleatorio
frutas.clear()              # set()

# issubset / issuperset
pares = {2,4,6,8}
nums  = {1,2,3,4,5,6,7,8,9}
print(pares.issubset(nums))   # True
print(nums.issuperset(pares)) # True

#ejemplo 3

grupo_a = {"Ana","Carlos","Elena","David"}
grupo_b = {"Carlos","Elena","Fernando"}

comunes     = grupo_a.intersection(grupo_b)  # {'Carlos','Elena'}
todos       = grupo_a.union(grupo_b)
solo_en_a   = grupo_a.difference(grupo_b)    # {'Ana','David'}
exclusivos  = grupo_a.symmetric_difference(grupo_b)

vegetales = {"zanahoria","pepino"}
frutas    = {"manzana","platano"}
print(vegetales.isdisjoint(frutas))  # True — sin elementos comunes

# Encadenamiento
resultado = grupo_a.intersection(grupo_b).difference({"Elena"})
# → {'Carlos'}

#ejemplo 4

u1 = {"acción","comedia","ciencia ficción","aventura"}
u2 = {"drama","comedia","romance","documental"}
u3 = {"acción","aventura","fantasía","ciencia ficción"}

comunes_1_3  = u1 & u3   # {'acción','ciencia ficción','aventura'}
todos_1_2    = u1 | u2
solo_u1      = u1 - u2   # excluye lo de u2
excl_2_3     = u2 ^ u3   # en uno pero no en ambos

# Operadores de comparación
print(u3 <= u1)  # False — u3 NO es subconjunto de u1
print({2,4} <= {1,2,3,4,5})  # True

#reto Tiendas y recomendaciones de películas


#1. Definir catálogos de tiendas como sets
tienda_centro = {"Laptop", "Tablet", "Audífonos", "Teclado", "Monitor", "Webcam"}
tienda_norte  = {"Tablet", "Audífonos", "Mouse", "Impresora", "Micrófono", "Webcam"}
tienda_sur    = {"Cámara", "Proyector", "Audífonos", "Monitor", "Drone", "Trípode"}

#2. Catálogo completo e intersección
catalogo_completo  = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes  = tienda_centro.intersection(tienda_norte, tienda_sur)

#3. Exclusivos de cada tienda (diferencia con las otras dos) 
exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivos_norte  = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivos_sur    = tienda_sur.difference(tienda_centro.union(tienda_norte))

# Verificar solapamientos con isdisjoint()
centro_norte_disjoint = tienda_centro.isdisjoint(tienda_norte)
centro_sur_disjoint   = tienda_centro.isdisjoint(tienda_sur)
norte_sur_disjoint    = tienda_norte.isdisjoint(tienda_sur)

#  4. Géneros cinematográficos por usuario
usuario1 = {"Acción", "Ciencia Ficción", "Thriller", "Aventura"}
usuario2 = {"Ciencia Ficción", "Drama", "Thriller", "Comedia"}
usuario3 = {"Terror", "Drama", "Animación", "Aventura"}

#5. Operadores matemáticos de sets
generos_comunes_1_2     = usuario1 & usuario2          
universo_generos        = usuario1 | usuario2 | usuario3  
exclusivos_usuario1     = usuario1 - usuario2           
diferencia_simetrica    = usuario1 ^ usuario2         

# Subconjunto con <=
base_generos = {"Acción", "Drama"}
usuario1_incluye_base = base_generos <= usuario1
usuario2_incluye_base = base_generos <= usuario2


print("=" * 60)
print(" analista de tienda- el catalogo de los prodcutos")
print("=" * 60)
print(f" Catálogo del centro  : {sorted(tienda_centro)}")
print(f" Catálogo del norte  : {sorted(tienda_norte)}")
print(f" Catálogo del sur     : {sorted(tienda_sur)}")
print(f" Catálogo Completo ({len(catalogo_completo)} productos):")
print(f"   {sorted(catalogo_completo)}")
print(f"Productos comunes em las 3 tiendas:")
print(f"   {sorted(productos_comunes) if productos_comunes else 'Ninguno'}")
print(f" Exclusivos del centro el hueco : {sorted(exclusivos_centro) if exclusivos_centro else 'Ninguno'}")
print(f"Exclusivos del norte  : {sorted(exclusivos_norte)  if exclusivos_norte  else 'Ninguno'}")
print(f"Exclusivos del sur    : {sorted(exclusivos_sur)    if exclusivos_sur    else 'Ninguno'}")
print(f" ¿Centro y Norte sin solapamiento? → {centro_norte_disjoint}")
print(f"¿Centro y Sur sin solapamiento?   → {centro_sur_disjoint}")
print(f"¿Norte y Sur sin solapamiento?    → {norte_sur_disjoint}")

print("\n" + "=" * 60)
print("recomendacion de peliculas")
print("=" * 60)
print(f"Usuario 1: {sorted(usuario1)}")
print(f"Usuario 2: {sorted(usuario2)}")
print(f"Usuario 3: {sorted(usuario3)}")
print(f"egneros muy comunes (u1 & u2)          : {sorted(generos_comunes_1_2)}")
print(f" Universo de géneros (u1|u2|u3)     : {sorted(universo_generos)}")
print(f" Exclusivos de Usuario1 vs u2 (-)   : {sorted(exclusivos_usuario1)}")
print(f"Diferencia simétrica u1^u2 (^)     : {sorted(diferencia_simetrica)}")
print(f"\n Base de géneros analizados         : {sorted(base_generos)}")
print(f"   ¿Base ⊆ Usuario1 (<=)?            → {usuario1_incluye_base}")
print(f"   ¿Base ⊆ Usuario2 (<=)?            → {usuario2_incluye_base}")
print("\n" + "=" * 60)
print(" Análisis completado exitosamente por favor melissa salgamos trabajas en el afa y donde trabajo te veo siempre me enamore y como me miras me enamoras mas")
print("=" * 60)