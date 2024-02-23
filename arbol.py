class ArbolBinario:
  def __init__(arbol, valor):
    
    arbol.__valor = valor
    arbol.__izquierdo = None
    arbol.__derecho = None

  def insertar(arbol, valor):
    
    if valor < arbol.__valor:
      if arbol.__izquierdo is None:
        arbol.__izquierdo = ArbolBinario(valor)
      else:
        arbol.__izquierdo.insertar(valor)
    else:
      if arbol.__derecho is None:
        arbol.__derecho = ArbolBinario(valor)
      else:
        arbol.__derecho.insertar(valor)

  def buscar(arbol, valor):
    
    if valor == arbol.__valor:
      return True
    elif valor < arbol.__valor:
      if arbol.__izquierdo is None:
        return False
      else:
        return arbol.__izquierdo.buscar(valor)
    else:
      if arbol.__derecho is None:
        return False
      else:
        return arbol.__derecho.buscar(valor)

  def recorrer_inorden(arbol):
    if arbol.__izquierdo is not None:
      arbol.__izquierdo.recorrer_inorden()
    print(arbol.__valor)
    if arbol.__derecho is not None:
      arbol.__derecho.recorrer_inorden()


#-------------------------------------------------

arbol = ArbolBinario(10)
arbol.insertar(50)
arbol.insertar(100)
arbol.insertar(75)
arbol.insertar(150)

print("Valor buscado:", 25)
print("¿El valor está en el árbol?:", arbol.buscar(25))

print("Recorrido inorden:")
arbol.recorrer_inorden()
