import math
import numpy as np
#El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea.
#El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

def norma_veccom(vector):
    #Funcion que calcula la norma de un vector complejo
    vec_conj = []
    for i in range(len(vector)):
        a = np.conj(vector[i])
        vec_conj.append(a)
    vec_daga = np.array(vec_conj)
    vec_daga = np.array([vec_daga])
    vec_daga = (vec_daga.T)
    norma = np.dot(vector, vec_daga)
    norma = norma.real
    norma = math.sqrt(norma)
    return norma

def prob_pos(vector, xi):
    # Funcion que calcula la probabilidad de encontrarlo en una posición en particular
    norma = norma_veccom(vector)
    modulo = abs(vector[xi])
    a = modulo ** 2
    b = norma ** 2
    a = int(a)
    b = int(b)
    probabilidad = a / b
    return probabilidad
#print(prob_pos([-3-1j,0+-2j,0+1j,2+0j], 2))

def vec_to_vec(v1, v2):
    # Funcion que efectua la siguiente operacion, si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
    vec_conj1 = []
    for i in range(len(v1)):
        a = np.conj(v1[i])
        vec_conj1.append(a)
    vec_daga1 = np.array(vec_conj1)
    vec_daga1 = np.array([vec_daga1])
    vec_daga1 = (vec_daga1.T)
    norma1 = np.dot(v1, vec_daga1)
    norma1 = norma1.real
    norma1 = math.sqrt(norma1)
    vec_conj2 = []
    for i in range(len(v2)):
        a = np.conj(v2[i])
        vec_conj2.append(a)
    vec_daga2 = np.array(vec_conj2)
    vec_daga2 = np.array([vec_daga2])
    vec_daga2 = (vec_daga2.T)
    norma2 = np.dot(v2, vec_daga2)
    norma2 = norma2.real
    norma2 = math.sqrt(norma2)
    #print(norma1, norma2)
    for i in range(len(v1)):
        v1[i] = v1[i]/norma1
    for i in range(len(v2)):
        v2[i] = v2[i]/norma2
    vec_prod_int = np.dot(v1,v2)
    #print(vec_prod_int)
    return vec_prod_int.round(0)

#print(vec_to_vec([0-(1j/math.sqrt(2)), (1/math.sqrt(2))+0j],[(1/math.sqrt(2))+0j, 0-(1j/math.sqrt(2))]))
#El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea.
#El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

def norma_veccom(vector):
    #Funcion que calcula la norma de un vector complejo
    vec_conj = []
    for i in range(len(vector)):
        a = np.conj(vector[i])
        vec_conj.append(a)
    vec_daga = np.array(vec_conj)
    vec_daga = np.array([vec_daga])
    vec_daga = (vec_daga.T)
    norma = np.dot(vector, vec_daga)
    norma = norma.real
    norma = math.sqrt(norma)
    return norma
#print(norma_veccom([1/math.sqrt(2), (1/math.sqrt(2))*1j]))

def prob_pos(vector, xi):
    # Funcion que calcula la probabilidad de encontrarlo en una posición en particular
    norma = norma_veccom(vector)
    modulo = abs(vector[xi])
    a = modulo ** 2
    b = norma ** 2
    a = int(a)
    b = int(b)
    probabilidad = a / b
    return probabilidad
#print(prob_pos([-3-1j,0+-2j,0+1j,2+0j], 2))

def vec_to_vec(v1, v2):
    # Funcion que efectua la siguiente operacion, si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
    vec_conj1 = []
    for i in range(len(v1)):
        a = np.conj(v1[i])
        vec_conj1.append(a)
    vec_daga1 = np.array(vec_conj1)
    vec_daga1 = np.array([vec_daga1])
    vec_daga1 = (vec_daga1.T)
    norma1 = np.dot(v1, vec_daga1)
    norma1 = norma1.real
    norma1 = math.sqrt(norma1)
    vec_conj2 = []
    for i in range(len(v2)):
        a = np.conj(v2[i])
        vec_conj2.append(a)
    vec_daga2 = np.array(vec_conj2)
    vec_daga2 = np.array([vec_daga2])
    vec_daga2 = (vec_daga2.T)
    norma2 = np.dot(v2, vec_daga2)
    norma2 = norma2.real
    norma2 = math.sqrt(norma2)
    #print(norma1, norma2)
    for i in range(len(v1)):
        v1[i] = v1[i]/norma1
    for i in range(len(v2)):
        v2[i] = v2[i]/norma2
    vec_prod_int = np.dot(v1,v2)
    #print(vec_prod_int)
    return vec_prod_int.round(0)

#print(vec_to_vec([0-(1j/math.sqrt(2)), (1/math.sqrt(2))+0j],[(1/math.sqrt(2))+0j, 0-(1j/math.sqrt(2))]))

def amplitud_transicion(v1, v2):
    # Funcion que calcula Amplitud de transición.
    # El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación.
    vec_conj1 = []
    for i in range(len(v1)):
        a = np.conj(v1[i])
        vec_conj1.append(a)
    vec_daga1 = np.array(vec_conj1)
    vec_daga1 = np.array([vec_daga1])
    vec_daga1 = (vec_daga1.T)
    norma1 = np.dot(v1, vec_daga1)
    norma1 = norma1.real
    norma1 = math.sqrt(norma1)
    vec_conj2 = []
    for i in range(len(v2)):
        a = np.conj(v2[i])
        vec_conj2.append(a)
    vec_daga2 = np.array(vec_conj2)
    vec_daga2 = np.array([vec_daga2])
    vec_daga2 = (vec_daga2.T)
    norma2 = np.dot(v2, vec_daga2)
    norma2 = norma2.real
    norma2 = math.sqrt(norma2)
    for i in range(len(v1)):
        v1[i] = v1[i]/norma1
    for i in range(len(v2)):
        v2[i] = v2[i]/norma2
    vec_prod_int = np.dot(v1,v2)
    return vec_prod_int.round(0)

def matriz_hermitiana(matriz):
    # Funcion que verifica si una matriz es hermitiana
    matriz = np.array(matriz)
    a = np.array(matriz)
    a = np.conj(matriz)
    a = a.T
    if np.array_equal(a, matriz):
        return True
    return False
#print(matriz_hermitiana([[5,3+7j],[3-7j,2]]))

def media(matriz, vector):
    # Funcion que calcula la media de una matriz observable y un vector Ket.
    norma = norma_veccom(vector)
    for i in range(len(vector)):
        vector[i] = vector[i]/norma
    vec_conj = np.conj(vector)
    matriz = np.array(matriz)
    v = np.array(vector)
    v = np.array([v])
    v = (v.T)
    resp1 = np.dot(matriz,v)
    respuesta = np.dot(vec_conj, resp1)
    return respuesta.real

def varianza(matriz, vector):
    # Funcion que calcula la varianza de una matriz observable y un vector Ket.
    return 0

def matObservable_vecKet(matriz, vector):
    # Funcion que recive una matriz que describa un observable y un vector ket.
    # La funcion revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
    matriz = np.array(matriz)
    vector = np.array(vector)
    a = matriz_hermitiana(matriz)
    if a == True:
        b = media(matriz, vector)
        c = varianza(matriz, vector)
        print("La media es:")
        print(float(b))
        print("la varianza es:")
        print(float(c))
    elif a != True:
        return "La matriz no es hermitiana"
print(matObservable_vecKet([[0, -1j],[1j, 0]], [1/math.sqrt(2), (1/math.sqrt(2))*1j]))

#print([1/math.sqrt(2), (1/math.sqrt(2))*1j])
#[0.7071067811865475, 0.7071067811865475j]