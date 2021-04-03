#Indexing.
#Items() function
#fruits_items = {'f1': "Apple", 'f2': "Banana", 'f3': "Mango", 'f4': "Kiwi", 'f5': "Blackberry"}
#print(fruits)
#print(type(fruits))
#print(len(fruits)
#fruits_items_list = list(fruits_items)
#print(fruits_items_list[2][1])

#Keys() Function.
#fruits_keys = fruits.keys()
#print(fruits_keys)
#fruits_keys_list = list(fruits_keys)
#print(fruits_keys_list)

#Values() Function.
#fruits_values = fruits.keys()
#print(fruits.keys)
#fruits_values_list = list(fruits_values)
#print(fruits_values_list)

#Update() Function.
#fruits.update({'f6': "Strawberry"})
#print(fruits)

#Pop() Function.
#fruits.pop('f4')
#print(fruits)

#Popitem() Function.
#fruits.popitem()
#print(fruits)

#Dictionary w/ multiple values.
items = {'fruits': ["Apple", "Blackberry", "Mango"], 'veggies': ["Carrot", "Garlic", "Beans"], 'companies': ["Gymshark", "KWD", "Jordan"]}
print(items)
print(items.keys())
print(items.values())

#Nested Dictionary.
employee = {173956: {'name': "Connor", 'age': "22", 'gender': "male"}, 132597: {'name': "Anton", 'age': 40, 'gender': "male"}}
print(employee)
emp_ids = employee.keys()
emp_info = employee.values()
print(emp_ids)
print(emp_info)

emp_info_list = list(emp_info)
print(emp_info_list[1]['name'])
