# -*- coding:utf-8 -*-
def  matrixReshape(nums, r, c):
    flat = sum(nums, [])    # convert list of list to list
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)


print matrixReshape([[1,2,3,4,5,6]], 6, 1)

# https://stupidpythonideas.blogspot.de/2013/08/how-grouper-works.html
# ([iter(flat)] * c) will create c number of iter() items that all point
# to the same object a. i.g. i1=i2=iter(a)
