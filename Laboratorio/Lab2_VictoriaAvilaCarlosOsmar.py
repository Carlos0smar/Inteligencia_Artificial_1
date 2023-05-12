
import random
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
        self.padre = accion

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

# Produce los números aleatorios para desifrar la contraseña
def produceNum(solucion_):
    aux=[]
    c = False
    while c == False:
        aleatorio=random.randint(0, 9)
        if aleatorio in solucion_ :
            if solucion.count(aleatorio) > aux.count(aleatorio):
                aux.append(aleatorio)
                if len(aux)==len(solucion_):
                    c = True;1
    return aux


def busqueda_BPPR(nodo_inicial, solucion, visitado):
    visitado.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:


        datos_nodo = nodo_inicial.get_estado()
        lista_hijos=[]
        for i in range(len(datos_nodo)-1):
            hijo = list(datos_nodo)  # crea una copia de la lista original
            hijo[i], hijo[i+1] = hijo[i+1], hijo[i]  # intercambia los elementos i e i+1
            hijo_nodo = Nodo(hijo)
            lista_hijos.append(hijo_nodo)
        nodo_inicial.set_hijo(lista_hijos)


        for nodo_hijo in nodo_inicial.get_hijo():
            if not nodo_hijo.get_estado() in visitado:
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, solucion, visitado)
                if Solution is not None:
                    return Solution
        return None

if __name__ == "__main__":


    solucion = input("introduce la solucion: ")
    solucion = list(map(int,solucion.split(",")))
    estado_inicial = produceNum(solucion)
    nodo_solucion = None
    visitado = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_actual = busqueda_BPPR(nodo_inicial, solucion, visitado)

    # Mostrar Resultado
    resultado = []
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)