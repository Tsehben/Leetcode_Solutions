# remove Duplicate
l = 1
nums = [1,2,3412,123]
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        nums[l] = nums[i]
        l+=1
print(nums)