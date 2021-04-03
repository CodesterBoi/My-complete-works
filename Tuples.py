#Count Function
t1 = (2,4,7,5,1,8,4,('test',2))
var1 = t1.count(4)
print(var1)

#Arithmetics
x1 = (9,8,7)
x2 = (4,5,6)
x3 = x2 + x1
print(x3)

x4 = ('Antonio', 'Gold')
print(x4*5)

#Length of Tuples
t1 = (2,4,7,5,1,8,4,('test',2))
a = len(t1)
print(a)

#Index Function
t1 = (2,4,7,5,1,8,4,('test',2))
var1 = t1.index(1)
print(var1)

#Del() Tuple Function
t1 = (2,4,7,5,1,8,4,('test',2))
del(t1)

#List to Tuple
list_example = [2,4,7,5,1,8,4]
list_to_tuple = tuple(list_example)
print(list_to_tuple)

#Tuple to List
tuple_example = (3,5,8,6,2,9,5)
tuple_to_list = list(tuple_example)
print(tuple_to_list)
