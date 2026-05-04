# listas #
# ejemplo 1 creacion y acceso

tareas = ["estudiar","ejercicio","programar","descansar"]
primera   = tareas[0]    # "estudiar"
ultima    = tareas[-1]   # "descansar"
penultima = tareas[-2]   # "programar"

print(len(tareas))           # 4
print("programar" in tareas) # True
print(tareas.count("ejercicio")) # 1
print(tareas.index("programar")) # 2

#ejemplo 2 metodos para añadir
tareas = ["estudiar", "ejercicio"]
tareas.append("programar")         # añade al final
tareas.insert(0, "llamar médico")  # inserta al inicio
tareas.extend(["lavar ropa", "cocinar"])

# append vs extend — diferencia importante
a = [1, 2, 3]
a.append([4, 5])   # → [1, 2, 3, [4, 5]]  ← lista anidada
a = [1, 2, 3]
a.extend([4, 5])   # → [1, 2, 3, 4, 5]    ← elementos sueltos

#ejemplo 3 metodos para eliminar

colores = ["rojo", "verde", "azul", "verde"]
colores.remove("verde")  # → ["rojo", "azul", "verde"]

nums = [10, 20, 30, 40]
ultimo  = nums.pop()   # retorna 40 → nums = [10, 20, 30]
segundo = nums.pop(1)  # retorna 20 → nums = [10, 30]

mi_lista = [1, 2, 3, 4]
mi_lista.clear()         # → []

#ejemplo 4 ordenar y organizar

nums = [3, 1, 4, 2]
nums.sort()              # [1, 2, 3, 4] — modifica la original
nums.sort(reverse=True)  # [4, 3, 2, 1]

letras = ["c", "a", "b"]
letras.reverse()         # ["b", "a", "c"]

original = [3, 1, 4, 2]
nueva = sorted(original) # nueva = [1, 2, 3, 4]
print(original)          # [3, 1, 4, 2] — sin cambios

#ejemplo 5 recorrido de listas
frutas = ["manzana", "plátano", "naranja"]
for f in frutas:
    print(f"Me gusta {f}")

for i, f in enumerate(frutas, 1):
    print(f"{i}. {f}")

nombres = ["Ana","Carlos","Elena"]
edades  = [28, 35, 23]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad} años")

cuadrados = [n**2 for n in range(5)]  # [0,1,4,9,16]
pares = [n for n in range(10) if n%2==0]

#ejemplo 6 modificacion y copias

# Problema de referencia compartida
a = [1, 2, 3]
b = a        # misma referencia
b[0] = 100
print(a)     # [100, 2, 3] — ¡a también cambió!

# Solución: copy()
a = [1, 2, 3]
b = a.copy()
b[0] = 100
print(a)     # [1, 2, 3] — intacta

# Listas anidadas → deepcopy
import copy
anidada = [[1, 2], [3, 4]]
deep = copy.deepcopy(anidada)
deep[0][0] = 99
print(anidada) # [[1, 2], [3, 4]] — intacta

#reto
#estión de inventario

##Construye un sistema de inventario usando listas anidadas que gestione productos, precios y stock.

#1 Define inventario como lista de sublistas [ nombre, cantidad, precio ]
#2 Implementa actualizar_precio() para modificar el precio de un producto
#3 Implementa registrar_venta() descontando stock si hay suficiente
#4 Implementa añadir_producto() añadiendo o actualizando el stock
#5 Implementa mostrar_inventario() e imprime el estado final#

#1 Define inventario como lista de sublistas [ nombre, cantidad, precio ]
inventario = [
    ["camisa de miau",   30, 2500],
    ["zapato de futbol",   20, 8000],
    ["celular chino",  10, 9500],
]


#2 Implementa actualizar_precio() para modificar el precio de un producto
inventario[1][2] = 7500
print("ahora el precio actualizado del zapatico te vale $7500")

#3 Implementa registrar_venta() descontando stock si hay suficiente
if inventario[0][1] >= 8:
    inventario[0][1] -= 8
    print("Venta registrada: 3 x  camisa de miau | Stock restante:", inventario[0][1])
else:
    print("Stock insuficiente")

#4 Implementa añadir_producto() añadiendo o actualizando el stock
inventario.append(["audifono gringo", 15, 12000])
print("'audifono' agregado al inventario")

#5 Implementa mostrar_inventario() e imprime el estado final#
print("\n--- inventario ---")
for nombre, cantidad, precio in inventario:
    print(nombre, cantidad, precio)


#lo que hize ver la guia del profesor donde esta todo documentado y guiarme con la explicacion