#Libreria que ejecuta operaciones entre numeros complejos c1[a, b], c2[c, d]. Donde el elemento en la posicion 0 tanta en c1 como en c2 representa la parte real, y el elemento en la posicion 1 de c1 y c2 representa la parte imaginaria
def suma_complejos(c1, c2):
    #Efectua la suma de dos numeros complejos c1, c2
    preal = c1[0] + c2[0]
    pimg = c1[1] + c2[1]
    c = [preal, pimg]
    return pretty_sum(c)
def pretty_sum(c):
    if c[0] > 0 and c[1] > 0:
        print(str(c[0]) + "+" + str(c[1]) + "i" )
    elif c[1] < 0:
        print(str(c[0]) + str(c[1]) + "i" )
    elif c[0] < 0 and c[1] < 0 :
        print("-" + str(c[0]) + "-" + str(c[1]) + "i")
    elif c[0] < 0:
        print("-" + str(c[0]) + "+" + str(c[1]) + "i")
    elif c[0] == 0 and c[1] != 0:
        print(str(c[1]) + "i")
    elif c[1] == 0:
        print(str(c[0]))
    elif c[0] == 0 and c[1] == 0:
        print(str(0))

def producto_complejos(c1, c2):
    #Efectua el producto entre dos numeros complejos c1, c2
    preal = (c1[0] * c2[0]) - (c1[1] * c2[1])
    pimg = (c1[0] * c2[1]) + (c1[1] * c2[0])
    b = [preal, pimg]
    return pretty_prod(b)
def pretty_prod(b):
    if b[0] > 0 and b[1] > 0:
        print(str(b[0]) + "+" + str(b[1]) + "i" )
    elif b[0] < 0 and b[1] < 0:
        print(str(b[0]) + str(b[1]) + "i")
    elif b[0] < 0 and b[1] > 0:
        print(str(b[0]) + "+" + str(b[1]) + "i" )
    elif b[0] > 0 and b[1] < 0:
        print(str(b[0]) + str(b[1]) + "i")
    elif b[0] == 0 and b[1] != 0:
        print(str(b[1]) + "i")
    elif b[1] == 0:
        print(str(b[0]))
    elif b[0] == 0 and b[1] == 0:
        print(str(0))

def resta_complejos(c1, c2):
    #Efectua la resta de dos numeros complejos c1, c2
    preal = c1[0] - c2[0]
    pimg = c1[1] - c2[1]
    a = [preal, pimg]
    return pretty_res(a)

def pretty_res(a):
    if a[0] > 0 and a[1] > 0:
        print(str(a[0]) + "+" + str(a[1]) + "i" )
    elif a[0] < 0 and a[1] < 0:
        print(str(a[0]) + str(a[1]) + "i")
    elif a[0] < 0 and a[1] > 0:
        print(str(a[0]) + "+" + str(a[1]) + "i" )
    elif a[0] > 0 and a[1] < 0:
        print(str(a[0]) + str(a[1]) + "i")
    elif a[0] == 0 and a[1] != 0:
        print(str(a[1]) + "i")
    elif a[1] == 0:
        print(str(a[0]))
    elif a[0] == 0 and a[1] == 0:
        print(str(0))

def division_complejos(c1, c2):
    #Efectua la division entre dos numeros complejos c1, c2
    preal = (((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0] * c2[0]) + (c2[1] * c2[1])))
    pimg = (((c1[1] * c2[0]) - (c1[0] * c2[1])) / ((c2[0] * c2[0]) + (c2[1] * c2[1])))
    d = [preal, pimg]
    return pretty_div(d)

def pretty_div(d):
    if d[0] > 0 and d[1] > 0:
        print(str(d[0]) + "+" + str(d[1]) + "i" )
    elif d[0] < 0 and d[1] < 0:
        print(str(d[0]) + str(d[1]) + "i")
    elif d[0] < 0 and d[1] > 0:
        print(str(d[0]) + "+" + str(d[1]) + "i" )
    elif d[0] > 0 and d[1] < 0:
        print(str(d[0]) + str(d[1]) + "i")
    elif d[0] == 0 and d[1] != 0:
        print(str(d[1]) + "i")
    elif d[1] == 0:
        print(str(d[0]))
    elif d[0] == 0 and d[1] == 0:
        print(str(0))

def modulo_complejo(c1):
    #Entrega el modulo de un numero complejo
    e = ((c1[0])**2 + (c1[1])**2)**(1/2)
    return e

def conjugado_complejos(c1):
    #Entrega el conjugado de un numero complejo
    conimg = (c1[1]) * (-1)
    f =  [c1[0], conimg]
    return pretty_conj(f)

def pretty_conj(f):
    if f[0] > 0 and f[1] > 0:
        print(str(f[0]) + "+" + str(f[1]) + "i" )
    elif f[0] < 0 and f[1] < 0:
        print(str(f[0]) + str(f[1]) + "i")
    elif f[0] < 0 and f[1] > 0:
        print(str(f[0]) + "+" + str(f[1]) + "i" )
    elif f[0] > 0 and f[1] < 0:
        print(str(f[0]) + str(f[1]) + "i")
    elif f[0] == 0 and f[1] != 0:
        print(str(f[1]) + "i")
    elif f[1] == 0:
        print(str(f[0]))
    elif f[0] == 0 and f[1] == 0:
        print(str(0))

import math
def cart_a_polar(c1):
    # Efectua el cambio de coordenadas cartesianas a polares de un numero complejo, con el uso de math
    r = ((c1[0])**2 + (c1[1])**2)**(1/2)
    θ = ((math.atan(c1[1] / c1[0])) * 180) / math.pi
    z = [r, θ]
    return pretty_polar(z)

def pretty_polar(z):
    print(str(z[0]) + "," + "∠" + str(z[1]) + "°")










