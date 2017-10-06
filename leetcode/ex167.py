class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        b, e = 0, len(numbers)-1
        while b < e:
            s = numbers[b] + numbers[e]
            if s == target:
                return [b+1, e+1]
            elif s < target:
                b += 1
            else: 
                e -= 1
