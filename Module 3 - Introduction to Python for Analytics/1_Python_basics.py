##############################################################################
# 1. Variables and Data Types
##############################################################################
# Variables

# Int (whole number) 
4

# Float (decimal point number)
4.6

# String (text string)
"Jim"

# We can store these values in a placeholder, called a variable. 
# The variable can then be called later.

x = 2 + 2
y = "Jim"

print(x)
print(y)

# Be careful when you store values - you should always use new variable names
# Otherwise, you may overwrite the previous value

x = 10
x = "Maria"

print(x)


# You can create more than one variable in a single line. 
# The values are passed into the variables respectively 

a, b = "yellow", "green"

print(a)
print(b)


# Data Types
# To check the type of a variable, we can use Python's built-in function, called *type()* . 
# More info on data types can be found here: https://realpython.com/python-data-types/


a = 4
type(a)

b = 4.6
type(b)

c = "Jim Carrey"
type(c)

d = True
type(d)

# A Boolean value is a True/False value. 
# More info here: https://realpython.com/python-data-types/#boolean-type-boolean-context-and-truthiness

##############################################################################
# 2. Collections
##############################################################################
# Collections are groups of variables. A few examples of collections are:
#
#  - Lists
#  - Tuples
#  - Dictionaries

a_list = [1,2,3,4,5]
print(a_list)
type(a_list)

a_tuple = (1, 2, 3, 4, 5)
print(a_tuple)
type(a_tuple)

a_dictionary = {'GRC': 'Greece', 'EU':'European Union'}
print(a_dictionary)
type(a_dictionary)

#We use indexes (for lists, tuples) and keys (for dictionaries) 
# to access certain values within the collections
a_list[0]
a_list[1]

a_tuple[0]
a_tuple[1]

#Difference list vs tuples. Tuples are immutable 
a_list[0]="100"
print(a_list)

a_tuple[0]="100"
print(a_tuple)

a_dictionary['GRC']
a_dictionary['EU']


#Some collections can store values of different data types
b_list = [1, "40", 1.5]
b_list[1]


##############################################################################
# 3. Operators
##############################################################################
#Python Arithmetic Operators
#https://www.w3schools.com/python/python_operators.asp

a = 2 + 2
b = 2 - 2
c = 1 * 9
d = 12/1.3
print(a, b, c, d)

e = 12//1.3       # Floor division
print(e)


##############################################################################
# 4. Logic Operators
##############################################################################
# If/Else statements are use to control logic flow.

i_know_python = True

if i_know_python:
    print( "Then what are you still doing here?" )

########################################
sky_is_red = False

if sky_is_red:
    print("Red Sky")
else:
    print("No, sky is blue.")

########################################
a = 1.4

if a > 2:
    print("a > 2")
elif a < 1:
    print("a < 1")
else:
    print("a is between 1 and 2")
    
########################################
a = 1.4

if a < 2 and a > 1:
    print("a is between 1 and 2")
    
    

##############################################################################
# 5. Functions
##############################################################################
# We already used Python's built-in functions earlier, 
# such as type() and print(), but we can also build our own.
# Functions take one or more values in, transform them, 
# and then output one or more values.
 
#Define a function that finds the square term of a value    
def double(x):
    return 2*x    
    
double(5)    
    
double(9)    
    
#Define a function that adds two values
def add(num_1, num_2):
    return num_1+num_2

add(6,10)


# x and y only exist within the function - we can't access them outside the function
print("you should see an error below:")
print(num_1)

#Define a function that splits a string
def parse_string(string):
    split_string = str.split(string)
    return split_string

parse_string("Hello World")

parse_string("My name is Dimitris")

parse_string("My name is Dimitris")[0]
parse_string("My name is Dimitris")[3]
parse_string("My name is Dimitris")[4]


##############################################################################
# 6. Classes and Objects
##############################################################################
#Python is an Object-Oriented Programming (OOP) language. 
# Almost everything is an Object, and each object belongs to a Class. 
#More on this here - https://docs.python.org/3/tutorial/classes.html

# lets create our own class - Dog

class Dog:
    def __init__(self, fur_color, size_of_dog):
        self.fur = fur_color
        self.size = size_of_dog

# now, we can create an object from the Dog class
# we need to pass in the required parameters

my_dog_1 = Dog(fur_color='golden', size_of_dog='medium')

# my_dog is an Object of the class Dog 

# classes have "attributes"
# think of these as adjectives that describe the object
print(my_dog_1.fur)
print(my_dog_1.size)
print("My dog 1 has",my_dog_1.fur,"color and is", my_dog_1.size,"sized")


# we can create the class with default parameters so the 
# user doesn't need to specify them if they don't want
class Dog:
    def __init__(self, fur_color='orange', size_of_dog='xx-large'):
        self.fur = fur_color
        self.size = size_of_dog

my_dog_2 = Dog()
my_dog_3 = Dog(size_of_dog='small')

print("My dog 1 has",my_dog_1.fur,"color and is", my_dog_1.size,"sized")
print("My dog 2 has",my_dog_2.fur,"color and is", my_dog_2.size,"sized")
print("My dog 3 has",my_dog_3.fur,"color and is", my_dog_3.size,"sized")



# objects can also have "Methods" - think of these as actions on the object
class Dog:
    def __init__(self, fur_color='golden', size_of_dog='large', status='sitting'):
        self.fur = fur_color
        self.size = size_of_dog
        self.status = status
    
    def run(self):
        self.status= 'running'
        
    def sit(self):
        self.status = 'sitting'
        
    def bark(self, n_barks):
        return n_barks*"Bark"


neighbors_dog = Dog()
print(neighbors_dog.status)

neighbors_dog.run()
print(neighbors_dog.status)

neighbors_dog.sit()
print(neighbors_dog.status)

neighbors_dog.bark(3)














