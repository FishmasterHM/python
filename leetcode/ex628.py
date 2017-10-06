nums = [1000,1000,2,1,2,5,3,1]
def main(nums):
    olist = sorted(nums)
    if len(olist) > 6:
        olist = olist[:3] + olist[-3:]
    llist = len(olist)
    print olist
    maxo = olist[0] * olist[1] * olist[2]
    print maxo,olist[0] , olist[1] , olist[2]
    for i in xrange(llist-2):
        for j in xrange(i+1, llist-1):
            for k in xrange(j+1, llist):
                maxo = max(maxo, olist[i] * olist[j] * olist[k])
    return maxo

print main(nums)
