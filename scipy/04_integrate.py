# -*- coding:utf-8 -*-
import numpy as np
from scipy import integrate
import matplotlib as plt

# help(integrate)
# https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html

# quad alway take the first argument as 'x'
def integrand(x, a, b):
    return a * x ** 2 + b
a = 2
b = 1
I = integrate.quad(integrand, 0, 1, ags=(a,b))
#I = (integration, estimated error)      

# 双重积分
def integrand(t, n, x):
    return np.exp(-x*t) / t ** n

def expint(n, x):
    return quad(integrand, 1, np.inf, args(n,x))[0]

result = quad(lambda x:expint(3, x), 0, np.inf)
#--------------------------------------------
# use dblquad or tplquad, all argument for inner integration must be functions.
def I(n):
    return integrate.dblquad(lambda t,x: np.exp(-x*t) / t ** n,
                             0, np.inf, lambda x:1, lambda x:np.inf)
# none constant limits 
from scipy.integrate import dblquad
area = dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)


# integration with sample points (simps)

def f1(x):
    return x ** 2
x = np.array([1,3,4])
z = f1(x)
I1 = integrate.simps(y, x)
