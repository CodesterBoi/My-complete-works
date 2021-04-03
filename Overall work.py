#1
Z1 = [995, 896, 797, 698, 599]
def Average(Z1):
    return sum(Z1)/len(Z1)
average = Average(Z1) 
print("Average of the list =", round(average, 2))

#2
LA = ["a", "b", "a", "c", "d", "b", "c", "e"]
LA = list(dict.fromkeys(LA))
print(LA)

#3
def upperlower(string):
    upper = 0
    lower = 0
  
    for i in range(len(string)): 
          
        #Lower
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122): 
            lower += 1
        #Upper
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90): 
            upper += 1
  
    print('Lower case characters = %s' %lower, 
          'Upper case characters = %s' %upper) 
  
string = 'A GREAT WAY TO EMBARRASS YOURSELF. Yeah right.'
upperlower(string) 

#4
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(word_count('Suddenly, the room shook with such force that all the items collapsed without notice.'))

#5
t1 = (1,2,3,4,5,6,7,8,9,10)
print(t1[0:5])
print(t1[5:10])

#6
v1 = 413364
v2 = 463314
sum = int(v1) + int(v2)
print("The sum of given numbers is: ", sum)

