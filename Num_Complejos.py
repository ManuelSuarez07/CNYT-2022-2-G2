def suma_complejos(c1, c2):
    pral = c1[0] + c2[0]
    pimp = c1[1] + c2[1]
    c = [preal, pimg]
    return pretty_sum(c)
def pretty_sum(c):
    if c[0] and c[1] > 0:
        print(str(c[0]) + "+" + str(c[1]) + "i" )
    elif c[1] < 0:
        print(str(c[0]) + "-" + str(c[1]) + "i" )
    elif c[0] and c[1] < 0 :
        print("-" + str(c[0]) + "-" + str(c[1]) + "i")
    elif c[0] < 0:
        print("-" + str(c[0]) + "+" + str(c[1]) + "i")
    elif c[0] = 0:
        print(str(c[1]) + "i")
    elif c[1] = 0:
        print(str(c[0]))
    elif c[0] and c[1] = 0:
        print(str(0))
print(suma_complejos([1,-1],[1,2]))
print(suma_complejos([-1,-1],[1,1]))
print(suma_complejos([1,-1],[-1,2]))
print(suma_complejos([1,-1],[1,1]))
print(suma_complejos([1,-1],[1,-2]))
print(suma_complejos([-1,-1],[-1,2]))