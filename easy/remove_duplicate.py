nums=[1,1,2,3,3,4,5,6,6]
def remove_duplicates(nums):
    test_val=nums[0]-1
    for i in range(len(nums)):
        if nums[i] == test_val:
            nums.remove(nums[i])
            nums.append('_')
        else:
            test_val=nums[i]
    return nums

print(remove_duplicates(nums))
