def twoSum(nums, target):
    # Brute force using two for loops since although ineeficient()
    n = len(nums) # one time declaration 
    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [i,j]



print(twoSum([2,7,11,15],9))