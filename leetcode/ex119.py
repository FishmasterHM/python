class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in xrange(rowIndex):
            row = [x + y for x,y in zip(row + [0], [0] + row)] 
        return row
