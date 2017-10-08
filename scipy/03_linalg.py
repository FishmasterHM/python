# -*- coding:utf-8 -*-
import numpy as np
from scipy import linalg as spla
import matplotlib.pyplot as plt
"""
# scipy.linalg has all the functions in numpy.linalg,
# and might be faster 
A = np.array([[1,2],[3,4]])
B = np.array([[5,6]])
print spla.det(A)            # 求行列式
print spla.inv(A)            # 求逆矩阵
print A * B                  # element wise
print A.dot(B.T)             # .T 转置, Matrix multiplication 

# solve linear system
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
B = np.array([[10,8,3]]).T
print spla.solve(A, B)


# np.c_, np.r_
print np.c_[A,B]     # row axis 上a.append(b), also concatenate()
#print np.r_[A,0]
"""

# some example to solve linear least-squares problems (linalg.lstsq)
# example on https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html
# is not correct
c1, c2 = 5.0, 2.0
i = np.r_[1:11]
xi = 0.1 * i
yi = c1 * -xi + c2 * xi
zi = yi + 0.05 * np.max(yi) * np.random.randn(len(yi)) # random points
A = np.c_[np.exp(xi)[:, np.newaxis], xi[:, np.newaxis]] #data elements for x
c, resid, rank, sigma = spla.lstsq(A, zi)

xi2 =  np.r_[0.1:1.0:100j]          # 100j = linspace(), 100 = arange()
yi2 = c[0] * -xi2 + c[1] * xi2
print c, resid
plt.plot(xi, zi, 'o', xi2, yi2)
#plt.axis([0,1.1,3.0,5.5])
plt.show()
