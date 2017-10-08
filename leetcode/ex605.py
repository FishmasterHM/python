flowerbed = [1,0,0,0,0,1]
n = 2   
"""   
for i in xrange(len(flowerbed)):
    print sum(flowerbed[max(0, i-1) : i+1]), flowerbed[max(0, i-1) : i+2], i
    if sum(flowerbed[max(0, i-1) : i+2]) == 0:
        flowerbed[i] = 1
        n -= 1
        if n <= 0:
            print flowerbed
            print True
print False
"""
class Solution2(object):        #faster!
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        counter = 1
        for i in xrange(len(flowerbed)):
            if flowerbed[i] == 0:
                counter += 1
                if i == len(flowerbed) - 1:
                    n -= counter/2
            else:
                n -= (counter - 1)/2
                counter = 0
        return n <= 0
        
