import numpy as np
import math
def suma_vectores_complejos(v1, v2):
    # Efectua la suma de dos vectores complejos v1[a,b], v2[c, d] donde a y c es la parte real y b y d la parte imaginaria.
    preal = v1[0] + v2[0]
    pimg = v1[1] + v2[1]
    c = [preal, pimg]
    return pretty_sum_veccom(c)

def pretty_sum_veccom(c):
    if c[0] > 0 and c[1] > 0:
        return(str(c[0]) + "+" + str(c[1]) + "i")
    elif c[1] < 0:
        return(str(c[0]) + str(c[1]) + "i")
    elif c[0] < 0 and c[1] < 0:
        return("-" + str(c[0]) + "-" + str(c[1]) + "i")
    elif c[0] < 0:
        return("-" + str(c[0]) + "+" + str(c[1]) + "i")
    elif c[0] == 0 and c[1] != 0:
        return(str(c[1]) + "i")
    elif c[1] == 0:
        return(str(c[0]))
    elif c[0] == 0 and c[1] == 0:
        return(str(0))

# Ejemplo, ejecute la suma de los vectores 3-i + 5+2i.
#print(suma_vectores_complejos([3,-1],[5,2]))

def inver_aditivo_veccom(v1):
    # Funcion que retorna el inverso aditivo de un vector complejo v1[a, b] donde a es la parte real y b la parte imaginaria.
    a = (v1[0] * -1), (v1[1] * -1)
    return pretty_inverad(a)

def pretty_inverad(a):
    if a[0] > 0 and a[1] > 0:
        return(str(a[0]) + "+" + str(a[1]) + "i" )
    elif a[0] < 0 and a[1] < 0:
        return(str(a[0]) + str(a[1]) + "i")
    elif a[0] < 0 and a[1] > 0:
        return(str(a[0]) + "+" + str(a[1]) + "i" )
    elif a[0] > 0 and a[1] < 0:
        return(str(a[0]) + str(a[1]) + "i")
    elif a[0] == 0 and a[1] != 0:
        return(str(a[1]) + "i")
    elif a[1] == 0:
        return(str(a[0]))
    elif a[0] == 0 and a[1] == 0:
        return(str(0))

# Ejemplo, obtener el inverso aditivo del vector 3+5i.
#print(inver_aditivo_veccom([3,5]))

def escalar_por_veccom(n, v1):
    # Funcion que calcula la multiplicación de un escalar (n) por un vector complejo v1[a, b] donde a es la parte real y b la parte imaginaria.
    a = []
    for i in range(len(v1)):
        produc = n * v1[i]
        a.append(produc)
    return pretty_escalarXveccom(a)

def pretty_escalarXveccom(a):
    if a[0] > 0 and a[1] > 0:
        return(str(a[0]) + "+" + str(a[1]) + "i" )
    elif a[0] < 0 and a[1] < 0:
        return(str(a[0]) + str(a[1]) + "i")
    elif a[0] < 0 and a[1] > 0:
        return(str(a[0]) + "+" + str(a[1]) + "i" )
    elif a[0] > 0 and a[1] < 0:
        return(str(a[0]) + str(a[1]) + "i")
    elif a[0] == 0 and a[1] != 0:
        return(str(a[1]) + "i")
    elif a[1] == 0:
        return(str(a[0]))
    elif a[0] == 0 and a[1] == 0:
        return(str(0))

# Ejemple, multiplicar el vector 3+5i por 3.
#print(escalar_por_veccom(3, [3,5]))

def suma_matrices_complejas(m1, m2):
    # Funcion que calcula la suma entre dos matrices complejas con la misma dimension m1[[a+bj, c+dj][e+fj, g+hj]] y m2[[a2+b2j, c2+d2j][e2+f2j, g2+h2j]]
    # donde el numero acompañado por la j es la parte imaginaria.
    a = np.array(m1)
    n, m = a.shape
    matriz_sum = []
    for i in range(n):
        for j in range(m):
            b = m1[i][j] + m2[i][j]
            matriz_sum.append(b)
    return matriz_sum
# Ejemplo, sumar las matrices complejas [[2+3i, 4+5i],[2+5i, 8+7i]] + [[2+4i, 2+7i],[5+9i, 3+1i]].
#print(suma_matrices_complejas([[2+3j, 4+5j],[2+5j, 8+7j]],[[2+4j, 2+7j],[5+9j, 3+1j]]))

def inver_ad_matcom(m1):
    # Funcion que retorna el inverso aditivo de una matriz compleja m1[[a+bj, c+dj][e+fj, g+hj]], donde el numero acompañado por la j representa la parte imaginaria.
    a = np.array(m1)
    f, c = a.shape
    for i in range(f):
        for j in range(c):
            m1[i][j] = m1[i][j] * -1
    return m1
# Ejemplo, retornar el inverso aditivo de la matriz compleja [[2+3i, 4+5i],[2+5i, 8+7i]].
#print(inver_ad_matcom([[2+3j, 4+5j],[2+5j, 8+7j]]))

def escalar_X_matcom(n, m1):
    # Funcion que retorna el producto escalar de un numero n por una matriz compleja m1[[a+bj, c+dj][e+fj, g+hj]], donde el numero acompañado por la j representa la parte imaginaria.
    a = np.array(m1)
    f, c = a.shape
    for i in range(f):
        for j in range(c):
            m1[i][j] = m1[i][j] * n
    return m1

# Ejemplo, multiplicar la matriz compleja [[2+3i, 4+5i],[2+5i, 8+7i]] por 2
#print(escalar_X_matcom(2, [[2+3j, 4+5j],[2+5j, 8+7j]]))

def transpuesta_matcom_veccom(mv1):
    # Funcion que retorna la transpues de una matriz compleja o un vector complejo.
    a = np.array(mv1)
    f, c = a.shape
    for i in range(f):
        for j in range(c):
            mv1[i][j] = mv1[j][i]
    return mv1

# Ejemplo, obtener la traspuesta de la matriz compleja [[2+3i, 4+5i],[2+5i, 8+7i]].
#print(transpuesta_matcom_veccom([[2+3j, 4+5j],[2+5j, 8+7j]]))

def conjugado_matcom_veccom(mv1):
    # Funcion que retorna el conjugado de una matriz compleja o un vector complejo.
    a = np.array(mv1)
    f, c = a.shape
    for i in range(f):
        for j in range(c):
            mv1[i][j] = np.conj(mv1[i][j])
    return mv1
# Ejemplo, obtener el conjugado de la matriz compleja [[2+3i, 4+5i],[2+5i, 8+7i]].
#print(conjugado_matcom_veccom([[2+3j, 4+5j],[2+5j, 8+7j]]))

def daga_matcom_veccom(mv1):
    # Funcion que retorna la adjunta de una matriz compleja o un vector complejo.
    a = np.array(mv1)
    f, c = a.shape
    for i in range(f):
        for j in range(c):
            mv1[i][j] = np.conj(mv1[i][j])
    for i in range(f):
        for j in range(c):
            mv1[i][j] = mv1[j][i]
    return mv1
# Ejemplo, obtener la adjunta de la matriz compleja [[2+3i, 4+5i],[2+5i, 8+7i]].
#print(daga_matcom_veccom([[2+3j, 4+5j],[2+5j, 8+7j]]))

def prod_matcom(m1, m2):
    # Funcion que retorna el producto entre dos matrices solo si estas son compatibles, si no se cumple, retorna un mensaje "No es posible".
    m1 = np.array(m1)
    m2 = np.array(m2)
    f1, c1 = m1.shape
    f2, c2 = m2.shape
    if c1 == f2:
        return np.dot(m1, m2)
    elif c1 != f2:
        return "No es posible"

# Ejemplo, 1) Efectuar el producto entre una matriz 2X3 y una matriz 3X5 (Si es posible) 2) Ejectuar el producto entre una matriz 2X3 y una matriz 2X2 (No es posible).
#Ejemplo 1:
#print(prod_matcom([[2+3j, 4+5j, 9+4j],[2+5j, 8+7j, 8+3j]],[[2+4j, 2+7j, 6+4j, 7+1j, 3+3j],[5+9j, 3+1j, 9+9j, 7+3j, 15+1j],[2+1j, 3+4j, 9+5j, 6+7j, 1+1j]]))
#Ejemplo 2:
#print(prod_matcom([[2+3j, 4+5j, 9+4j],[2+5j, 8+7j, 8+3j]],[[2+4j, 2+7j],[5+9j, 3+1j]]))

def accion_mat_vec(m1, v1):
    return 0

def prod_interno_veccom(v1, v2):
    # Funcion que retorna el producto interno entre dos vectores.
    for i in range(len(v1)):
        v1[i] = np.conj(v1[i])
    for i in range(len(v2)):
         v2[i] = np.conj(v2[i])
    a = np.array(v1)
    b = np.array(v2)
    c = a * b
    suma = 0+0j
    for i in range(len(c)):
        a = c[i]
        suma = suma + a
    return str(suma)
# Ejemplo, 1) Calcule el producto interno entre los vectores [1+3i, 2i, 3i] y [2+1i, 3+5i, 4-5i] 2) Calcule el producto interno entre los vectores [-3, 5] y [2, -4].
#Ejemplo 1:
#print(prod_interno_veccom([1+3j,2j,3j], [2+1j,3+5j,4-5j]))
#Ejemplo 2:
#print(prod_interno_veccom([-3, 5], [2, -4]))

def norma_vector(v1):
    #funcion que entrega la norma de un vector.
    for i in range(len(v1)):
        v1[i] = v1[i]**2
    suma = 0
    for i in range(len(v1)):
        a = v1[i]
        suma = suma + a
    return str(math.sqrt(suma))

# Ejemplo, Calcule la norma del vector [3, 5, 4].
#print(norma_vector([3,5,4]))

def dist_dos_vec(v1, v2):
    # Funcion que retorna la distancia entre dos vectores.
    vector_v1_v2 = []
    for i in range(len(v1)):
        a = v1[i] - v2[i]
        vector_v1_v2.append(a)
    for i in range(len(vector_v1_v2)):
        vector_v1_v2[i] = vector_v1_v2[i]**2
    suma = 0
    for i in range(len(vector_v1_v2)):
        a = vector_v1_v2[i]
        suma = suma + a
    return str(math.sqrt(suma))

# Ejemplo, Calcule la distancia entre los vectores [-1,0,4] y [1,-2,-3]
#print(dist_dos_vec([-1,0,4], [1,-2,-3]))

def matriz_unitaria(m1):
    return 0
def matriz_hermitiana(m1):
    return 0
def prod_tensor_matrices(m1, m2):
    return 0
def prod_tensor_vectores(v1, v2):
    return 0