from collections import defaultdict
def topKFrequent(nums, k):
    # count all the elements in the array using the hashmap
    count = {}
    for num in nums:
        if num in count:
            count[num]+= 1
        else:
            count[num] = 1

    sorted_values = sorted(count.values(), reverse = True)


    grouped = []
    
    # for i in sorted_values[:k]:
    #     num = list(count.keys())[list(count.values()).index(i)]
    #     grouped.append(i)

    for num in count.keys():
        if count[num] in sorted_values[:k]:
            grouped.append(num)

    
    



    return grouped

nums = [1,1,1,2,2,3]
k = 2
    


print(topKFrequent(nums,k))