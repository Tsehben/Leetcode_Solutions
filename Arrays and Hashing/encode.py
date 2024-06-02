
# most optimal solution with O(m * n )
def encode(strs):

    # iterate throught elements, get length and add a delimiter to each string in the list then combine to one string. 
    new_str = ""
    for s in strs:
        new_str += str(len(s)) + "#" + s
    return new_str





def decode(s):

    res = []
    i = 0
    # iterate throught the encoded string, find the delimeter and the number and form  the substring , then append to the res list

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])

        res.append(s[j+1:  j + 1 + length])
        i = j + 1 + length 

    return res


print(decode(encode(["Hello", "World"])))