import numpy as np
import math
import matplotlib.pyplot as plot
def canicas(m, v, c):
    # Funcion que efectua el experimento de la doble rendija.
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