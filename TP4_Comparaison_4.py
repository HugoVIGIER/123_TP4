import math as m
import matplotlib.pyplot as plt
import numpy as np

#Question 3: Equation 3
#Fonction:

def Point_Fixe(g, x0, epsilon, Nitermax):
    L_Pointfixe_n = []
    xold = x0
    xnew = g(xold)
    erreur = g(xold)- xold
    xnew = g(xold)
    n = 1
    L_Pointfixe_xn = []
    L_Pointfixe_en = []
    while abs(erreur) > epsilon and n < Nitermax :
        n = n + 1
        xnew = g(xold)
        erreur = xnew - xold
        xold = xnew
        L_Pointfixe_n.append(n)
        L_Pointfixe_xn.append(xold)
        L_Pointfixe_en.append(abs(erreur))
    return L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en

def g(x) :
    return (7+m.log(x)*(-4))/3

L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en = Point_Fixe(g, 1.7, 1e-10, 5e4)
plt.semilogy(L_Pointfixe_n, L_Pointfixe_en)



def Dichotomie(f, a0, b0, epsilon, Nitermax):
    an = a0
    bn = b0
    n = 1
    L_Dichotomie_n = []
    L_Dichotomie_an = []
    L_Dichotomie_en = []
    while abs(bn - an) > epsilon and n < Nitermax :
        m = (an + bn)/2
        if (f(an)*f(m) <= 0):
            bn = m
        else :
            an = m
        n+=1
        L_Dichotomie_n.append(n)
        L_Dichotomie_an.append(an)
        L_Dichotomie_en.append(abs(bn - an))
    return L_Dichotomie_n, L_Dichotomie_an, L_Dichotomie_en

def f1(x) :
    return 3*x+4*m.log(x)-7


L_Dichotomie_n, L_Dichotomie_an, L_Dichotomie_en = Dichotomie(f1, 1, 2, 1e-10, 5e4)
plt.semilogy(L_Dichotomie_n, L_Dichotomie_en)



def Newton (f, fder, x0, epsilon, Nitermax):
    xold = x0
    xnew = xold-((f(xold))/fder(xold))
    erreur = xnew - xold
    xold = xnew
    n = 1
    L_Newton_n = []
    L_Newton_xn = []
    L_Newton_en = []
    while abs(erreur) > epsilon and n < Nitermax :
        n = n + 1
        xnew = xold - ((f(xold))/fder(xold))
        erreur = xnew - xold
        xold = xnew
        L_Newton_n.append(n)
        L_Newton_xn.append(xold)
        L_Newton_en.append(abs(erreur))
    return L_Newton_n, L_Newton_xn, L_Newton_en

def f2(x) :
    return 3*x+4*m.log(x)-7

def f2der(x):
    return 3+(4/x)

L_Newton_n, L_Newton_xn, L_Newton_en = Newton(f2, f2der, 1.7, 1e-10, 5e4)
plt.semilogy(L_Newton_n, L_Newton_en)



def Secante(f, x0, x1, epsilon, Nitermax):
    n=0
    L_Secante_n = []
    L_Secante_xn = []
    L_Secante_en = []
    while abs(x0-x1) > epsilon and n < Nitermax:
        x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0, x1 = x1, x2
        n+=1
        L_Secante_n.append(n)
        L_Secante_xn.append(x0)
        L_Secante_en.append(abs(x0-x1))
    return L_Secante_n, L_Secante_xn, L_Secante_en

def f3(x):
    return 3*x+4*m.log(x)-7

L_Secante_n, L_Secante_xn, L_Secante_en = Secante(f3, 1, 2, 1e-10, 5e4)
plt.semilogy(L_Secante_n, L_Secante_en)

plt.xlabel("Nombre d'itérations", font = ("Georgia"), fontsize = 10)
plt.ylabel("Ecarts", font = ("Georgia"), fontsize = 10)
plt.title("Evolution des erreurs en fonction du nombre d'itérations", font = ("Georgia"), fontsize = 15)
plt.grid()

plt.show()
