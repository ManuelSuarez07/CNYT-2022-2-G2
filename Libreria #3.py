import numpy as np
import math
import matplotlib.pyplot as plot
def canicas(m, v, c):
    # Funcion que efectua el experimento de las canicas con coeficiente booleanos
    # m = Matriz dada, v = Vector, c = Numero de clicks.
    m = np.array(m)
    v = np.array(v)
    v = np.array([v])
    v = (v.T)
    mult = v
    resp = 0
    for i in range(0, c):
        resp = np.dot(m,mult)
        mult = resp
    return resp

print(canicas([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]], [6,2,1,5,3,10], 1))

def clasico_probabilistico(m, v, c):
    # Funcion que realiza el experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
    # m = Matriz dada, v = Vector, c = Numero de clicks.
    m = np.array(m)
    v = np.array(v)
    v = np.array([v])
    v = (v.T)
    f1, c1 = m.shape
    f2, c2 = v.shape
    for i in range(c):
        if c1 == f2:
            vector = np.dot(m, v)
        elif c1 != f2:
            return "No es posible"
    return vector

def norma_vector(v):
    # Funcion que calcula la norma de un vector.
    # v = vector.
    for i in range(len(v)):
        v[i] = v[i]**2
    suma = 0
    for i in range(len(v)):
        a = v[i]
        suma = suma + a
    return math.sqrt(suma)

def multiples_rendijas_cuantico(m, v, c):
    # Funcion que realiza el experimento de las múltiples rendijas cuántico.
    # m = Matriz dada, v = Vector, c = Numero de clicks.
    m = np.array(m)
    v = np.array(v)
    v = np.array([v])
    v = (v.T)
    f1, c1 = m.shape
    f2, c2 = v.shape
    probabilidades = []
    for i in range(c):
        if c1 == f2:
            vector = np.dot(m, v)
        elif c1 != f2:
            return "No es posible"
    for elemento in vector:
        elemento = (norma_vector([elemento])[0])**2
        probabilidades = probabilidades + [elemento]
    return probabilidades

def graf_diagrama(v):
    # Funcion que crea y guarda un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se guarda en el computador con un formato de imagen.
    ejes = len(v)
    x = np.array([x for x in range(ejes)])
    y = np.array([round(v[x]*100, 3) for x in range(ejes)])
    plot.bar(x, y, color="gray", align="center")
    plot.title("Vector_Probabilidades")
    plot.savefig("Vector_Probabilidades.png")
    plot.show()