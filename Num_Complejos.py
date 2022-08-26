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
    #Efectua el
    preal = (c1[0] * c2[0]) - (c1[1] * c2[1])
    pimg = (c1[0] * c2[1]) + (c1[1] * c2[0])
    b = [preal, pimg]
    return pretty_prod(b)
def pretty_prod(b):

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


