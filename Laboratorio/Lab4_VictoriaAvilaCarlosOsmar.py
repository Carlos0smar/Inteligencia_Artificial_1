import heapq
import time
import random

def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

def string_to_list(string_):
    return [row.strip().split('-') for row in string_.split('\n')]

def find_location(inicio, objetivo):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       Devuelve una tupla: fila, columna'''
    for f in range(len(inicio)):
      for c in range(len(inicio[f])):
          if (inicio[f][c] ) != (objetivo[f][c] ):
              if(inicio[f][c] == "/" or inicio[f][c] == "\\"):
                return f , c

class ColaPrioridadLimitada(object):
  def __init__(self, limite=None, *args):
    self.limite = limite
    self.queue = list()

  def __getitem__(self, val):
    return self.queue[val]

  def __len__(self):
    return len(self.queue)

  def append(self, x):
    heapq.heappush(self.queue, x)
    if self.limite and len(self.queue) > self.limite:
      self.queue.remove(heapq.nlargest(1, self.queue)[0])

  def pop(self):
    return heapq.heappop(self.queue)

  def extend(self, iterable):
    for x in iterable:
      self.append(x)

  def clear(self):
    for x in self:
      self.queue.remove(x)

  def remove(self, x):
    self.queue.remove(x)

  def sorted(self):
    return heapq.nsmallest(len(self.queue), self.queue)

class EigthPuzzleProblem(object):
  def __init__(self, estado_inicial, estado_objetivo):
    self.estado_inicial = estado_inicial
    self.estado_objetivo = estado_objetivo

  def acciones(self, estado):
    '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
    # fila_e, columna_e = find_location(filas, 'e')
    estado_ = estado
    acciones = [] 
    row, column = find_location(estado_, self.estado_objetivo)
    if row > 0:
        if estado_[row - 1][column] is None:
            acciones.append([row - 1, column])
        elif estado_[row - 2][column] == None:
          acciones.append([row - 2, column])
    if row < 3:
        if estado_[row + 1][column] is None:
            acciones.append([row + 1, column])
        elif estado_[row + 2][column] == None:
          acciones.append([row + 2, column])
    if column > 0:
        if estado_[row][column - 1] is None:
            acciones.append([row, column - 1])
        elif estado_[row][column - 2] == None:
          acciones.append([row, column - 2])
    if column < 3:
        if estado_[row][column + 1] is None:
          acciones.append([row, column + 1])
        elif estado_[row][column + 2] == None:
          acciones.append([row, column + 2])

    return acciones

  def resultado(self, estado, accion):
    '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
    '''
    estado_ = estado
    row, column = find_location(estado_, self.estado_objetivo)

    # la accion es una tupla (fila, columna)
    fila_n, columna_n = accion

    estado_[row][column], estado_[fila_n][columna_n] = estado_[fila_n][columna_n], estado_[row][column]

    return estado_

  def es_objetivo(self, estado):
    '''Devuelve True si un estado es el estado_objetivo.'''
    return estado == self.estado_objetivo

  def costo(self, estado1, accion, estado2):
    '''Devuelve el costo de ejecutar una accion. 
    '''
    return 1

  def heuristica(self, estado):
    '''Devuelve una estimacion de la distancia
    de un estado a otro, utilizando la distancia manhattan.
    '''

    # distancia = 0
    row, column = find_location(estado, self.estado_objetivo)

    fila_n1_objetivo, col_n1_objetivo = posiciones_objetivo[0]
    fila_n_objetivo, col_n_objetivo = posiciones_objetivo[1]

    distancia1 = abs(row - fila_n1_objetivo) + abs(column - col_n1_objetivo)
    distancia = abs(row - fila_n_objetivo) + abs(column - col_n_objetivo)
    if distancia1 < distancia:
      return distancia1
    else:
      return distancia

  def estado_representacion(self, estado):
    """
    Devuelve un string de representacion de un estado.
    Por defecto devuelve str(estado).
    """
    return str(estado)

class NodoBusqueda(object):
    '''Nodo para el proceso de busqueda.'''

    def __init__(self, estado, padre=None, accion=None, costo=0, problema=None, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo = costo
        self.problema = problema or padre.problema
        self.profundidad = profundidad

    def expandir(self, busqueda_local=False):
        '''Crear sucesores.'''
        nodos_nuevos = []
        for accion in self.problema.acciones(self.estado):
            estado_nuevo = self.problema.resultado(self.estado, accion)
            costo = self.problema.costo(self.estado, accion, estado_nuevo)
            fabrica_nodos = self.__class__
            nodos_nuevos.append(fabrica_nodos(estado=estado_nuevo,
                                        padre=None if busqueda_local else self,
                                        problema=self.problema,
                                        accion=accion,
                                        costo=self.costo + costo,
                                        profundidad=self.profundidad + 1))
        return nodos_nuevos

    def camino(self):
        '''Camino (lista de nodos y acciones) desde el nodo raiz al nodo actual.'''
        nodo_actual = self
        camino = []
        while nodo_actual:
            camino.append((nodo_actual.accion, nodo_actual.estado))
            nodo_actual = nodo_actual.padre
        return list(reversed(camino))

    def __eq__(self, otro):
        return isinstance(otro, NodoBusqueda) and self.estado == otro.estado

    def estado_representacion(self):
        return self.problema.estado_representacion(self.estado)

    def accion_representacion(self):
        return self.problema.accion_representacion(self.accion)

    def __repr__(self):
        return 'Node <%s>' % self.estado_representacion().replace('\n', ' ')

    def __hash__(self):
        return hash((
            self.estado,
            self.padre,
            self.accion,
            self.costo,
            self.profundidad,
        ))

class NodoBusquedaHeuristicaOrdenado(NodoBusqueda):
    def __init__(self, *args, **kwargs):
        super(NodoBusquedaHeuristicaOrdenado, self).__init__(*args, **kwargs)
        self.heuristica = self.problema.heuristica(self.estado)

    def __lt__(self, otro):
        return self.heuristica < otro.heuristica

class NodoBusquedaEstrellaOrdenado(NodoBusquedaHeuristicaOrdenado):
    def __lt__(self, otro):
        return self.heuristica + self.costo < otro.heuristica + otro.costo

def busqueda_AEstrella(problema): 
  limite_profundidad = None
  busqueda_en_grafo = False
  reemplazar_grafo_cuando_mejor = True
  # frontera = ColaPrioridadLimitada()
  frontera = []
  nodos_visitados = []

  nodo_inicio = NodoBusquedaEstrellaOrdenado(estado=problema.estado_inicial, problema=problema)
  frontera.append(nodo_inicio)
  while frontera:
    nodo_actual = frontera.pop(0)
    # print("###"*20)
    # print(nodo_actual.estado)
    # print(problema.estado_objetivo)

    if problema.es_objetivo(nodo_actual.estado):
      return nodo_actual
    
    nodos_visitados.append(nodo_actual.estado)

    if limite_profundidad is None or nodo_actual.profundidad < limite_profundidad:
      nodos_expandidos = nodo_actual.expandir()

      for n in nodos_expandidos:
        if busqueda_en_grafo:
          otros_nodos = [x for x in frontera if x.estado == n.estado]
          assert len(otros_nodos) in (0, 1)
          if n.estado not in nodos_visitados and len(otros_nodos) == 0:
            frontera.append(n)
          elif reemplazar_grafo_cuando_mejor and len(otros_nodos) > 0 and n < otros_nodos[0]:
            frontera.remove(otros_nodos[0])
            frontera.append(n)
        else:
          frontera.append(n)

if __name__ == "__main__":
  EMPTY = None
  estado_inicial = [[EMPTY, "\\", EMPTY, EMPTY],
                    ["\\", "/","\\", EMPTY],
                    ["/", "\\", "/", EMPTY],
                    [EMPTY, "/", EMPTY, EMPTY]]


  estado_objetivo = [[EMPTY, EMPTY, EMPTY, EMPTY],
                    [EMPTY, "/","\\", EMPTY],
                    ["/", "\\", "/", "\\"],
                    [EMPTY, "/", "\\", EMPTY]]
  


  posiciones_objetivo = []
  for f in range(len(estado_inicial)):
    for c in range(len(estado_inicial[f])):
        if (estado_inicial[f][c] ) != (estado_objetivo[f][c] ):
          if(estado_inicial[f][c] == None): 
            posiciones_objetivo.append([f,c])
            
  problema = EigthPuzzleProblem(estado_inicial, estado_objetivo)
  resultado = busqueda_AEstrella(problema)

  for row in resultado:
    for element in row:
        if element is  None:
            element = " "
        print(element, end=" ")
    print()        
    
