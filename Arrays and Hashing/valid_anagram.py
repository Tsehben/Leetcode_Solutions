# from collections import defaultdict
def isAnagram(s,t):
    #compare the length of string s and string t

    if len(s) != len(t):
        return False
    
    # using a single hashmap

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    # use get which behaves in similar function as default dict
    
    for char in t:
        if char not in count:
            return False
        else:
            count[char] -= 1
    
    for char in count:
        if count[char] != 0:
            return False
  
        return True


# second cheat 
from collections import defaultdict, Counter


def isAnagram_2(s,t):
   return (Counter(s)) == Counter(t)



# print(isAnagram("anagram","angaram"))


