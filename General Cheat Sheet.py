"""LISTS"""

print("\n*************LISTS************\n")

users = ['val', 'rich', 'annie', 'mum', 'dad']

# Testing if a value is in a list, and then if list is empty
if 'val' in users:
    print('Val is in the list')

if users:  # returns False if list is empty, otherwise True
    print('There are users in the user list')

# Accessing elements.  The index of the first element in 0.  The last element iis -1
first_user = users[0]
last_user = users[-1]

# Adding an element to the end of the list, then a t a particular position
users.append('Grandma')
users.insert(3, 'Grandpa')

print(users)

# Removing elements
del users[3]
users.remove('val')
users.pop()
users.pop(0)

print(users)

# Sorting a list
users.sort()  # changes list permanently
print('SORT PERMAMENTLY ' + str(users))
print('SORTED TEMPORARILY ' + str(sorted(users, reverse=True)))  # changes list temporarily
print(users)

# List comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)

# Copying a list
copy_of_list = squares[:]

"""DICTIONARIES"""

print("\n*************DICTIONARIES************\n")

fav_numbers = {'Annie': 8, 'Jim': 4, 'Richard': 9, 'Alison': 10}

length_of_dictionary = len(fav_numbers)
print(length_of_dictionary)

# Accessing values
annies_number = fav_numbers['Annie']
fav_numbers.get('Richard', 9)  # Accessing using Get.  Returns NONE or a default value rather than an error

# Looping through all ke)y-value pairs
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

# Looping through all keys
for name in fav_numbers.keys():
    print('Name is ' + name)

# Looping through all values
for number in fav_numbers.values():
    print('Number is ' + str(number))

# Sorted Dictionary - preserving the order in which keys and valuers are added
from collections import OrderedDict as OrdDict

fav_languages = OrdDict()
fav_languages['Rich'] = ['Python', 'Javascript', 'java']
fav_languages['Annie'] = ['Ruby', 'c']

# Display result in the same order they were entered
for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("- " + lang)

'''If your nesting items much deeper than what you see here there are probably simpler was
of managing your data, such as using classes'''

"""FUNCTIONS"""

print("\n*************FUNCTION OPERATIONS************\n")


# Positional arguments with default value- must be listed after parameters without default values
def describe_pet(pet_name, animal='dog'):

    print('I have a ' + animal + ".  Its name is " + pet_name)


# Using None to make an argument optional
def describe_pet2(animal, pet_name=None):
    print('I have a ' + animal)
    if pet_name:
        print('Its name is ' + pet_name)


describe_pet2('snake')
describe_pet2('hamster', 'Henry')


# Passing an arbitrary number of arguments
def make_pizza(size, *toppings):
    print("\nMaking a " + size + " pizza")
    print("Toppings: ")
    for topping in toppings:
        print(" - " + topping)

make_pizza('large', 'ham', 'pineapple', 'olives')

"""FILE OPERATIONS"""

print("\n*************FILE OPERATIONS************\n")

filename = 'siddhartha.txt'
overwrite_file = 'overwrite.txt'

with open(filename) as file_object:
    contents = file_object.read()  # read entire file at once
    print(contents)

with open(filename) as file_object:
    for line in file_object:  # read line by line
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()  # stores lines in a list
    for line in lines:
        print(line.rstrip())

# Overwriting a file - creates a new file if it doesn't exist
with open(overwrite_file, 'w') as file_object:
    file_object.write('I love programming')

# Appending to a file
with open(overwrite_file, 'a') as file_object:
    file_object.write('\nI love gaming')

# Storing data with JSON - dump simple python data structures into file and load them later

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

new_filename = 'numbers.json'
with open(new_filename) as f_obj:
    numbers_json = json.load(f_obj)
    print(numbers_json)


"""EXCEPTIONS"""

print("\n*************EXCEPTIONS************\n")

#  If you don't know which exception to handle, write code without try statement and generate an error

"""The try block should only contain code that may cause an error
Any code that depends on the try block running successfully should
be placed in the else block"""

try:
    with open('file_doesnt_exist.txt', 'r') as file_object:
        file_object.read()
except FileNotFoundError as e:
    print("Can't find the file{0}.".format(overwrite_file))
    print(e, type(e))
else:
    print('File write successful')
finally:
    print("clean up ")



