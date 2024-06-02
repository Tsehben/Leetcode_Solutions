def topKFrequent(nums, k):
    # using backet sort, create a two d array 

    # use hashmap to count elements
    count = {}
    freq =[[] for _ in range(len(nums)+ 1) ]
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    for n, c in count.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n) 
            if len(res) == k:
                return res

    

    



print(topKFrequent([1,1,1,2,2,3], 2))
