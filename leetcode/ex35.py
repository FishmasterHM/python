nums = [1,2,3]
tgt = 3
def main(nums, tgt):
    curl = len(nums)
    bottom = 0
    top = len(nums) - 1
    if curl == 0:
        return 0
    if tgt <= nums[0]:
        return 0
    else:
        while curl > 2:
            halfp = (curl - 1) / 2 + bottom
            if tgt <= nums[halfp]:
                top = halfp
            else:
                bottom = halfp
            curl = len(nums[bottom : top+1])
            print nums[bottom : top+1], top
        return bottom +1

print main(nums, tgt)
