def containsDuplicate(nums):
    # initialize a counter to keep track of each number count
     counter = 1
     n = len(nums)
     # if the counter gives two or more return the function and false
     for i in range(n):
        for j in range(n):
            if i != j:
                if nums[i] == nums[j]:
                    return True
    
     return False
        


print(containsDuplicate([1,1,2]))