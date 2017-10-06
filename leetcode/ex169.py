d = {}
nums = [3,2,3]
for n in nums:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
print max(d.items(), key = lambda x:x[1])[0]

