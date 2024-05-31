from collections import defaultdict
def groupAnagrams(strs):

    # our hashmap with key sequence of letters, and value the words that match this sequence

    grouped_map = defaultdict(list)

    # getting sequence of characters in each word

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        grouped_map[tuple(count)].append(s)
    

    return grouped_map.values()


print(list(groupAnagrams(["eat","tea","tan","ate","nat","bat"])))
