def groupAna(strs):
    # first thoughts is brute force

    # iterate through the list and compare in O(n^2) if they are anagrams

    def isAnagram(word1, word2):
        return sorted(word1) == sorted(word2)
    grouped_ana = []
    seen = set()
    for i in range(len(strs)):
        if strs[i] in seen:
            continue
        
        current_ana = [strs[i]]
        seen.add(strs[i])
        for j in range(i+1, len(strs)):
            if isAnagram(strs[i], strs[j]):
                current_ana.append(strs[j])
                seen.add(strs[j])
        grouped_ana.append(current_ana)
                


    return grouped_ana


print(groupAna(["",""]))

