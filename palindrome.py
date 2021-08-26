def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = str(input("enter the word of your choice"))

ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
