s = "Hello world Hoq   "

res = []
temp = ""
for c in s:
    
    if c != " ":
        temp += c
    elif temp != "":
        res.append(temp)
        temp = ""

if temp != "":
    res.append(temp)


print(res)
