import math as m 

#Fonction Secante

def Secante(f, x0, x1, epsilon, Nitermax):
    n=0
    while abs(x0-x1) > epsilon and n < Nitermax:
        x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0, x1 = x1, x2
        n+=1
    return x1 ,n



#Equation 1:

print("="*25,"Equation 1","="*25)
def f1(x):
    return x**4+3*x-9

print(Secante(f1, 1, 2, 1e-10, 5e4))

print("="*20)

print(Secante(f1, -2, -1, 1e-10, 5e4))


#Equation 2:

print("="*25,"Equation 2","="*25)

def f2(x):
    return 3*m.cos(x)-2-x

print(Secante(f2, 0.25 , 1, 1e-10, 5e4))

print("="*20)

print(Secante(f2, -2, -1, 1e-10, 5e4))

print("="*20)

print(Secante(f2, -4.5, -3.5, 1e-10, 5e4))


#Equation 3:

print("="*25,"Equation 3","="*25)

def f3(x):
    return (x*m.exp(x)-7)

print(Secante(f3, 1, 2, 1e-10, 5e4))


#Question 4:

print("="*25,"Question 4","="*25)

def f4(x):
    return m.exp(x)-x-10

print(Secante(f4, 2, 3, 1e-10, 5e4))

print("="*20)

print(Secante(f4, -(9.5), -(10.5), 1e-10, 5e4))


#Question 5:

print("="*25,"Question 5","="*25)

def f5(x):
    return 2*m.tan(x)-x-5

print(Secante(f5, 1, 1.5, 1e-10, 5e4))


#Question 6:

print("="*25,"Question 6","="*25)

def f6(x):
    return m.exp(x)-x**2-3

print(Secante(f6, 1, 2, 1e-10, 5e4))


#Question 7:

print("="*25,"Question 7","="*25)

def f7(x):
    return 3*x+4*m.log(x)-7

print(Secante(f7, 1, 2, 1e-10, 5e4))


#Question 8:

print("="*25,"Question 8","="*25)

def f8(x):
    return ((x**4)-2*x**2+4*x-17)

print(Secante(f8, 1.5, 2.5, 1e-10, 5e4))

print("="*20)

print(Secante(f8, -2, -3, 1e-10, 5e4))


#Question 9:

print("="*25,"Question 9","="*25)

def f9(x):
    return m.exp(x)-2*m.sin(x)-7

print(Secante(f9, 1.5, 2.5, 1e-10, 5e4))


#Question 10:

print("="*25,"Question 10","="*25)

def f10(x):
    return m.log(x**2+4)*m.exp(x)-10

print(Secante(f10, 1, 2, 1e-10, 5e4))



#TP4:

print("="*25,"TP4","="*25)

def f11(x):
    return 2*x-(1+m.sin(x))

print(Secante(f11, 0, 1, 1e-10, 5e4))


