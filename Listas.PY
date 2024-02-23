class Lista:

  def __init__(list):
    
    list.__lista = []

  def agregar(list, elemento):

    list.__lista.append(elemento)

  def eliminar(list, elemento):
    
    list.__lista.remove(elemento)

  def buscar(list, elemento):
    
    return elemento in list.__lista

  def obtener_tamanio(list):
    
    return len(list.__lista)

  def imprimir(list):
    
    for elemento in list.__lista:
      print(elemento)

  def ordenar(list):
    
    list.__lista.sort()

  def obtener_elemento(list, indice):
    
    return list.__lista[indice]


#-----------------------------------------------------------------------------
lista = Lista()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)

print("Tamaño de la lista:", lista.obtener_tamanio())

lista.imprimir()

print("Elemento en la posición 1:", lista.obtener_elemento(1))

lista.ordenar()

print("Lista ordenada:")
lista.imprimir()

lista.eliminar(5)

print("Lista después de eliminar el elemento 5:")
lista.imprimir()
