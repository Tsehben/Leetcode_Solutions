def containsDuplicate(nums):
    # using a dictionaty to hash the array, keep track of the counts then check if it counts more than 1
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in dict.values():
        print(i)
    #     if i > 1:
    #         return True
    # return False




print(containsDuplicate([1,2,3,41]))


