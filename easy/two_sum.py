li=[3,2,4]
target=6

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i==j):
                continue
            if((nums[i]+nums[j])==target):
                return [i,j]

print(two_sum(li,target))
