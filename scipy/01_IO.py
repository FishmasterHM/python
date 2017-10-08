# -*- coding:utf-8 -*-

# https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io

from scipy import io as spio
import numpy as np

a = np.ones((3,3), dtype=int)
spio.savemat('file.mat',{'a': a})
data = spio.loadmat('file.mat')
print spio.mminfo(data['a'])
