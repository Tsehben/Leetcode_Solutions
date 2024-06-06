# def ispalindrome(s):
#         l_ptr = 0
#         r_ptr = len(s) - 1
        
#         def alphaNum(c):

#             return (ord('A') <= ord(c) <= ord('Z') or 
#             ord('a') <= ord(c) <= ord('z') or 
#             ord('0') <= ord(c) <= ord('9') )
     
#         while l_ptr < r_ptr:
#             while l_ptr < r_ptr and not alphaNum(s[l_ptr]):
#                 l_ptr += 1
#             while r_ptr > l_ptr and not alphaNum(s[r_ptr]):
#                 r_ptr -= 1


#             if s[l_ptr].lower() != s[r_ptr].lower():
#                 return False
#             l_ptr += 1
#             r_ptr -= 1
            
            

            
#         return True
            
            
            
       
     





   
    # raw_s = ""

    # for char in s:
    #     if char.isalpha() or char.isdigit():
    #         raw_s += char.lower()
    # reversed_s = raw_s[::-1]

    # if raw_s == reversed_s:
    #     return True
    # return False



# print(ispalindrome("aba"))

print("12a".isalnum())