# from collections import defaultdict
# def groupAnagrams(strs):

#     # our hashmap with key sequence of letters, and value the words that match this sequence

#     grouped_map = defaultdict(list)

#     # getting sequence of characters in each word

#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         grouped_map[tuple(count)].append(s)
    

#     return grouped_map.values()


# print(list(groupAnagrams(["eat","tea","tan","ate","nat","bat"])))

# n = 4
# for i in range(1, n + 1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(1, 2*i):
#         print("*", end="")
     
#     print()


# for i in range(n):

#     for j in range(i+1):
#         print("*", end="")
#     print()

# n_word = "abcd"
# s_word = list(n_word)
# l_ptr = 0
# r_ptr = len(n_word) - 1

# while l_ptr < r_ptr:
#     s_word[l_ptr], s_word[r_ptr] = s_word[r_ptr], s_word[l_ptr]
#     l_ptr += 1
#     r_ptr -= 1

# print(list(reversed(n_word)))

roman = "XCIXO"

r_d = {"I":1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
total = 0
previous_value = 0
for char in reversed(roman):
   if char in r_d:
     value = r_d[char]
     if previous_value > value:
        total -= value
     else:
        total += value
     previous_value = value

print(total)
