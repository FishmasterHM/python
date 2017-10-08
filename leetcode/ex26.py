nums = [1,1,1,2,2,4,5]
begin = 1
save = nums[0]
if len(nums) <= 1:
    print len(nums)
for i in nums:
    if i > save:
        nums[begin] = i
        begin += 1
        save = i
print begin
