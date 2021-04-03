'''
#Reading from a file:
car_name = input("Which car's stats do you want to display?")
t = open("Car_stats.txt","r")
end_of_file = False
print(car_name)

car_name = True

while True:
    car_name = t.readline().strip()
    speed = t.readline().strip()
    acceleration = t.readline().strip()
    handling = t.readline().strip()
    nitro = t.readline().strip()
    break

if bool(car_name):
    print(car_name)
    print("speed: ",speed)
    print("acceleration: ",acceleration)
    print("handling: ",handling)
    print("nitro: ",nitro)

t.close()
'''

'''
#Appending from a file:
t = open("Car stats.txt","a")

car_name = input("Enter the name of your chosen car: ")
speed = input("Enter the value of the car's top speed: ")
acceleration = input("Enter the value of your car's acceleration: ")
handling = input("Enter the value of your car's handling: ")
nitro = input("Enter the value of your car's nitro: ")

print("car_name: "+car_name)
print("speed: "+speed)
print("acceleration: "+acceleration)
print("handling: "+handling)
print("nitro: "+nitro)

t.close()
'''

'''
#Writing from a file:
t = open("Car stats.txt","w")

car_name = input("Enter the name of your chosen car: ")
speed = input("Enter the value of the car's top speed: ")
acceleration = input("Enter the value of your car's acceleration: ")
handling = input("Enter the value of your car's handling: ")
nitro = input("Enter the value of your car's nitro: ")

print("car_name: "+car_name)
print("speed: "+speed)
print("acceleration: "+acceleration)
print("handling: "+handling)
print("nitro: "+nitro)

t.close()
'''

'''
#Overwriting a file.
filecontent = open(Car_stats.txt,"w")
filecontent.write("I solemnly swear that these stats are true.")
filecontent.close()
filecontent = open(Car_stats.txt, "r")
print(filecontent.read())
'''

'''
#Creating a file from scratch.
f = open("Python Mechanics.py", "x")
'''

'''
#Current Working Directory and creating a new folder.
import os
curDir = os.getcwd()
print(curDir)
os.mkdir('Asphalt9')
'''

'''
#Deleting a file
import os
if os.path.exists("12 days of christmas.txt"):
    os.remove("12 days of christmas.txt")
else:
    print("This file doesn't exist.")
'''
