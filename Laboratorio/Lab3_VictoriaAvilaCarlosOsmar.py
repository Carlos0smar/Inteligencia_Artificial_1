import time
# Laboratorio 3
# Inteligencia Artificial
# Alumno: Victoria Avila Carlos Osmar



# A partir del codigo de rompecabezas lineal, para n digitos, aplicar una heuristica y resolver el mismo, identificando, cual es 
# la capacidad maxima de resolucion y el tiempo que aplica para dicho proposito. Debe probar al menos 3 heuristicas diferentes, pueden ser las recomendadas en 
# clase u otra considere adecuada y demostrar cual el la mejor de las tres.


# ES UN BUSQUEDA BPA PARA N NUMEROS
# libreria para medir el tiempo
class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo
    
    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre
    
    def set_accion(self, accion):
        self.accion = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_estado())

# función que intercambia dos elementos de una lista
def intercambiar(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop()
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        cont = 0
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            lista_hijos=[]
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # ciclo while que recorre el estado del nodo actuals
            while cont < (len(estado_inicial)-1):
                cont+=1
                hijo = list(estado_nodo) # Crear una copia de la lista para evitar modificar el estado original
                intercambiar(hijo, cont-1, cont) # Intercambiar los elementos en las posiciones 0 y 1
                hijo_1 = Nodo(hijo)
                lista_hijos.append(hijo_1)

# De la heuristica 1
                if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera) and heuristica_1(nodo_actual, hijo_1) :
                    nodos_frontera.append(hijo_1)


# De la heuristica 2
                # if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera) and heuristica_2(nodo_actual, hijo_1) :
                #     nodos_frontera.append(hijo_1)


# De la heuristica 3
                # if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera) and heuristica_3(nodo_actual, hijo_1) :
                #     nodos_frontera.append(hijo_1)

            nodo_actual.set_hijo(lista_hijos)




#heuristica 1 que determina si la calidad del hijo es mayor que el padre
def heuristica_1(padre_node, hijo_node):
    calidadPadre = 0
    calidadHijo = 0
    padre_data = padre_node.get_estado()
    hijo_data = hijo_node.get_estado()

    for n in range(1, len(padre_data)):
        if padre_data[n] > padre_data[n - 1]:
            calidadPadre += 1
        if hijo_data[n] > hijo_data[n - 1]:
            calidadHijo += 1

    if calidadHijo >= calidadPadre:
        return True
    else:
        return False


# heuristica 2 que determina si la calidad del hijo es mayor que el padre, calculando la distancia de cada elemento a su posicion correcta
#Porblema: es lento y no es eficiente, me hubiera gustado implementar el algoritmo de A* pero aún no tube la idea completa de como hacerlo
def heuristica_2(padre_node, hijo_node):
    padre_data = padre_node.get_estado()
    hijo_data = hijo_node.get_estado()
    cont_padre = 0
    cont_hijo = 0
    for i in range(len(padre_data)):
        x = padre_data[i]
        n = int(x)-1
        j=i
        while n != j:
            if n < j:
                j-=1
            else:
                j+=1
            cont_padre += j
    
    for i in range(len(hijo_data)):
        x = hijo_data[i]
        n = int(x)-1
        j=i
        while n != j:
            if n < j:
                j-=1
            else:
                j+=1
            cont_hijo += j
    
    return cont_hijo <= cont_padre




#heuristica 3 determina si el elemento está en su posición correcta
#problemas: no funciona con numeros impares ya que estos producen repetidos
def heuristica_3(padre_node, hijo_node):
    calidadPadre = 0
    calidadHijo = 0
    padre_data = padre_node.get_estado()
    hijo_data = hijo_node.get_estado()

    for n in range(len(padre_data)):
        if n == int(padre_data[n])-1 :
            calidadPadre += 1
        if n == int(hijo_data[n])-1:
            calidadHijo += 1

    return calidadHijo >= calidadPadre




if __name__ == "__main__":
    # Se pedirán los datos al usuario
    elementos_iniical = input("Introduce los numeros a ordenar separados por comas: ") 
    estado_inicial = elementos_iniical.split(",")
    
    elementos_solucion = input("Introduce la solución separados por comas: ")
    solucion= elementos_solucion.split(",")

    #empezar a contar el tiempo
    start_time = time.time()
    # ejecutar la busqueda
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    # busqueda de nodos padres para ser impresos
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print("El camino para llegar a la solución es: ")
    print(resultado)
    # terminar de contar el tiemp
    end_time = time.time()
    # calcular el tiempo transcurrido
    elapsed_time = end_time - start_time
    # imprimir el tiempo transcurrido
    print(f"Tiempo transcurrido: {elapsed_time} segundos")