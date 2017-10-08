# -*- coding:utf-8 -*-
# https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as spip

# 1D
data = np.genfromtxt('data1.txt',
                     delimiter='\t',
                     skip_header=1,
                     names = True,
                     missing_values='INFINITE',
                     filling_values=np.inf)

plt.figure(1)                     
p = plt.plot(data['TK'], data['Cp'], 'kx')
intp = spip.interp1d(data['TK'], data['Cp'],
                     bounds_error=False, fill_value=-999.25,
                     kind = 'cubic')
#print intp(4000)
#plt.show()

# 2D griddata
x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)
tck = spip.splrep(x, y, s=0)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xnew, tck, der=0) # der

#  derivation: splev(xnew, tck, der=1)

# Object Oriented
"""
>>> x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
>>> y = np.sin(x)
>>> s = interpolate.InterpolatedUnivariateSpline(x, y)
>>> xnew = np.arange(0, 2*np.pi, np.pi/50)
>>> ynew = s(xnew)
"""
