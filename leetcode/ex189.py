nums = [1,2,3,4,5]
k = -4
def main(nums, k):
    realk = k % len(nums)
       
    if realk >= 0:
        a = nums[-realk:]
        nums[realk:] = nums[:-realk]
        nums[:realk] = a[:]
    else:
        a = nums[:-realk]
        nums[:realk] = nums[realk:]
        nums[real:] = a
    return nums

print main(nums, k)
