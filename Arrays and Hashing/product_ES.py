
def productExceptSelf(nums):
    res = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        res.append(product)

    return res
        

print(productExceptSelf([1,2,3,4]))
