class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l_ptr = 0
        r_ptr = 1
        count = 1
        n = len(nums)
        while r_ptr <  n:
            if nums[l_ptr] == nums[r_ptr]:
                r_ptr += 1
            else:
                l_ptr += 1
                nums[l_ptr] = nums[r_ptr] 
                count += 1
                r_ptr += 1

        return count
# use two pointer technique to iterate through and change inplace to aavoid duplicates
