#Anagram in Python.
'''
a = "Listen"
b = "Silent"

global isAnagram
a = a.lower()
b = b.lower()
def check(a, b):
    if len(a) == len(b):
        if set(a) == set(b):
            for i in range(0, len(a)-1):
                if a[i] != b[i]:
                    isAnagram = False

if(isAnagram):
    print("Both strings are anagrams.")
else:
    print("Both strings aren't anagrams.")
print(set(a))
print(set(b))
'''

#Palindrome in Python.
'''
def isPalindrome(z):
    return z == z[::-1]

z = "radar"
ans = isPalindrome(z)
 
if ans:
    print("Yes. This word is a palindrome.")
else:
    print("No. This word isn't a palindrome.")
'''

#
a = "Sashwit"
b = "Harish"
