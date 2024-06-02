def topKFrequent(nums, k):
    # first count to  get the frequency of the nums
    # sort the elements in the hashmap into a 2d array using bucket sort, to store the elements 
    # with the bucket sort having the frequency of the numbers, we can first k elements in a descending order 


    # count

    count = {}

    for num in nums:
        count[num] = 1 + count.get(num, 0) 

    # create a frequency two d array, append elemnts at the frequency. in O(n)

    freq = [[] for _ in range(len(nums) + 1)]

    # itereate through the hashmap geting key value pairs, 

    for num, f in count.items():
        freq[f].append(num)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res





print(topKFrequent([1,1,1,2,2,3], 2))
