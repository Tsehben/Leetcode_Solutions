# this is going to be the most efficient algorithm
def twoSum(nums, target):
    """ thinking of unpacking elements from array into the hashmap with index value, this will cost space 
      complexity of O(n) since for each element in the array we need to add it to the hash map
      and time of O(n), since we have to iterate through all elements in the hashmap
    """

    nums_dict = {}
    index = 0
    for num in nums:
        nums_dict[num] = index
        index += 1
    
    # at this point we have a hash map with key, value => num , index pair

    """ select first element, find the remainder, do a constant lookup in hashmap, if it workss 
    done, if not move to next element, find remainder, do constant look up and so on
    """
    
    for i in range(len(nums)):
        remainder = target - nums[i] 
        if remainder in nums_dict and nums_dict[remainder] != i:
            return[i, nums_dict[remainder]]
   
   


print(twoSum([3,3], 6))



