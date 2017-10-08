def main(nums):      
    if len(nums) <= 1:
        return len(nums)
        
    minp = float('inf')
    for l in xrange(1, len(nums)):
        if nums[l] < nums[l-1]:
            minp = min(minp, nums[l])
    
    maxp = -float('inf')
    for r in xrange(len(nums)-2, -1, -1):
        if nums[r] > nums[r+1]:
            maxp = max(maxp, nums[r])
       
    if minp == float('inf'):
        return 0      
 
    head = 0
    tail = len(nums) -1
    while minp >= nums[0]:
        nums.pop(0)
        head += 1

    while maxp <= nums[-1]:
        print 'aaa'
        nums.pop()
        tail -= 1
    print tail, head
    return tail - head + 1

nums = [1,3,2,3,3]
print main(nums)
