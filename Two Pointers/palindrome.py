def ispalindrome(s):

   
    raw_s = ""

    for char in s:
        if char.isalpha() or char.isdigit():
            raw_s += char.lower()
    reversed_s = raw_s[::-1]

    if raw_s == reversed_s:
        return True
    return False



print(ispalindrome("aba"))