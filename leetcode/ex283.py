nums = [0,0,1,0,1,4,0,2,0] 
a = nums[:]
i = 0
for n in nums:
    print n
    if n == 0:
         nums.append(nums.pop(i))
    else:
       i += 1
print nums
        
