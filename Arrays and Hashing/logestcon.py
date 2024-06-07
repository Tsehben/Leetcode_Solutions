def longestConsecutive(nums):
    set_nums = set(nums)
    long_length = 0

    for num in set_nums:
        
        
        if (num - 1) not in set_nums:
            length = 1
            while (length + num) in set_nums:
                length += 1
            long_length = max(length, long_length)
    return long_length




print(longestConsecutive([100,4,200,1,3,2]))


            
