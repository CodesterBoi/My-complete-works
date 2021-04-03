("""Q1: a = "South America"
write code to fetch "South" and "America" with help of positive and negative indexing
""")
'''
a = 'South America'
print(a[0:5])
print(a[6:13])
'''

("""
Q2: b = hsaarsihswhiat
write a code to seprate letters at even and odd places and create a word out of it.
output: ['harisha','sashwit']
""")
'''
#Correction:
b = "hsarsihswhiat"
word1 = b[0::2]
word2 = b[1::2]
list1 = []
list1.extend[word1:word2]
'''
("""
Q3: write a program to draw below pattern:
*****
****
***
**
*
""")
#C:(n,0,-1)
'''
def upsidedown_right_triangle(n):
    for i in range(n,0,-1):
        print(''*(n-i)+"*"*i)

upsidedown_right_triangle(5)
'''

("""
Q4: write a function to check whether year is leap year or not
""")
'''
year = 2000
if (year%4) == 0:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
'''

("""
Q5: write a function to do factorial of a number
""")
'''
def function(factorial):
 num = int(input('Enter a number: '))
if num < 0:
    print('Sorry, factorials only exist in positive numbers. Try again.')
elif num == 0:
    print('0 Factorial is 1.')
else:
    for n in range(1, num+1):
        factorial = factorial*n
        print('The factorial of the chosen number', num, 'is', factorial)
'''

("""
Q6: write a while loop code to print sum of 1 to 10
""")
'''
z = 1
while z in range(1,11):
    print(z)
    z = z + 1
''' 

("""
Q7:
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics": 70,
            "history": 80
         }
      }
   }
}
Access the value of ket "Physics"
""")
'''
sampleDict = {"class": ["physics", "history"], ["student name": "Mike"], ["marks": "70", "80"]}
print(sampleDict)
sDict_ids = sampleDict.keys()
sDict_info = sampleDict.values()
print(sDict_ids)
print(sDict_info)

sDict_info_list = list(emp_info)
print(sDict_info_list[1]['class'])
'''

("""
Q8: 
sampleDict = {'a': 100, 'b': 200, 'c': 300}
Check if a value 200 exists in a dictionary
""")
'''
sampleDict = {'a': 100, 'b': 200, 'c': 300}
value = 200
if value in sampleDict.values:
    print(f"Yes, value" '{value}' "exists in dictionary")
'''

("""
Q9:
write a for loop to fetch values from 100 to 200 which are divisble by 5 and 10
""")
'''
for x in range(100,201):
    if x == x/5:
        if x == x/10:
            print(x)
'''

("""
Q10:
write a function to print vowel from a string
""")
'''
str1 = 'Scott'
str1 = str1.casefold()
def vowel_count(string, vowels):
 vowels = ('a','e','i','o','u')
b = vowels
count = {}.fromkeys(vowels, 0)
for b in str1:
    if b in count:
        count[b] += 1
print('Given string: /n', str1)
print('The count of vowels in the string: /n', vowel_count(str1 ,vowels))
'''
