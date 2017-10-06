"""
import numpy as np
import numpy.ma as ma
a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
a = np.array(a)
lrow, lcol = a.shape
b = np.insert(a,(0,lcol),-1,axis=1)
mones = np.zeros((1,lcol+2),dtype=np.int)-1
b = np.concatenate((b, mones), axis=0)
b = np.concatenate((mones, b), axis=0)
b = ma.masked_values(b, -1)
print b

for c in xrange(1, lcol+1):
    for r in xrange(1, lrow+1):
        a[r-1, c-1] = b[r-1:r+2, c-1:c+2].mean()
        #print  b[r-1:r+2, c-1:c+2]

print a
"""

a = [[2,3,4],[5,6,7],[8,9,10],[11,12,13]]
lrow = len(a)
lcol = len(a[0])
switch = []
for i in range(-1, 2):
    for j in range(-1, 2):
        switch.append([i, j])
out = [[0 for n in xrange(lcol)] for n in xrange(lrow)]
for r in xrange(lrow):
    for c in xrange(lcol):
        counter = 0
        total = 0
        for rs, cs in switch:
            vr = r + rs
            vc = c + cs
            if vr < 0 or vc < 0 or vr == lrow or vc == lcol:
                continue
            total += a[vr][vc]
            counter += 1
        print total,counter,r,c
        out[r][c] = int(total/counter)
print out
