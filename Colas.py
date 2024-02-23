class Cola:

  def __init__(colas):
    colas.__cola = []

  def agregar(colas, elemento):

    colas.__cola.append(elemento)

  def eliminar(colas):
 
    return colas.__cola.pop(0)

  def validar_vacio(colas):
 
    return len(colas.__cola) == 0

  def obtener_tamanio(colas):

    return len(colas.__cola)

  def imprimir(colas):

    for elemento in colas.__cola:
      print(elemento)


#-------------------------------------------------------------------------

cola = Cola()
cola.agregar(12)
cola.agregar(24)
cola.agregar(48)

print("Tamaño de la cola:", cola.obtener_tamanio())

cola.imprimir()

print("Elemento eliminado:", cola.eliminar())

print("Cola después de eliminar un elemento:")
cola.imprimir()

print("¿La cola está vacía?:", cola.validar_vacio())
