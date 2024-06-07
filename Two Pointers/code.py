# def validPara(s):
#     stack = []
#     closeToOpen = {")": "(", "}":"{", "]":"["}
#     for c in s:
#         if c in closeToOpen:
#             if stack and stack[-1] == closeToOpen[c]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(c)
    
#     if not stack:
#         return True
#     return False

""" Kth largest element in a stream """

nums = [1,2,3,4,1,2]