def containsDuplicate(nums):
    
     # I believe this should be the most efficient one 
     # here we will use a set and then check if an element is in the set, once we find it the code ends and returns saving space and time 
     # create a set called seen to keep track of the elements 
     seen = set()

     #itereate throguh and add elements to seen if there are new 
     for num in nums:
        if num in seen:
            # once we see the number already in the seen set, we end implying there is a duplicate
            return True
        seen.add(num)
     return False
# same as what neetcode did 



print(containsDuplicate([1,2,3]))