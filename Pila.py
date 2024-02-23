class Pila:
  
  def __init__(pilas):
    pilas.__pila = []

  def agregar(pilas, elemento):
    pilas.__pila.append(elemento)

  def eliminar(pilas):
    return pilas.__pila.pop()

  def validar_vacia(pilas):
    return len(pilas.__pila) == 0

  def obtener_tamanio(pilas):
    return len(pilas.__pila)

  def imprimir(pilas):
    for elemento in pilas.__pila:
      print(elemento)

#-------------------------------------------------------------------
pila = Pila()
pila.agregar(15)
pila.agregar(30)
pila.agregar(60)

print("Tamaño de la pila:", pila.obtener_tamanio())

pila.imprimir()

print("Elemento eliminado:", pila.eliminar())

print("Pila después de eliminar un elemento:")
pila.imprimir()

print("¿La pila está vacía?:", pila.validar_vacia())
