#Even numbers from 50 to 200:
for z in range(50,201):
    if z%2 == 0:
     print(z)

#Prime numbers from 50 to 200:
for z in range(50,201):
   if z%2 == 1:
     print(z)

#print only string values in output: 'john', 'smith', 'joe'.
list1 = [1,2,'john',5,'smith',1.5,'joe']
for i in range(0,len(list1)):
    if type(list1[i]) =='str':
      print(list1[i])

#print only odd index values:
s = 'Krishna'  
for i in range(0,len(s)):
    if i%2 == 1:
     print(s[i])

#return values more than 3
v = {1,3,2,4,5,6,9,1}
for i in v:
    if i > 3:
        print(i)

#print square of odd values
a = (1,2,3,4,5,6)
for i in a:
    if i%2 == 1:
        print(i*i)

dict1 = {100: 'a', 101: 'b', 103:['c','d','e']}
print(dict1)
dict1_letters = dict1.keys()
dict1_info = dict1.values()
print(dict1_ids)
print(dict1_info)





