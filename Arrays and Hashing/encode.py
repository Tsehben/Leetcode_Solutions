new = ""

nam = ["ebe", "kwak", "nyame"]

for i in range(len(nam)):
    if i == len(nam) - 1:
        new += nam[i]
    else:
        new += f"{nam[i]}-"

decoded = []
# use two pointer to keep track of what is happening 

l_ptr = 0
r_ptr = 1
n = len(new) - 1
while r_ptr <= n:
    if new[r_ptr] == '-' :
        decoded.append(new[l_ptr:r_ptr])
    elif r_ptr == n:
        decoded.append(new[l_ptr:r_ptr + 1])

    else:
        r_ptr += 1
        continue
    
    l_ptr = r_ptr + 1
    r_ptr += 1


name = "EBENEzer"
n = 2
print(name[n:n+3])

print(new)
print(decoded)

